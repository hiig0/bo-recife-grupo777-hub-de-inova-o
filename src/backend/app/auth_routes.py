from fastapi import APIRouter, Depends, HTTPException, status



from .database import get_db
from .models import Usuario
from .security import bcrypt_context
from .schemas import UsuarioSchema
from sqlalchemy.orm import Session
# from .schemas import LoginRequest, 


auth_router = APIRouter(prefix="/auth", tags=["auth"])


@auth_router.get("/")
async def home():
    """
    Essa é a rota padrão de autenticação.
    """
    return {
        "mensagem": "Você acessou a rota padrão de autenticação.",
        "autenticado": False,
    }


@auth_router.post("/criar_conta")
async def criar_conta(usuario_schema:UsuarioSchema, session = Depends(pegar_sessao)):
    usuario= session.query(Usuario).filter(Usuario.email==usuario_schema.email).first()
    if usuario:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Já existe um usuário com este e-mail.",
        )

    else:
        senha_criptografada = bcrypt_context.hash(usuario_schema.senha)
        novo_usuario = Usuario(usuario_schema.nome, usuario_schema.email, senha_criptografada, usuario_schema.admin)
        session.add(novo_usuario)
        session.commit()
        return{"mensagem":"Usuário cadastrado com sucesso"}


# @auth_router.post("/login")
# def login(usuario_login: LoginRequest, db: Session = Depends(get_db)):
#     usuario = db.query(Usuario).filter(Usuario.email == usuario_login.email).first()

#     if not usuario or usuario.senha != usuario_login.senha:
#         raise HTTPException(
#             status_code=status.HTTP_401_UNAUTHORIZED,
#             detail="E-mail ou senha inválidos.",
#         )

#     return {
#         "mensagem": "Login realizado com sucesso.",
#         "usuario": {
#             "id": usuario.id,
#             "nome": usuario.nome,
#             "email": usuario.email,
#             "ativo": usuario.ativo,
#         },
#     }


# @auth_router.get("/me")
# def obter_me(email: str, db: Session = Depends(get_db)):
#     usuario = db.query(Usuario).filter(Usuario.email == email).first()
#     if not usuario:
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND,
#             detail="Usuário não encontrado.",
#         )

#     return {
#         "id": usuario.id,
#         "nome": usuario.nome,
#         "email": usuario.email,
#         "ativo": usuario.ativo,
#         "admin": usuario.admin,
#     }
