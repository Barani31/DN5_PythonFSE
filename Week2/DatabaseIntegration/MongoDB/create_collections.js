
db.createCollection("employees")

db.employees.insertOne({

emp_id:1,

name:"Barani",

department:"IT",

salary:50000

})

db.employees.insertMany([

{

emp_id:2,

name:"Arun",

department:"HR",

salary:40000

},

{

emp_id:3,

name:"John",

department:"IT",

salary:65000

}

])

