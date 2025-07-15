from pydantic import BaseModel, ValidationError

class Produto(BaseModel):
    nome: str
    preco: float

try:
    p = Produto(nome="Celular", preco=10.0)
except ValidationError as e:
    print("Erro de validação:", e)
print(f'{p}')
