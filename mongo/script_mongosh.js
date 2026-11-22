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



if (db.tickets.countDocuments({}) === 0)
   {
  db.tickets.insertMany([
    {_id:'T1', minutoLlegada:0, minutoAtencion:5, prioridad:'Alta', agente_id:'1'},
    {_id:'T2', minutoLlegada:3, minutoAtencion:7, prioridad:'Alta', agente_id:'1'},
    {_id:'T3', minutoLlegada:6, minutoAtencion:4, prioridad:'Media', agente_id:'1'},
    {_id:'T4', minutoLlegada:14, minutoAtencion:8, prioridad:'Baja', agente_id:'1'},
    {_id:'T5', minutoLlegada:25, minutoAtencion:6, prioridad:'Alta', agente_id:'1'},
    {_id:'T6', minutoLlegada:28, minutoAtencion:5, prioridad:'Media', agente_id:'1'},
    {_id:'T7', minutoLlegada:40, minutoAtencion:9, prioridad:'Baja', agente_id:'1'},
    {_id:'T8', minutoLlegada:52, minutoAtencion:4, prioridad:'Alta', agente_id:'1'}
  ]
);
}


if (db.pruebas.countDocuments({}) === 0) {
  db.pruebas.insertMany([28,23,22,17,16,12,12,9].map((n,i) => ({_id:i+1, semana:i+1, defectos_nuevos:n})));
}

print('Tickets de prioridad Alta');


printjson(db.tickets.find({prioridad:'Alta'}).toArray());


print('Tickets con atención mayor a 6 minutos');


printjson(db.tickets.find({minutoAtencion:{$gt:6}}).toArray());

print('Semanas con menos de 15 defectos');

printjson(db.pruebas.find({defectos_nuevos:{$lt:15}}).toArray());

print('Actualizar T7 a prioridad Media');
printjson(db.tickets.updateOne({_id: 'T7'}, {$set: {prioridad: 'Media'}}));
printjson(db.tickets.findOne({_id: 'T7'}));
 

 
