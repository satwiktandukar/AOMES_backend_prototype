from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///./blog.db', connect_args={"check_same_thread":False})

SessionLocal = sessionmaker(bind=engine,autocommit=False, autoflush=False)

Base = declarative_base()


