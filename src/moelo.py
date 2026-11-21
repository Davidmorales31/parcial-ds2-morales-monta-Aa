 
from pathlib import Path
import math


class MesaDeAyuda:
    def __init__(self, tickets, mu):
        self.tickets = []
        for ticket in tickets:
            self.tickets.append(dict(ticket))
        self.tickets.sort(key=lambda ticket: (ticket['llegada_min'], ticket['_id']))
        if not self.tickets or not math.isfinite(mu) or mu <= 0:
            raise ValueError('Se requieren tickets y una tasa de servicio positiva.')
        for ticket in self.tickets:
            if ticket['llegada_min'] < 0 or ticket['atencion_min'] <= 0:
                raise ValueError('Las llegadas deben ser no negativas y las atenciones positivas.')
        self.mu = float(mu)

    def tasa_llegadas(self):
 
        duracion = self.tickets[-1]['llegada_min'] - self.tickets[0]['llegada_min']
        if len(self.tickets) < 2 or duracion <= 0:
            raise ValueError('Se requieren al menos dos llegadas en tiempos distintos.')
        return (len(self.tickets) - 1) * 60 / duracion

    def metricas_mm1(self, tasa_llegadas):
        if not math.isfinite(tasa_llegadas) or tasa_llegadas < 0 or tasa_llegadas >= self.mu:
            raise ValueError('El equilibrio M/M/1 requiere 0 <= lambda < mu.')
        utilizacion = tasa_llegadas / self.mu
        longitud_cola = utilizacion ** 2 / (1 - utilizacion)
        espera_horas = utilizacion / (self.mu - tasa_llegadas)
        return {'lambda': tasa_llegadas, 'mu': self.mu, 'rho': utilizacion,
                'Lq': longitud_cola, 'Wq_horas': espera_horas}

    def simular(self):
        fin = 0
        resultado = []
        for ticket in self.tickets:
            inicio = max(ticket['llegada_min'], fin)
            fin = inicio + ticket['atencion_min']
            resultado.append({'ticket': ticket['_id'], 'llegada_min': ticket['llegada_min'],
                              'inicio_min': inicio, 'fin_min': fin,
                              'espera_min': inicio - ticket['llegada_min']})
        return resultado

    def graficar(self, destino):
        import matplotlib
        matplotlib.use('Agg')
        import matplotlib.pyplot as plt
        datos = self.simular()
        teorica = self.metricas_mm1(self.tasa_llegadas())['Wq_horas'] * 60
        codigos = []
        esperas = []
        for resultado in datos:
            codigos.append(resultado['ticket'])
            esperas.append(resultado['espera_min'])
        media = sum(esperas) / len(esperas)
        figura, ejes = plt.subplots(figsize=(10, 5.5))
        ejes.bar(codigos, esperas,
               color='#2563eb', label='Espera simulada FIFO')
        ejes.axhline(media, color='#059669', linestyle='--', label=f'Media simulada: {media:.2f} min')
        ejes.axhline(teorica, color='#dc2626', linestyle=':', label=f'Media M/M/1: {teorica:.2f} min')
        ejes.set(title='HuilaSoft · Espera en la mesa de ayuda', xlabel='Ticket', ylabel='Espera en cola (minutos)')
        ejes.set_ylim(0, teorica * 1.25)
        ejes.legend()
        ejes.grid(axis='y', alpha=.2)
        figura.tight_layout()
        destino = Path(destino)
        destino.parent.mkdir(parents=True, exist_ok=True)
        figura.savefig(destino, dpi=180)
        plt.close(figura)
