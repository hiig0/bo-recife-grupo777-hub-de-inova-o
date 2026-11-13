from fastapi import Depends, HTTPException
from .models import db, Usuario
from sqlalchemy.orm import sessionmaker, Session
from jose import jwt, JWTError
from jose.exceptions import ExpiredSignatureError
from .security import ALGORITHOM,  SECRET_KEY, oauth2_schema


def pegar_sessao():
    try:
        Session = sessionmaker(bind=db)
        session = Session()
        yield session
    finally:
        session.close()


def _verificar_token(token: str, tipo_esperado: str, session: Session):
    try:
        dic_info = jwt.decode(token, SECRET_KEY, ALGORITHOM)
        id_usuario = dic_info.get("sub")
        tipo_token = dic_info.get("type")
    except ExpiredSignatureError:
        if tipo_esperado == "refresh":
            raise HTTPException(
                status_code=401,
                detail="O refresh token expirou. Faça login novamente.",
                headers={"WWW-Authenticate": "Bearer"},
            )
        raise HTTPException(
            status_code=401,
            detail="O access token expirou. Solicite um novo token usando o refresh token.",
            headers={"WWW-Authenticate": "Bearer"},
        )
    except JWTError:
        raise HTTPException(
            status_code=401,
            detail="Token inválido.",
            headers={"WWW-Authenticate": "Bearer"},
        )
    if tipo_token != tipo_esperado:
        raise HTTPException(
            status_code=401,
            detail=f"Envie um token do tipo {tipo_esperado}.",
            headers={"WWW-Authenticate": "Bearer"},
        )
    usuario = session.query(Usuario).filter(Usuario.id == id_usuario).first()
    if not usuario:
        raise HTTPException(status_code=401, detail="Usuário do token não encontrado.")
    return usuario


def verificar_token(
    token: str = Depends(oauth2_schema),
    session: Session = Depends(pegar_sessao),
):
    return _verificar_token(token, "access", session)


def verificar_refresh_token(
    token: str = Depends(oauth2_schema),
    session: Session = Depends(pegar_sessao),
):
    return _verificar_token(token, "refresh", session)