from pydantic import BaseModel

class Product(BaseModel):
    item_name: str
    price: float

p = Product(item_name="Phone", price=10.0)
# Method that converts the data set into a dictionary
print(p.model_dump())
# Method that converts the data set into a JSON object
print(p.model_dump_json())