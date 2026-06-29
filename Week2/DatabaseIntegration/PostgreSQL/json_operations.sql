CREATE TABLE Products(

id SERIAL PRIMARY KEY,

details JSONB

);

INSERT INTO Products(details)

VALUES

('{

"name":"Laptop",

"price":65000,

"brand":"Dell"

}');

SELECT

details->>'name'

FROM Products;

SELECT

details->>'price'

FROM Products;

UPDATE Products

SET details=jsonb_set(

details,

'{price}',

'70000'

)

WHERE id=1;