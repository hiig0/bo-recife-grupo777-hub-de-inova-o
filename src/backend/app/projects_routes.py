from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .dependencies import pegar_sessao, verificar_token
from .schemas import ProjetoSchema
from .models import Projeto, Usuario



projects_router = APIRouter(prefix="/projetos", tags=["projetos"], dependencies=[Depends(verificar_token)])


@projects_router.get("/")
async def projetos():
    """
    Essa é a rota padrão de projetos.
    """
    return {
        "mensagem": "Você acessou a rota padrão de projetos.",
        "autenticado": False,
    }

@projects_router.post("/criar_projeto")
async def criar_projeto(projeto_schema: ProjetoSchema, session: Session = Depends(pegar_sessao)):
    novo_projeto = Projeto(
        usuario=projeto_schema.usuario,
        descricao=projeto_schema.descricao,
        categoria=projeto_schema.categoria
    )
    session.add(novo_projeto)
    session.commit()
    return{"mensagem": "Projeto criado com sucesso!"}

@projects_router.post("/projeto/cancelar/{id_projeto}")
async def cancelar_projeto(id_projeto: int, session: Session = Depends(pegar_sessao), usuario: Usuario = Depends(pegar_sessao)):
    projeto = session.query(Projeto).filter(Projeto.id==id_projeto).first()
    if not projeto:
        raise HTTPException(status_code=400,detail="Projeto não encontrado")
    if not usuario.admin and usuario.id != projeto.usuario:
        raise  HTTPException(status_code=401, detail="Você não tem autorização para fazer essa modificação")
    session.commit()
    return {
        "mensagem": f"Projeto número: {id_projeto} cancelado com sucesso!",
        "projeto": projeto
    }
    