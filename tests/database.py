from fastapi.testclient import TestClient
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from app.main import app
from app.config import settings
from app.database import get_db, Base
from alembic import command


# SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
# SQLALCHEMY_DATABASE_URL = f'postgresql://postgres:Viethoaken321@localhost:5432/fastapi_test'
SQLALCHEMY_DATABASE_URL = f'postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}_test'

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine) # create all table

# Base = declarative_base()

# Dependency
def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


@pytest.fixture()
def session():
    Base.metadata.drop_all(bind=engine) # delete all table
    Base.metadata.create_all(bind=engine) # create all table
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

# client = TestClient(app)
# to keep database empty when you test many time
@pytest.fixture()
def client(session):

    # run your code before we run our test
    # Base.metadata.drop_all(bind=engine) # delete all table
    # Base.metadata.create_all(bind=engine) # create all table
    # command.upgrade("head")
    # yield TestClient(app) # yield = return
    # run your code after our test finishes
    # command.upgrade("base")
    def override_get_db():
        try:
            yield session
        finally:
            session.close()
    
    app.dependency_overrides[get_db] = override_get_db
    yield TestClient(app) # yield = return