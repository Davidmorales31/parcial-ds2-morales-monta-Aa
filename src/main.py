"""creamos el main.py para hacer las consulta los tickets y muestra los resultados de la mesa de ayuda."""
""" Nosotros escogemos el caso de la mesa de ayuda """
 
import json
import os
from pathlib import Path
from pymongo import MongoClient
from modelo import MesaDeAyuda

#esto es la conexion a la base de datos local
#queda en el puerto 27017  

def ejecutar():
    global resumen, simulacion

    cliente=MongoClient(os.environ.get('MONGODB_URI','mongodb://localhost:27017'),serverSelectionTimeoutMS=5000)

    base_datos=cliente['MatriculaAPP']
 

    agente=base_datos['Agente'].find_one({'_id':'1','en_turno':True})

   
    tickets=list(base_datos.tickets.find({'agente_id':agente['_id']}))
 
    modelo=MesaDeAyuda(tickets,agente['tickets_hora'])
    
    cliente.close()
    m=modelo.metricas_mm1(modelo.tasa_llegadas())
    simulacion=modelo.simular()
    suma=0
    for i in range(len(simulacion)):
        suma=suma+simulacion[i]['espera_min']
    promedio=suma/len(simulacion)
    resumen={'metricas':m,'espera_teorica_min':m['Wq_horas']*60,'simulacion':simulacion,'espera_media_simulada_min':promedio,'Wq_demanda_9_5_min':modelo.metricas_mm1(9.5)['Wq_horas']*60}
    raiz=Path(__file__).resolve().parents[1]
    modelo.graficar(raiz/'graficas'/'resultado.png')
    texto=json.dumps(resumen,indent=2,ensure_ascii=False)
    f=open(raiz/'graficas'/'resultados.json','w',encoding='utf-8')
    f.write(texto)
    f.close()
    print(texto)

if __name__=='__main__':
  ejecutar()