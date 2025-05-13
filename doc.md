# SQLAIchemy 
biblioteca que conecta o codigo em python ao banco de dados 
Trabalhar com bancos relacionais usando Python puro.

Escrever menos SQL manual (via ORM) ou usar SQL direto (via Core).

Tornar seu código mais portável (SQLite, PostgreSQL, MySQL etc.).

- teste de interação banco e api 

# SQLITE X PYTHON
enquanto o sqlaichemy cria um escopo de teste, estrutura como o dado deve ser na tabela para melhor comunicação com a api o sqlite cria tabelas e columnas , as colunas ficam em linhas como a key de um objeto 
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  isso é uma coluna 

# LEMBRETE & LOGICAS
* se um gestor pode representar mais de um centro de custo, o centro de custo deverá receber um nome , para que o usuario saiba identificar exatamente onde ele deve cobrar alateração para redução, ou qualquer outra coisa essa possibilidade deve existir

# API
trata dos dados compeltos que saem do banco

- Documentação 

class Cobranca(Base):
    __tablename__ = 'cobranca'
    id = Column(Integer, primary_key=True)
    linha_telefonica = Column(Integer, nullable=False, unique=True)
    nome_funcionario = Column(String, nullable=False)
    valor =  Column(Numeric(6, 2), nullable=False)
    
    centro_de_custo_id = Column(Integer, ForeignKey('centro_de_custo.id'), nullable=False)
    relation_centro_de_custo = relationship('CentroDeCusto', back_populates='Cobranca' )


coluna valor : referênte ao valor Total da fatura a pagar 
  * fatura possui, planos, status de uso de linhas telefonicas 