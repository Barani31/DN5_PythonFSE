from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String

engine = create_engine("sqlite:///college.db")

metadata = MetaData()

student = Table(

"student",

metadata,

Column("id",Integer,primary_key=True),

Column("name",String),

Column("age",Integer)

)

metadata.create_all(engine)

print("Database Created")