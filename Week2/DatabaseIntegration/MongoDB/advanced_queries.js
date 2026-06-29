db.employees.find({

salary:{

$gt:50000

}

})

db.employees.find({

salary:{

$lt:60000

}

})

db.employees.find({

department:"IT",

salary:{

$gt:50000

}

})

db.employees.find({

$or:[

{

department:"IT"

},

{

department:"HR"

}

]

})

db.employees.find({

name:/^B/

})

db.employees.find(

{},

{

name:1,

salary:1,

_id:0

}

)

db.employees.find().sort({

salary:-1

})

db.employees.find().limit(2)

db.employees.find().skip(1)