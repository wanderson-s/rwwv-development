import enum
from datetime import datetime
from sqlalchemy import (
    Boolean,
    Column,
    Date,
    DateTime,
    Float,
    ForeignKeyConstraint,
    Integer,
    BigInteger,
    MetaData,
    String,
    Table,
    Text,
    create_engine,
    Enum,
)
from sqlalchemy.sql.sqltypes import Numeric

# from app.model.database import engine
engine = create_engine("sqlite:///database.db", echo=True)

metadata = MetaData()


class EmploymentType(enum.Enum):
    manager = "manager"
    analyst = "analyst"
    director = "director"


position = Table(
    "positions",
    metadata,
    Column("id", BigInteger, primary_key=True, autoincrement=True),
    Column("name", String(50), nullable=False),
    Column("employment_type", Enum(EmploymentType), default=EmploymentType.analyst, nullable=False),
    Column("created_at", DateTime, default=datetime.now, nullable=False),
    Column(
        "updated_at",
        DateTime,
        default=datetime.now,
        onupdate=datetime.now,
        nullable=False,
    ),
)

employee = Table(
    "employees",
    metadata,
    Column("id", BigInteger, primary_key=True, autoincrement=True),
    Column("first_name", String(50), nullable=False),
    Column("last_name", String(100), nullable=False),
    Column("email", String(256), nullable=False),
    Column("cpf", String(11), nullable=False),
    Column("birth_date", Date, nullable=True),
    Column("positions_id_fk", BigInteger, nullable=False),
    Column("created_at", DateTime, default=datetime.now, nullable=False),
    Column(
        "updated_at",
        DateTime,
        default=datetime.now,
        onupdate=datetime.now,
        nullable=False,
    ),
    ForeignKeyConstraint(
        columns=["positions_id_fk"], refcolumns=["positions.id"], name="fk_employees_positions_id"
    ),
)

system_user = Table(
    "system_users",
    metadata,
    Column("id", BigInteger, primary_key=True, autoincrement=True),
    Column("email", String(256), nullable=False),
    Column("password", String(36), nullable=False),
    Column("employees_id_fk", BigInteger, nullable=False),
    Column("created_at", DateTime, default=datetime.now, nullable=False),
    Column(
        "updated_at",
        DateTime,
        default=datetime.now,
        onupdate=datetime.now,
        nullable=False,
    ),
    ForeignKeyConstraint(
        columns=["employees_id_fk"],
        refcolumns=["employees.id"],
        name="fk_system_users_employees_id",
    ),
)

account_employee = Table(
    "accounts_employees",
    metadata,
    Column("id", BigInteger, primary_key=True, autoincrement=True),
    Column("accounts_id_fk", BigInteger, nullable=False),
    Column("employees_id_fk", BigInteger, nullable=False),
    Column("created_at", DateTime, default=datetime.now, nullable=False),
    Column(
        "updated_at",
        DateTime,
        default=datetime.now,
        onupdate=datetime.now,
        nullable=False,
    ),
    ForeignKeyConstraint(
        columns=["employees_id_fk"],
        refcolumns=["employees.id"],
        name="fk_account_employees_employees_id",
    ),
    ForeignKeyConstraint(
        columns=["accounts_id_fk"],
        refcolumns=["accounts.id"],
        name="fk_accounts_accounts_employees_id",
    ),
)


account = Table(
    "accounts",
    metadata,
    Column("id", BigInteger, primary_key=True, autoincrement=True),
    Column("name", String(300), nullable=False),
    Column("created_at", DateTime, default=datetime.now, nullable=False),
    Column(
        "updated_at",
        DateTime,
        default=datetime.now,
        onupdate=datetime.now,
        nullable=False,
    ),
)

budget_status = Table(
    "budget_status",
    metadata,
    Column("id", BigInteger, primary_key=True, autoincrement=True),
    Column("status", String(50), nullable=False),
    Column("accounts_employees_id_fk", BigInteger, nullable=False),
    Column("budget_id_fk", BigInteger, nullable=False),
    Column("created_at", DateTime, default=datetime.now, nullable=False),
    Column(
        "updated_at",
        DateTime,
        default=datetime.now,
        onupdate=datetime.now,
        nullable=False,
    ),
    ForeignKeyConstraint(
        columns=["accounts_employees_id_fk"],
        refcolumns=["accounts_employees.id"],
        name="fk_budget_status_account_employees_id",
    ),
    ForeignKeyConstraint(
        columns=["budget_id_fk"], refcolumns=["budget.id"], name="fk_budget_status_budget_id"
    ),
)

budget = Table(
    "budget",
    metadata,
    Column("id", BigInteger, primary_key=True, autoincrement=True),
    Column("january", Numeric(18, 2), nullable=False),
    Column("february", Numeric(18, 2), nullable=False),
    Column("march", Numeric(18, 2), nullable=False),
    Column("april", Numeric(18, 2), nullable=False),
    Column("may", Numeric(18, 2), nullable=False),
    Column("june", Numeric(18, 2), nullable=False),
    Column("july", Numeric(18, 2), nullable=False),
    Column("august", Numeric(18, 2), nullable=False),
    Column("september", Numeric(18, 2), nullable=False),
    Column("october", Numeric(18, 2), nullable=False),
    Column("november", Numeric(18, 2), nullable=False),
    Column("december", Numeric(18, 2), nullable=False),
    Column("type", String(30), nullable=False),
    Column("description", Text, nullable=False),
    Column("comment", Text, nullable=True),
    Column("created_at", DateTime, default=datetime.now, nullable=False),
    Column(
        "updated_at",
        DateTime,
        default=datetime.now,
        onupdate=datetime.now,
        nullable=False,
    ),
)

metadata.create_all(bind=engine)
