import enum
import sqlalchemy
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
    email = sqlalchemy.Column(sqlalchemy.String(256), nullable=True)
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
    created_at = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.now, nullable=False)
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
    created_at = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.now, nullable=False)
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
    user = sqlalchemy.orm.relationship("Employee", back_populates="tokens")


class BusinessUnit(Base):  # relationship Employees <- 1 - N -> BU
    __tablename__ = "business_unit"
    # defaults
    id = sqlalchemy.Column(sqlalchemy.BigInteger, primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String(300), nullable=False)
    description = sqlalchemy.Column(sqlalchemy.Text, nullable=False)
    # datetime
    created_at = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.now, nullable=False)
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
    employee = sqlalchemy.orm.relationship("Employee", back_populates="bu")


# CREATING ...
class Budget(Base):
    __tablename__ = "budget"
    # default
    id = sqlalchemy.Column(sqlalchemy.BigInteger, primary_key=True, autoincrement=True)
    january = sqlalchemy.Column(sqlalchemy.Numeric(18, 2), nullable=False)
    february = sqlalchemy.Column(sqlalchemy.Numeric(18, 2), nullable=False)
    march = sqlalchemy.Column(sqlalchemy.Numeric(18, 2), nullable=False)
    april = sqlalchemy.Column(sqlalchemy.Numeric(18, 2), nullable=False)
    may = sqlalchemy.Column(sqlalchemy.Numeric(18, 2), nullable=False)
    june = sqlalchemy.Column(sqlalchemy.Numeric(18, 2), nullable=False)
    july = sqlalchemy.Column(sqlalchemy.Numeric(18, 2), nullable=False)
    august = sqlalchemy.Column(sqlalchemy.Numeric(18, 2), nullable=False)
    september = sqlalchemy.Column(sqlalchemy.Numeric(18, 2), nullable=False)
    october = sqlalchemy.Column(sqlalchemy.Numeric(18, 2), nullable=False)
    november = sqlalchemy.Column(sqlalchemy.Numeric(18, 2), nullable=False)
    december = sqlalchemy.Column(sqlalchemy.Numeric(18, 2), nullable=False)
    total = sqlalchemy.Column(sqlalchemy.Numeric(18, 2), nullable=False)
    type = sqlalchemy.Column(sqlalchemy.String(50), nullable=False)
    description = sqlalchemy.Column(sqlalchemy.Text, nullable=False)
    comment = sqlalchemy.Column(sqlalchemy.Text, nullable=False)

    # datetime
    created_at = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.now, nullable=False)
    updated_at = sqlalchemy.Column(
        sqlalchemy.DateTime,
        default=datetime.now,
        onupdate=datetime.now,
        nullable=False,
    )
    # fks
    fk_id_bu = sqlalchemy.Column(
        sqlalchemy.BigInteger,
        sqlalchemy.ForeignKey("employees.id", ondelete="CASCADE"),
        nullable=False,
    )
    # fks
    fk_id_approver = sqlalchemy.Column(
        sqlalchemy.BigInteger,
        sqlalchemy.ForeignKey("employees.id", ondelete="CASCADE"),
        nullable=False,
    )
    # relationship


class StatusBudget(Base):
    __tablename__ = "status_budget"
    # default
    id = sqlalchemy.Column(sqlalchemy.Biginteger, primary_key=True, autoincrement=True)
    status = sqlalchemy.Column(sqlalchemy.String(50), nullable=False)
    approved = sqlalchemy.Column(sqlalchemy.Boolean, nullable=False)
    current = sqlalchemy.Column(sqlalchemy.Boolean, nullable=False)

    # datetime
    created_at = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.now, nullable=False)
    updated_at = sqlalchemy.Column(
        sqlalchemy.DateTime,
        default=datetime.now,
        onupdate=datetime.now,
        nullable=False,
    )
    # fks
    fk_id_budget = sqlalchemy.Column(
        sqlalchemy.BigInteger,
        sqlalchemy.ForeignKey("employees.id", ondelete="CASCADE"),
        nullable=False,
    )


"""
class Budget(Base):
    __tablename__ = "budget"
    id = (
        sqlalchemy.Column(sqlalchemy.BigInteger, primary_key=True, autoincrement=True),
    )
    fk_id_employees = (sqlalchemy.Column(sqlalchemy.BigInteger, nullable=False),)
    fk_id_business_unit = (sqlalchemy.Column(sqlalchemy.BigInteger, nullable=False),)
    sqlalchemy.Column(
        "created_at", sqlalchemy.DateTime, default=datetime.now, nullable=False
    )
    sqlalchemy.Column(
        "updated_at",
        sqlalchemy.DateTime,
        default=datetime.now,
        onupdate=datetime.now,
        nullable=False,
    )
    sqlalchemy.ForeignKeyConstraint(
        columns=["fk_id_employees"],
        refcolumns=["employees.id"],
        name="fk_budget_employees_id",
    )
    sqlalchemy.ForeignKeyConstraint(
        columns=["fk_id_business_unit"],
        refcolumns=["business_unit.id"],
        name="fk_budget_business_unit_id",
    )


BaseBudget = sqlalchemy.Table(
    "base_budget",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.BigInteger, primary_key=True, autoincrement=True),
    sqlalchemy.Column("january", sqlalchemy.Numeric(18, 2), nullable=False),
    sqlalchemy.Column("february", sqlalchemy.Numeric(18, 2), nullable=False),
    sqlalchemy.Column("march", sqlalchemy.Numeric(18, 2), nullable=False),
    sqlalchemy.Column("april", sqlalchemy.Numeric(18, 2), nullable=False),
    sqlalchemy.Column("may", sqlalchemy.Numeric(18, 2), nullable=False),
    sqlalchemy.Column("june", sqlalchemy.Numeric(18, 2), nullable=False),
    sqlalchemy.Column("july", sqlalchemy.Numeric(18, 2), nullable=False),
    sqlalchemy.Column("august", sqlalchemy.Numeric(18, 2), nullable=False),
    sqlalchemy.Column("september", sqlalchemy.Numeric(18, 2), nullable=False),
    sqlalchemy.Column("october", sqlalchemy.Numeric(18, 2), nullable=False),
    sqlalchemy.Column("november", sqlalchemy.Numeric(18, 2), nullable=False),
    sqlalchemy.Column("december", sqlalchemy.Numeric(18, 2), nullable=False),
    sqlalchemy.Column("total", sqlalchemy.Numeric(18, 2), nullable=False),
    sqlalchemy.Column("type", sqlalchemy.String(50), nullable=False),
    sqlalchemy.Column("description", sqlalchemy.Text, nullable=False),
    sqlalchemy.Column("comment", sqlalchemy.Text, nullable=False),
    sqlalchemy.Column("fk_id_budget", sqlalchemy.BigInteger, nullable=False),
    sqlalchemy.Column(
        "created_at", sqlalchemy.DateTime, default=datetime.now, nullable=False
    ),
    sqlalchemy.Column(
        "updated_at",
        sqlalchemy.DateTime,
        default=datetime.now,
        onupdate=datetime.now,
        nullable=False,
    ),
    sqlalchemy.ForeignKeyConstraint(
        columns=["fk_id_budget"],
        refcolumns=["budget.id"],
        name="fk_base_budget_budget_id",
    ),
)

Approver = sqlalchemy.Table(
    "approvers",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.BigInteger, primary_key=True, nullable=True),
    sqlalchemy.Column("fk_id_budget", sqlalchemy.BigInteger, nullable=False),
    sqlalchemy.Column("fk_id_employees", sqlalchemy.BigInteger, nullable=False),
    sqlalchemy.Column(
        "created_at", sqlalchemy.DateTime, default=datetime.now, nullable=False
    ),
    sqlalchemy.Column(
        "updated_at",
        sqlalchemy.DateTime,
        default=datetime.now,
        onupdate=datetime.now,
        nullable=False,
    ),
    sqlalchemy.ForeignKeyConstraint(
        columns=["fk_id_budget"], refcolumns=["budget.id"], name="fk_approvers_budget_id"
    ),
    sqlalchemy.ForeignKeyConstraint(
        columns=["fk_id_employees"],
        refcolumns=["employees.id"],
        name="fk_approvers_employees_id",
    ),
)

StatusBudget = sqlalchemy.Table(
    "status_budget",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.BigInteger, primary_key=True, autoincrement=True),
    sqlalchemy.Column("status", sqlalchemy.String(50), nullable=False),
    sqlalchemy.Column("approved", sqlalchemy.Boolean, nullable=False),
    sqlalchemy.Column("fk_id_budget", sqlalchemy.BigInteger, nullable=False),
    sqlalchemy.Column(
        "created_at", sqlalchemy.DateTime, default=datetime.now, nullable=False
    ),
    sqlalchemy.Column(
        "updated_at",
        sqlalchemy.DateTime,
        default=datetime.now,
        onupdate=datetime.now,
        nullable=False,
    ),
    sqlalchemy.ForeignKeyConstraint(
        columns=["fk_id_budget"],
        refcolumns=["budget.id"],
        name="fk_status_budget_budget_id",
    ),
)
"""


def create_table():
    engine = sqlalchemy.create_engine(settings.database_uri, echo=True)
    Base.metadata.create_all(bind=engine)


def drop_table():
    engine = sqlalchemy.create_engine(settings.database_uri, echo=True)
    Base.metadata.drop_all(bind=engine, checkfirst=True)
