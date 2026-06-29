db.employees.aggregate([

{

$group:{

_id:"$department",

avgSalary:{

$avg:"$salary"

}

}

}

])


db.employees.aggregate([

{

$group:{

_id:"$department",

count:{

$sum:1

}

}

}

])


db.employees.aggregate([

{

$group:{

_id:null,

maxSalary:{

$max:"$salary"

}

}

}

])


db.employees.aggregate([

{

$sort:{

salary:-1

}

}

])