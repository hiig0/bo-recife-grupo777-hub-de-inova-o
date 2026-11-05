from pydantic import BaseModel, ConfigDict, EmailStr
from typing import Optional

class UsuarioSchema(BaseModel):
    nome: str
    email: str
    senha: str
    ativo: Optional[bool]
    admin: Optional[bool]

class Config:
    from_attributes = True

class ProjetoSchema(BaseModel):
    id_usuario = int
    descricao = str

class Config:
    from_attributes = True

#     model_config = ConfigDict(from_attributes=True)


# class LoginRequest(BaseModel):
#     email: EmailStr
#     senha: str
