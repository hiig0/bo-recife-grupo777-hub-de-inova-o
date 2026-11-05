from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .dependencies import pegar_sessao
from schemas import ProjetoSchema
from .models import Projeto



projects_router = APIRouter(prefix="/projetos", tags=["projetos"])


@projects_router.get("/")
async def projetos():
    """
    Essa é a rota padrão de projetos.
    """
    return {
        "mensagem": "Você acessou a rota padrão de projetos.",
        "autenticado": False,
    }

@projects_router.post("/projeto")
async def criar_pedido(projeto_schema: ProjetoSchema, session: Session = Depends(pegar_sessao)):
    novo_projeto = Projeto(usuario=ProjetoSchema.id_usuario, projeto_schema.descricao)
    session.add(novo_projeto)
    session.commit()
    return{"mensagem": "Projeto criado com sucesso!"}