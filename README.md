## Nosotros 

Juan Morales | Sofia Montaña 

# parcial-ds2-morales-monta-Aa

Creamos las base llamanola matriculaAPP, con tres colecciones, pruebas, tickets y Agente
 
prueba tiene los campos semana y defectos_nuevos
tickets tiene el campo id, minutoLLlegada, minutoAtencion y prioridad ademas de la relacion con la tabla de agentes 
 
 Agente tiene el campo de id , nombre, nivel, tikcts x hora y el esto e si esya en turno o no

 

## Ejecución

La ejecucion esta en local, apuntano al puerto 27017, se ejecuta con los siguientes comanados 

py -m pip install -r pymongo
py -m pip install -r matplotlib

mongosh --file mongo/script_mongosh.js
py src/main.py


## fase 2 
Escogimos la opción A: teoría de colas, con la clase MesaDeAyuda.
  

 
