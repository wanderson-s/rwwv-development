import enum
import sqlalchemy
from fastapi import FastAPI
from datetime import datetime, timedelta
from app.config.settings import settings
from app.model.database import Base


class EmploymentType(enum.Enum):
    manager = "manager"
    analyst = "analyst"
    director = "director"


# Documentation:
#   - Relationship: https://docs.sqlalchemy.org/en/14/orm/basic_relationships.html
#   - FastAPI SQLAlchemy: https://fastapi.tiangolo.com/tutorial/sql-databases/?h=sqlal#create-the-sqlalchemy-engine


# relationship with token, bu and budget
# Employee 1 - N Token
# Employee 1 - N BusinessUnit
# Employee 1 - 1 Budget
class Employee(Base):
    __tablename__ = "employees"
    # access
    id = sqlalchemy.Column(sqlalchemy.BigInteger, primary_key=True, autoincrement=True)
    email = sqlalchemy.Column(sqlalchemy.String(256), nullable=True, unique=True)
    password = sqlalchemy.Column(sqlalchemy.String(32), nullable=True)
    active = sqlalchemy.Column(sqlalchemy.Boolean, default=False)
    # personal
    cpf = sqlalchemy.Column(sqlalchemy.String(11), nullable=False)
    first_name = sqlalchemy.Column(sqlalchemy.String(50), nullable=False)
    last_name = sqlalchemy.Column(sqlalchemy.String(100), nullable=False)
    birth_date = sqlalchemy.Column(sqlalchemy.Date, nullable=True)
    position = sqlalchemy.Column(sqlalchemy.Enum(EmploymentType), nullable=False)
    # permission
    can_simulate_budget = sqlalchemy.Column(sqlalchemy.Boolean, default=False)
    can_submit_budget = sqlalchemy.Column(sqlalchemy.Boolean, default=False)
    can_approve_budget = sqlalchemy.Column(sqlalchemy.Boolean, default=False)
    can_read_budget = sqlalchemy.Column(sqlalchemy.Boolean, default=False)
    is_admin = sqlalchemy.Column(sqlalchemy.Boolean, default=False)
    # datetime
    created_at = sqlalchemy.Column(
        sqlalchemy.DateTime, default=datetime.now, nullable=False
    )
    updated_at = sqlalchemy.Column(
        sqlalchemy.DateTime,
        default=datetime.now,
        onupdate=datetime.now,
        nullable=False,
    )
    # relationship back_populates
    tokens = sqlalchemy.orm.relationship("Token", back_populates="user")
    bu = sqlalchemy.orm.relationship("BusinessUnit", back_populates="employee")


class Token(Base):  # relationship Employees <- 1 - N -> Tokens
    __tablename__ = "token"
    # default
    id = sqlalchemy.Column(sqlalchemy.BigInteger, primary_key=True, autoincrement=True)
    authorize = sqlalchemy.Column(sqlalchemy.Text, nullable=False)
    authoration = sqlalchemy.Column(sqlalchemy.Text, nullable=False)
    refresh = sqlalchemy.Column(sqlalchemy.Text, nullable=False)
    enable = sqlalchemy.Column(sqlalchemy.Boolean, nullable=False, default=False)
    expiration = sqlalchemy.Column(
        sqlalchemy.DateTime,
        default=lambda: (datetime + timedelta(hours=1)),
        nullable=False,
    )
    # datetime
    created_at = sqlalchemy.Column(
        sqlalchemy.DateTime, default=datetime.now, nullable=False
    )
    updated_at = sqlalchemy.Column(
        sqlalchemy.DateTime,
        default=datetime.now,
        onupdate=datetime.now,
        nullable=False,
    )
    # fks
    fk_id_employees = sqlalchemy.Column(
        sqlalchemy.BigInteger,
        sqlalchemy.ForeignKey("employees.id", ondelete="CASCADE"),
        nullable=False,
    )
    # relationship
    user = sqlalchemy.orm.relationship(
        "Employee", back_populates="tokens", uselist=False
    )


class BusinessUnit(Base):  # relationship Employees <- 1 - N -> BU
    __tablename__ = "business_unit"
    # defaults
    id = sqlalchemy.Column(sqlalchemy.BigInteger, primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String(300), nullable=False)
    description = sqlalchemy.Column(sqlalchemy.Text, nullable=False)
    # datetime
    created_at = sqlalchemy.Column(
        sqlalchemy.DateTime, default=datetime.now, nullable=False
    )
    updated_at = sqlalchemy.Column(
        sqlalchemy.DateTime,
        default=datetime.now,
        onupdate=datetime.now,
        nullable=False,
    )
    # fks
    fk_id_employee = sqlalchemy.Column(
        sqlalchemy.BigInteger,
        sqlalchemy.ForeignKey("employees.id", ondelete="CASCADE"),
        nullable=False,
    )
    # relationship
    employee = sqlalchemy.orm.relationship(
        "Employee", back_populates="bu", uselist=False
    )


def create_table():
    engine = sqlalchemy.create_engine(settings.database_uri, echo=True)
    Base.metadata.create_all(bind=engine)


def drop_table():
    engine = sqlalchemy.create_engine(settings.database_uri, echo=True)
    Base.metadata.drop_all(bind=engine, checkfirst=True)


def init_app(app: FastAPI):
    # drop_table()
    create_table()
