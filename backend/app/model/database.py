from databases import Database
from fastapi import FastAPI
from sqlalchemy import create_engine, MetaData as MD
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.config.settings import settings

Engine = create_engine(settings.database_uri)

Session = sessionmaker(autocommit=True, autoflush=True, bind=Engine)

MetaData = MD()

Base = declarative_base(bind=Engine, metadata=MetaData)
