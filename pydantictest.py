from pydantic import BaseModel, ValidationError

class Product(BaseModel):
    item_name: str
    price: float

try:
    p = Product(item_name="Phone", price=10.0)
except ValidationError as e:
    print("Erro de validação:", e)
finally:
    # Method that converts the data set into a dictionary
    print(p.model_dump())
    # Method that converts the data set into a JSON object
    print(p.model_dump_json())