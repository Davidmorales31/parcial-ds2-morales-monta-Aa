from pathlib import *
import math

#clase pa manejar la mesa de ayuda, toca no cambiar los nombres de los metodos porque main.py los usa
class MesaDeAyuda:
  def __init__(self,tickets,mu):
    self.tickets=[]
    for tiket in tickets:
       self.tickets.append(dict(tiket))
    self.tickets.sort(key=lambda tiket:(tiket['minutoLlegada'],tiket['_id']))
    if not self.tickets or not math.isfinite(mu) or mu<=0:
        raise ValueError('se nesecitan tickets y una tasa de servisio positiva, ojo')
    for tiket in self.tickets:
      if tiket['minutoLlegada']<0 or tiket['minutoAtencion']<=0:
        raise ValueError('las llegadas tienen que ser no negativas y las atenciones positivas')
    self.mu=float(mu)

  def tasa_llegadas(self):
    #calcula la tasa de llegadas pa la hora, si no hay tiempos distintos no sirve
    duracyon=self.tickets[-1]['minutoLlegada']-self.tickets[0]['minutoLlegada']
    if len(self.tickets)<2 or duracyon<=0:
      raise ValueError('se requieren al menos dos llegadas en tiempos distintos pues')
    return (len(self.tickets)-1)*60/duracyon

  def metricas_mm1(self,tasa_llegadass):
    if not math.isfinite(tasa_llegadass) or tasa_llegadass<0 or tasa_llegadass>=self.mu:
      raise ValueError('el equilibrio M/M/1 requiere 0 <= lambda < mu, si no se rompe')
    utilisacion=tasa_llegadass/self.mu
    longitut_cola=utilisacion**2/(1-utilisacion)
    esperaa_oras=utilisacion/(self.mu-tasa_llegadass)
    return {'lambda':tasa_llegadass,'mu':self.mu,'rho':utilisacion,
            'Lq':longitut_cola,'Wq_horas':esperaa_oras}

  def simular(self):
    #simulasion de la cola FIFO, el que yega primero se atiende primero, listo
    fn=0
    resltado=[]
    for tiket in self.tickets:
      inisio=max(tiket['minutoLlegada'],fn)
      fn=inisio+tiket['minutoAtencion']
      resltado.append({'ticket':tiket['_id'],'minutoLlegada':tiket['minutoLlegada'],
                        'inicio_min':inisio,'fin_min':fn,
                        'espera_min':inisio-tiket['minutoLlegada']})
    return resltado

  def graficar(self,destyno):
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    dathos=self.simular()
    teorika=self.metricas_mm1(self.tasa_llegadas())['Wq_horas']*60
    kodigos=[]
    esperas=[]
    for resltado in dathos:
      kodigos.append(resltado['ticket'])
      esperas.append(resltado['espera_min'])
    medya=sum(esperas)/len(esperas)
    figurra,ehjes=plt.subplots(figsize=(10,5.5))
    ehjes.bar(kodigos,esperas,
             color='#2563eb',label='Espera simulada FIFO')
    ehjes.axhline(medya,color='#059669',linestyle='--',label=f'Media simulada: {medya:.2f} min')
    ehjes.axhline(teorika,color='#dc2626',linestyle=':',label=f'Media M/M/1: {teorika:.2f} min')
    ehjes.set(title='HuilaSoft · Espera en la mesa de ayuda',xlabel='Ticket',ylabel='Espera en cola (minutos)')
    ehjes.set_ylim(0,teorika*1.25)
    ehjes.legend()
    ehjes.grid(axis='y',alpha=.2)
    figurra.tight_layout()
    destyno=Path(destyno)
    destyno.parent.mkdir(parents=True,exist_ok=True)
    figurra.savefig(destyno,dpi=180)
    plt.close(figurra)