db.employees.find()

db.employees.findOne({

emp_id:1

})

db.employees.updateOne(

{

emp_id:1

},

{

$set:{

salary:60000

}

}

)

db.employees.deleteOne({

emp_id:2

})

db.employees.deleteMany({

department:"HR"

})