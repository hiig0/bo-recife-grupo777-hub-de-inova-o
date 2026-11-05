from sqlalchemy import create_engine, Column, String, Integer, Boolean, Float, ForeignKey
from sqlalchemy.orm import declarative_base
from sqlalchemy_utils import ChoiceType

#cria a conexão do seu banco
db = create_engine("sqlite:///banco.db")

#cria a base do banco
Base = declarative_base()

#cria as classes/tabelas do banco

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    nome = Column ("nome", String)
    email = Column ("email", String, nullable=False)
    senha = Column ("senha", String)
    ativo = Column ("ativo", Boolean)
    admin = Column ("admin", Boolean, default=False)

    def __init__(self, nome, email, senha, ativo=True, admin=False):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.ativo = ativo
        self.admin = admin

class Projeto(Base):
    __tablename__ = "projetos"

    # CATEGORIA_PROJETOS = (
    #     ("EDUCACAO", "EDUCACAO"),
    #     ("SAUDE", "SAUDE"),
    #     ("MOBILIDADE URBANA", "MOBILIDADE URBANA")
    # )

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    categoria = Column("categoria", String) #educaçao, saude, meio-ambiente, mobilidade urbana
    descricao = Column("descricao", String)
    usuario = Column ("usuario", ForeignKey("usuarios.id"))

    def __init__(self, usuario, descricao, categoria="SAUDE"):
        self.usuario = usuario
        self.descricao = descricao
        self.categoria = categoria
    