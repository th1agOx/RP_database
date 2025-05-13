from sqlalchemy import Column, Integer, String, Float, ForeignKey, Numeric, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session, relationship

Base = declarative_base()

class Gestor(Base):
    __tablename__ = 'gestores'
    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    email_gestor = Column(String, nullable=False, unique=True)

    centro_de_custo = relationship('CentroDeCusto', back_populates='gestores')

class CentroDeCusto(Base):
    __tablename__ = 'centro_de_custo'
    id = Column(Integer, primary_key=True)
    numero_cc = Column(Integer, nullable=False)
    valor_mensal_total = Column(Float, nullable=False)

    gestor_id = Column(Integer, ForeignKey('gestores.id'), nullable=False)
    relation_gestor = relationship('Gestor', back_populates='centro_de_custo' )

    cobrancas = relationship('Cobranca', back_populates='centro_de_custo')

class Cobranca(Base):
    __tablename__ = 'cobranca'
    id = Column(Integer, primary_key=True)
    linha_ativa = Column(Integer, nullable=False, unique=True)
    nome_funcionario = Column(String, nullable=False)
    valor_de_consumo =  Column(Numeric(6, 2), nullable=False)
    
    centro_de_custo_id = Column(Integer, ForeignKey('centro_de_custo.id'), nullable=False)
    relation_centro_de_custo = relationship('Cobranca', back_populates='centro_de_custo' )

def getCobranca(session: Session):
    dados = []

    centros = session.query(CentroDeCusto).all()

    for centro in centros:
            linhas = [
                 {
                      "linha_telefonica": c.linha_ativa,
                      "nome_funcionario": c.nome_funcionario,
                      "valor": float(c.valor_de_consumo)
                 }
                 for c in centro.Cobranca
            ]
            dados.append({
                "centro_de_custo": centro.numero_cc,
                "linhas_telefonicas": linhas, 
            })

    return dados

def calcular_valor_total(session, centro_de_custo_id:int ) -> float:
    total = session.query(
        func.sum(Cobranca.valor_de_consumo)
    ).filter(
        Cobranca.centro_de_custo_id == centro_de_custo_id
    ).scalar()
    
    return float(total or 0.0)

def att_valor_mensal_total(session: Session, centro_de_custo_id: int):
    total = calcular_valor_total(session, centro_de_custo_id)
    centro = session.query(CentroDeCusto).get(centro_de_custo_id)

    if centro :
        centro.valor_mensal_total = total
        session.commit()

def att_todos_centros(session: Session):
    centros = session.query(CentroDeCusto).all()

    for centro in centros:
        att_valor_mensal_total(session, centros.id)