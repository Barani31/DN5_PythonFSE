const sum=require('./sum');

test(

'adds',

()=>{

expect(

sum(2,3)

).toBe(5);

}

);