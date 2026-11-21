// Aqui inciaimos con la ceacon e los atos e caso A /


// Inicamos la Base e taos e mongose


db = db.getSiblingDB('MatriculaAPP');



// Si no existe creaos los agentes nosotros lo creamos : )
if (db.Agente.countDocuments({}) === 0) {
  db.Agente.insertMany([
    {_id: '1', nombre: 'Sofia Montala', nivel: 'senior', tickets_hora: 10, en_turno: true},
    {_id: '2', nombre: 'Morales Davidd ', nivel: 'junior', tickets_hora: 6, en_turno: false}
  ]);
}



if (db.tickets.countDocuments({}) === 0) {
  db.tickets.insertMany([
    {_id:'T1', llegada_min:0, atencion_min:5, prioridad:'Alta', agente_id:'1'},
    {_id:'T2', llegada_min:3, atencion_min:7, prioridad:'Alta', agente_id:'1'},
    {_id:'T3', llegada_min:6, atencion_min:4, prioridad:'Media', agente_id:'1'},
    {_id:'T4', llegada_min:14, atencion_min:8, prioridad:'Baja', agente_id:'1'},
    {_id:'T5', llegada_min:25, atencion_min:6, prioridad:'Alta', agente_id:'1'},
    {_id:'T6', llegada_min:28, atencion_min:5, prioridad:'Media', agente_id:'1'},
    {_id:'T7', llegada_min:40, atencion_min:9, prioridad:'Baja', agente_id:'1'},
    {_id:'T8', llegada_min:52, atencion_min:4, prioridad:'Alta', agente_id:'1'}
  ]);
}


if (db.pruebas.countDocuments({}) === 0) {
  db.pruebas.insertMany([28,23,22,17,16,12,12,9].map((n,i) => ({_id:i+1, semana:i+1, defectos_nuevos:n})));
}

print('Tickets de prioridad Alta');


printjson(db.tickets.find({prioridad:'Alta'}).toArray());


print('Tickets con atención mayor a 6 minutos');


printjson(db.tickets.find({atencion_min:{$gt:6}}).toArray());

print('Semanas con menos de 15 defectos');

printjson(db.pruebas.find({defectos_nuevos:{$lt:15}}).toArray());
 

 