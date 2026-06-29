db.employees.createIndex({

department:1

})

db.employees.createIndex({

department:1,

salary:-1

})

db.employees.getIndexes()

db.employees.dropIndex({

department:1

})