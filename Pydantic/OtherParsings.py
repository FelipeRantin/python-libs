from pydantic import EmailStr, BaseModel

# Email
class User(BaseModel):
    email: EmailStr
    password: str

user1 = User (email = 'john123@gmail.com', password = '123456')