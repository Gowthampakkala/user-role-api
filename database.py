from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "postgresql://fastapidb_6fzm_user:awOkXvbb76a1pPdNFSNKCBY9fTEf891a@dpg-dakhrtp42hec73akrrf0-a.virginia-postgres.render.com/fastapidb_6fzm"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()
