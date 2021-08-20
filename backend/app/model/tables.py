import enum
from datetime import datetime
import sqlalchemy

from app.model.database import engine

metadata = sqlalchemy.MetaData()


class EmploymentType(enum.Enum):
    manager = "manager"
    analyst = "analyst"
    director = "director"


position = sqlalchemy.Table(
    "positions",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.BigInteger, primary_key=True, autoincrement=True),
    sqlalchemy.Column("name", sqlalchemy.String(50), nullable=False),
    sqlalchemy.Column(
        "employment_type",
        sqlalchemy.Enum(EmploymentType),
        default=EmploymentType.analyst,
        nullable=False,
    ),
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
)

"""
    employee = sqlalchemy.Table(
        "employees",
        metadata,
        sqlalchemy.Column("id", sqlalchemy.BigInteger, primary_key=True, autoincrement=True),
        sqlalchemy.Column("first_name", sqlalchemy.String(50), nullable=False),
        sqlalchemy.Column("last_name", sqlalchemy.String(100), nullable=False),
        sqlalchemy.Column("email", sqlalchemy.String(256), nullable=False),
        sqlalchemy.Column("cpf", sqlalchemy.String(11), nullable=False),
        sqlalchemy.Column("birth_sqlalchemy.Date", sqlalchemy.Date, nullable=True),
        sqlalchemy.Column("positions_id_fk", sqlalchemy.BigInteger, nullable=False),
        sqlalchemy.Column("created_at", sqlalchemy.sqlalchemy.DateTime, default=sqlalchemy.sqlalchemy.DateTime.now, nullable=False),
        sqlalchemy.Column(
            "updated_at",
            sqlalchemy.DateTime,
            default=datetime.now,
            onupdate=datetime.now,
            nullable=False,
        ),
        sqlalchemy.ForeignKeyConstraint(
            columns=["positions_id_fk"], refcolumns=["positions.id"], name="fk_employees_positions_id"
        ),
    )

    system_user = sqlalchemy.Table(
        "system_users",
        metadata,
        sqlalchemy.Column("id", sqlalchemy.BigInteger, primary_key=True, autoincrement=True),
        sqlalchemy.Column("email", sqlalchemy.String(256), nullable=False),
        sqlalchemy.Column("password", sqlalchemy.String(36), nullable=False),
        sqlalchemy.Column("employees_id_fk", sqlalchemy.BigInteger, nullable=False),
        sqlalchemy.Column("created_at", sqlalchemy.sqlalchemy.DateTime, default=sqlalchemy.sqlalchemy.DateTime.now, nullable=False),
        sqlalchemy.Column(
            "upsqlalchemy.Dated_at",
            sqlalchemy.sqlalchemy.DateTime,
            default=sqlalchemy.sqlalchemy.DateTime.now,
            onupsqlalchemy.Date=sqlalchemy.sqlalchemy.DateTime.now,
            nullable=False,
        ),
        sqlalchemy.ForeignKeyConstraint(
            sqlalchemy.Columns=["employees_id_fk"],
            refsqlalchemy.Columns=["employees.id"],
            name="fk_system_users_employees_id",
        ),
    )

    account_employee = sqlalchemy.Table(
        "accounts_employees",
        metadata,
        sqlalchemy.Column("id", sqlalchemy.BigInteger, primary_key=True, autoincrement=True),
        sqlalchemy.Column("accounts_id_fk", sqlalchemy.BigInteger, nullable=False),
        sqlalchemy.Column("employees_id_fk", sqlalchemy.BigInteger, nullable=False),
        sqlalchemy.Column("created_at", sqlalchemy.sqlalchemy.DateTime, default=sqlalchemy.sqlalchemy.DateTime.now, nullable=False),
        sqlalchemy.Column(
            "upsqlalchemy.Dated_at",
            sqlalchemy.sqlalchemy.DateTime,
            default=sqlalchemy.sqlalchemy.DateTime.now,
            onupsqlalchemy.Date=sqlalchemy.sqlalchemy.DateTime.now,
            nullable=False,
        ),
        sqlalchemy.ForeignKeyConstraint(
            sqlalchemy.Columns=["employees_id_fk"],
            refsqlalchemy.Columns=["employees.id"],
            name="fk_account_employees_employees_id",
        ),
        sqlalchemy.ForeignKeyConstraint(
            sqlalchemy.Columns=["accounts_id_fk"],
            refsqlalchemy.Columns=["accounts.id"],
            name="fk_accounts_accounts_employees_id",
        ),
    )


    account = sqlalchemy.Table(
        "accounts",
        metadata,
        sqlalchemy.Column("id", sqlalchemy.BigInteger, primary_key=True, autoincrement=True),
        sqlalchemy.Column("name", sqlalchemy.String(300), nullable=False),
        sqlalchemy.Column("created_at", sqlalchemy.sqlalchemy.DateTime, default=sqlalchemy.sqlalchemy.DateTime.now, nullable=False),
        sqlalchemy.Column(
            "upsqlalchemy.Dated_at",
            sqlalchemy.sqlalchemy.DateTime,
            default=sqlalchemy.sqlalchemy.DateTime.now,
            onupsqlalchemy.Date=sqlalchemy.sqlalchemy.DateTime.now,
            nullable=False,
        ),
    )

    budget_status = sqlalchemy.Table(
        "budget_status",
        metadata,
        sqlalchemy.Column("id", sqlalchemy.BigInteger, primary_key=True, autoincrement=True),
        sqlalchemy.Column("status", sqlalchemy.String(50), nullable=False),
        sqlalchemy.Column("accounts_employees_id_fk", sqlalchemy.BigInteger, nullable=False),
        sqlalchemy.Column("budget_id_fk", sqlalchemy.BigInteger, nullable=False),
        sqlalchemy.Column("created_at", sqlalchemy.sqlalchemy.DateTime, default=sqlalchemy.sqlalchemy.DateTime.now, nullable=False),
        sqlalchemy.Column(
            "upsqlalchemy.Dated_at",
            sqlalchemy.sqlalchemy.DateTime,
            default=sqlalchemy.sqlalchemy.DateTime.now,
            onupsqlalchemy.Date=sqlalchemy.sqlalchemy.DateTime.now,
            nullable=False,
        ),
        sqlalchemy.ForeignKeyConstraint(
            sqlalchemy.Columns=["accounts_employees_id_fk"],
            refsqlalchemy.Columns=["accounts_employees.id"],
            name="fk_budget_status_account_employees_id",
        ),
        sqlalchemy.ForeignKeyConstraint(
            sqlalchemy.Columns=["budget_id_fk"], refsqlalchemy.Columns=["budget.id"], name="fk_budget_status_budget_id"
        ),
    )

    budget = sqlalchemy.Table(
    "budget",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.BigInteger, primary_key=True, autoincrement=True),
    sqlalchemy.Column("january", Numeric(18, 2), nullable=False),
    sqlalchemy.Column("february", Numeric(18, 2), nullable=False),
    sqlalchemy.Column("march", Numeric(18, 2), nullable=False),
    sqlalchemy.Column("april", Numeric(18, 2), nullable=False),
    sqlalchemy.Column("may", Numeric(18, 2), nullable=False),
    sqlalchemy.Column("june", Numeric(18, 2), nullable=False),
    sqlalchemy.Column("july", Numeric(18, 2), nullable=False),
    sqlalchemy.Column("august", Numeric(18, 2), nullable=False),
    sqlalchemy.Column("september", Numeric(18, 2), nullable=False),
    sqlalchemy.Column("october", Numeric(18, 2), nullable=False),
    sqlalchemy.Column("november", Numeric(18, 2), nullable=False),
    sqlalchemy.Column("december", Numeric(18, 2), nullable=False),
    sqlalchemy.Column("type", sqlalchemy.String(30), nullable=False),
    sqlalchemy.Column("description", Text, nullable=False),
    sqlalchemy.Column("comment", Text, nullable=True),
    sqlalchemy.Column("created_at", sqlalchemy.sqlalchemy.DateTime, default=sqlalchemy.sqlalchemy.DateTime.now, nullable=False),
    sqlalchemy.Column(
        "upsqlalchemy.Dated_at",
        sqlalchemy.sqlalchemy.DateTime,
        default=sqlalchemy.sqlalchemy.DateTime.now,
        onupsqlalchemy.Date=sqlalchemy.sqlalchemy.DateTime.now,
        nullable=False,
    ),
)
"""
# metadata.drop_all(bind=engine)
metadata.create_all(bind=engine)
