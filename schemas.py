from pydantic import BaseModel

class UserCreate(BaseModel):
    name: str
    email: str
    password: str


class RoleCreate(BaseModel):
    name: str


class UserRoleCreate(BaseModel):
    user_id: int
    role_id: int
    