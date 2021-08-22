import enum
from datetime import datetime
import sqlalchemy

from app.model.database import engine

metadata = sqlalchemy.MetaData()


class EmploymentType(enum.Enum):
    manager = "manager"
    analyst = "analyst"
    director = "director"


Employee = sqlalchemy.Table(
    "employees",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.BigInteger, primary_key=True, autoincrement=True),
    sqlalchemy.Column("first_name", sqlalchemy.String(50), nullable=False),
    sqlalchemy.Column("last_name", sqlalchemy.String(100), nullable=False),
    sqlalchemy.Column("cpf", sqlalchemy.String(256), nullable=False),
    sqlalchemy.Column("position", sqlalchemy.String(50), nullable=False),
    sqlalchemy.Column("birth_date", sqlalchemy.Date, nullable=False),
    sqlalchemy.Column("fk_id_permission", sqlalchemy.BigInteger, nullable=Flase),
    sqlalchemy.Column("created_at", sqlalchemy.DateTime, default=datetime.now, nullable=False),
    sqlalchemy.Column(
        "updated_at",
        sqlalchemy.DateTime,
        default=datetime.now,
        onupdate=datetime.now,
        nullable=False,
    ),
    sqlalchemy.ForeingKeyConstraint(
        columns=["fk_id_permission"],
        refcolumns=["permission.id"],
        name="fk_employees_permission_id",
    ),
)

System_user = sqlalchemy.Table(
    "system_users",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.BigInteger, primary_key=True, autoincrement=True),
    sqlalchemy.Column("email", sqlalchemy.String(256), nullable=False),
    sqlalchemy.Column("password", sqlalchemy.String(36), nullable=False),
    sqlalchemy.Column("fk_id_employees", sqlalchemy.BigInteger, nullable=False),
    sqlalchemy.Column("fk_id_token", sqlalchemy.BigInteger, nullable=False),
    sqlalchemy.Column("created_at", sqlalchemy.DateTime, default=datetime.now, nullable=False),
    sqlalchemy.Column(
        "updated_at",
        sqlalchemy.DateTime,
        default=datetime.now,
        onupdate=datetime.now,
        nullable=False,
    ),
    sqlalchemy.ForeingKeyConstraint(
        columns=["fk_id_employees"],
        refcolumns=["employees.id"],
        name="fk_system_users_employees_id",
    ),
    sqlalchemy.ForeingKeyConstraint(
        columns=["fk_id_token"], refcolumns=["token.id"], name="fk_system_users_token_id"
    ),
)

Token = sqlalchemy.Table(
    "token",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.BigInteger, primary_key=True, autoincrement=True),
    sqlalchemy.Column("authorize", sqlalchemy.Text, nullable=False),
    sqlalchemy.Column("authoration", sqlalchemy.Text, nullable=False),
    sqlalchemy.Column("refresh", sqlalchemy.Text, nullable=False),
    sqlalchemy.Column("created_at", sqlalchemy.DateTime, default=datetime.now, nullable=False),
    sqlalchemy.Column(
        "updated_at",
        sqlalchemy.DateTime,
        default=datetime.now,
        onupdate=datetime.now,
        nullable=False,
    ),
)

Permission = sqlalchemy.Table(
    "permission",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.BigInteger, primary_key=True, autoincrement=True),
    sqlalchemy.Column("can_simulate_budget", sqlalchemy.Boolean, nullable=False),
    sqlalchemy.Column("can_submit_budget", sqlalchemy.Boolean, nullable=False),
    sqlalchemy.Column("can_approve_budget", sqlalchemy.Boolean, nullable=False),
    sqlalchemy.Column("can_read_budget", sqlalchemy.Boolean, nullable=False),
    sqlalchemy.Column("is_admin", sqlalchemy.Boolean, nullable=False),
    sqlalchemy.Column("created_at", sqlalchemy.DateTime, default=datetime.now, nullable=False),
    sqlalchemy.Column(
        "updated_at",
        sqlalchemy.DateTime,
        default=datetime.now,
        onupdate=datetime.now,
        nullable=False,
    ),
)

Business_unit = sqlalchemy.Table(
    "business_unit",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.BigInteger, primary_key=True, autoincrement=True),
    sqlalchemy.Column("name", sqlalchemy.String(300), nullable=False),
    sqlalchemy.Column("description", sqlalchemy.Text, nullable=False),
    sqlalchemy.Column("fk_id_employees", sqlalchemy.BigInteger, nullable=False),
    sqlalchemy.Column("created_at", sqlalchemy.DateTime, default=datetime.now, nullable=False),
    sqlalchemy.Column(
        "updated_at",
        sqlalchemy.DateTime,
        default=datetime.now,
        onupdate=datetime.now,
        nullable=False,
    ),
    sqlalchemy.ForeingKeyConstraint(
        columns=["fk_id_employees"],
        refcolumns=["employees.id"],
        name="fk_business_unit_employees_id",
    ),
)

Budget = sqlalchemy.Table(
    "budget",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.BigInteger, primary_key=True, autoincrement=True),
    sqlalchemy.Column("fk_id_employees", sqlalchemy.BigInteger, nullable=False),
    sqlalchemy.Column("fk_id_business_unit", sqlalchemy.BigInteger, nullable=False),
    sqlalchemy.Column("created_at", sqlalchemy.DateTime, default=datetime.now, nullable=False),
    sqlalchemy.Column(
        "updated_at",
        sqlalchemy.DateTime,
        default=datetime.now,
        onupdate=datetime.now,
        nullable=False,
    ),
    sqlalchemy.ForeingKeyConstraint(
        columns=["fk_id_employees"], refcolumns=["employees.id"], name="fk_budget_employees_id"
    ),
    sqlalchemy.ForeingKeyConstraint(
        columns=["fk_id_business_unit"],
        refcolumns=["business_unit.id"],
        name="fk_budget_business_unit_id",
    ),
)

Base_budget = sqlalchemy.Table(
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
    sqlalchemy.Column("created_at", sqlalchemy.DateTime, default=datetime.now, nullable=False),
    sqlalchemy.Column(
        "updated_at",
        sqlalchemy.DateTime,
        default=datetime.now,
        onupdate=datetime.now,
        nullable=False,
    ),
    sqlalchemy.ForeingKeyconstraint(
        columns=["fk_id_budget"], refcolumns=["budget.id"], name="fk_base_budget_budget_id"
    ),
)

Approver = sqlalchemy.Table(
    "approvers",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.BigInteger, primary_key=True, nullable=True),
    sqlalchemy.Column("fk_id_budget", sqlalchemy.BigInteger, nullable=False),
    sqlalchemy.Column("fk_id_employees", sqlalchemy.BigInteger, nullable=False),
    sqlalchemy.Column("created_at", sqlalchemy.DateTime, default=datetime.now, nullable=False),
    sqlalchemy.Column(
        "updated_at",
        sqlalchemy.DateTime,
        default=datetime.now,
        onupdate=datetime.now,
        nullable=False,
    ),
    sqlalchemy.ForeingKeyconstraint(
        columns=["fk_id_budget"], refcolumns=["budget.id"], name="fk_approvers_budget_id"
    ),
    sqlalchemy.ForeingKeyconstraint(
        columns=["fk_id_employess"], refcolumns=["employees.id"], name="fk_approvers_employees_id"
    ),
)

Status_budget = sqlalchemy.Table(
    "status_budget",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.BigInteger, primary_key=True, autoincrement=True),
    sqlalchemy.Column("status", sqlalchemy.String(50), nullable=False),
    sqlalchemy.Column("approved", sqlalchemy.boolean, nullable=False),
    sqlalchemy.Column("fk_id_budget", sqlalchemy.BigInteger, nullable=False),
    sqlalchemy.Column("created_at", sqlalchemy.DateTime, default=datetime.now, nullable=False),
    sqlalchemy.Column(
        "updated_at",
        sqlalchemy.DateTime,
        default=datetime.now,
        onupdate=datetime.now,
        nullable=False,
    ),
    sqlalchemy.ForeingKeyconstraint(
        columns=["fk_id_budget"], refcolumns=["budget.id"], name="fk_status_budget_budget_id"
    ),
)
# metadata.drop_all(bind=engine)
metadata.create_all(bind=engine)
