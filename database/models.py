# ORM
from sqlalchemy import Column, Integer, String, Float, ForeignKey, Numeric, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session

Base = declarative_base()

class Gestor(Base):
    __tablename__ = 'gestores'
    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    email_gestor = Column(String, nullable=False, unique=True)

class CentroDeCusto(Base):
    __tablename__ = 'centro_de_custo'
    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    valor_mensal_total = Column(Float, nullable=False)
    gestor_id = Column(Integer, ForeignKey('gestores.id'), nullable=False)

class Cobranca(Base):
    __tablename__ = 'cobranca'
    id = Column(Integer, primary_key=True)
    telefone = Column(String, nullable=False, unique=True)
    nome_funcionario = Column(String, nullable=False)
    valor_mensal =  Column(Numeric(5, 3), nullable=False)
    data_referencia = Column(String, nullable=False)
    centro_de_custo_id = Column(Integer, ForeignKey('centro_de_custo.id'), nullable=False)


def calcular_valor_total(session, centro_de_custo_id:int ) -> float:
    total = session.query(
        func.sum(Cobranca.valor_mensal)
    ).filter(
        Cobranca.centro_de_custo_id == centro_de_custo_id
    ).scalar()
    
    return total or 0.0