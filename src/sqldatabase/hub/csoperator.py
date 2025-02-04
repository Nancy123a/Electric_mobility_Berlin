from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from src.sqldatabase.database import engine, Base  # Adjust import path as needed

# Define the User table
class CSOperator(Base):
    __tablename__ = 'csoperator'  # Table name

    cs_operator_id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    number_reports_assigned = Column(Integer, nullable=False)
