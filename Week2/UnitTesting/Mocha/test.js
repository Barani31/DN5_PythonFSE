const add=require("./calculator");

const expect=require("chai").expect;

describe(

"Addition",

()=>{

it(

"adds",

()=>{

expect(

add(2,3)

).to.equal(5);

});

});