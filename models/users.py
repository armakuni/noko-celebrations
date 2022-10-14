from pydantic import BaseModel, EmailStr


class NokoUser(BaseModel):
    id: int
    email: EmailStr
    first_name: str
    last_name: str
