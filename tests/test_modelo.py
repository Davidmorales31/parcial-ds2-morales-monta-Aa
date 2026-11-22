import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))
from modelo import MesaDeAyuda


#pruebas pa ver si la mesa de ayuda funciona bien 
def test_es ():
    modelo = MesaDeAyuda([
        {'_id': 'T1', 'minutoLlegada': 0, 'minutoAtencion': 5}
    ], 10)
    assert abs(modelo.metricas_mm1(8)['Wq_horas'] - 0.4) < 0.000001


def test_simu():
    llegadas  = [0, 3, 6, 14, 25, 28, 40, 52]
    atenciones = [5, 7, 4, 8, 6, 5, 9, 4]
    tickets = []
    for i in range(8):
        tickets.append({'_id': 'T' + str(i + 1),
                        'minutoLlegada': llegadas[i],
                        'minutoAtencion': atenciones[i]})
    modelo = MesaDeAyuda(tickets, 10)
    espras = []
    for resltado in modelo.simular():
        espras.append(resltado['espera_min'])
    assert espras == [0, 2, 6, 2, 0, 3, 0, 0]


if __name__ == '__main__':
    test_es()
    test_simu ()
    print('las pruebas pasaron siuuuu')