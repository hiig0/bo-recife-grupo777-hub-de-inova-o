from fastapi import APIRouter, Depends, HTTPException, status
from .dependencies import pegar_sessao
from .models import Usuario
from .security import bcrypt_context, ALGORITHOM, ACESS_TOKEN_EXPIRE_MINUTES, SECRET_KEY
from .schemas import UsuarioSchema, LoginSchema
from sqlalchemy.orm import Session
from jose import jwt, JWTError
from datetime import datetime, timedelta, timezone



auth_router = APIRouter(prefix="/auth", tags=["auth"])


def criar_token(id_usuario):
    data_expiracao = datetime.now(timezone.utc) + timedelta(minutes=ACESS_TOKEN_EXPIRE_MINUTES)
    dic_info = {"user_id": id_usuario, "exp": data_expiracao }
    jwt_codificado = jwt.encode(dic_info, SECRET_KEY, ALGORITHOM)
    return jwt_codificado



def autenticar_usuario(email, senha, session):
    usuario = session.query(Usuario).filter(Usuario.email==email).first()
    if not usuario:
        return False
    elif  not bcrypt_context.verify(senha, usuario.senha):
        return False

    return usuario


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
        novo_usuario = Usuario(usuario_schema.nome,usuario_schema.email,senha_criptografada,admin=usuario_schema.admin,)
        session.add(novo_usuario)
        session.commit()
        return{"mensagem":"Usuário cadastrado com sucesso"}

@auth_router.post("/login")
async def login(login_schema:LoginSchema, session: Session = Depends(pegar_sessao)):
    usuario = session.query(Usuario).filter(Usuario.email==login_schema.email).first()
    usuario = autenticar_usuario(login_schema.email, login_schema.senha, session)
    if not usuario:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Nenhum usuário encontrado ou credenciais inválidas .",)
    else:
        acess_token = criar_token(usuario.id)
        return {
            "acess_token": acess_token,
            "token_type": "Bearer"
        }
        







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
