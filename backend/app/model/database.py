from sqlalchemy.engine import create_engine


# engine = create_engine("sqlite:///database.db", echo=True)
engine = create_engine("postgresql://postgres:1234@localhost:5432", echo=True)
