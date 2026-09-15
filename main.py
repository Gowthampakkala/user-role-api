from fastapi import FastAPI
from sqlalchemy.orm import Session

from database import engine, SessionLocal
from models import Base, User, Role, UserRole
from schemas import UserCreate, RoleCreate, UserRoleCreate

Base.metadata.create_all(bind=engine)

app = FastAPI()



@app.post("/users")
def create_user(user: UserCreate):

    db: Session = SessionLocal()

    new_user = User(
        name=user.name,
        email=user.email,
        password=user.password
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    db.close()

    return new_user


@app.get("/users")
def get_users():

    db: Session = SessionLocal()

    users = db.query(User).all()

    db.close()

    return users


@app.post("/roles")
def create_role(role: RoleCreate):

    db: Session = SessionLocal()

    new_role = Role(name=role.name)

    db.add(new_role)
    db.commit()
    db.refresh(new_role)

    db.close()

    return new_role


@app.get("/roles")
def get_roles():

    db: Session = SessionLocal()

    roles = db.query(Role).all()

    db.close()

    return roles


@app.post("/userroles")
def create_user_role(userrole: UserRoleCreate):

    db: Session = SessionLocal()

    new_user_role = UserRole(
        user_id=userrole.user_id,
        role_id=userrole.role_id
    )

    db.add(new_user_role)
    db.commit()
    db.refresh(new_user_role)

    db.close()

    return new_user_role


@app.get("/userroles")
def get_user_roles():

    db: Session = SessionLocal()

    user_roles = db.query(UserRole).all()

    db.close()

    return user_roles