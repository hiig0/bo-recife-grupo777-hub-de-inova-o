from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer
import os

bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_schema = OAuth2PasswordBearer(tokenUrl="auth/login-form")

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM", "HS256")
ALGORITHOM = ALGORITHM

_expire_minutes_raw = (
	os.getenv("ACESS_TOKEN_EXPIRE_MINUTES")
	or os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES")
	or "60"
)

try:
	ACESS_TOKEN_EXPIRE_MINUTES = int(_expire_minutes_raw)
except ValueError:
	ACESS_TOKEN_EXPIRE_MINUTES = 60