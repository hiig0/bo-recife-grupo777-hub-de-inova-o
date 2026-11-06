from pydantic import BaseModel, ConfigDict, EmailStr, field_validator
from typing import Optional

class UsuarioSchema(BaseModel):
    nome: str
    email: str
    senha: str
    ativo: Optional[bool]
    admin: Optional[bool]

    @field_validator("senha")
    @classmethod
    def validar_tamanho_da_senha(cls, senha: str) -> str:
        if len(senha.encode("utf-8")) > 72:
            raise ValueError("A senha deve ter no máximo 72 bytes.")
        return senha

class Config:
    from_attributes = True

class ProjetoSchema(BaseModel):
    usuario: int
    descricao: str
    categoria: Optional[str] = "SAUDE"

class Config:
    from_attributes = True

class LoginSchema(BaseModel):
    email:str
    senha:str

class Config:
    from_attributes = True
