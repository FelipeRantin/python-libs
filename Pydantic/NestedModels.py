from pydantic import BaseModel
from typing import List

class Food(BaseModel):
    name: str
    price: float
    ingredients: List[str] = None


class Restaurant(BaseModel):
    name : str
    location: str
    # Nesting the 'Food' model into the restaurant model
    foods: List[Food]

lukes = Restaurant(
    name="Luke's",
    location="Stars Hollow, CT",
    foods=[
        {"name": "Cheese Pizza", "price": 12.50, "ingredients": ["Cheese", "Tomato Sauce", "Dough"]},
        {"name": "Veggie Burger", "price": 8.99}
    ]
)