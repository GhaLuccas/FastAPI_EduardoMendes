from datetime import datetime, timedelta, timezone

from jwt import encode
from pwdlib import PasswordHash

# Initialize password hashing context
pwd_context = PasswordHash.recommended()

SECRET_KEY = 'segredo'  # chave que gera o token
ALGORITHM = 'HS256'
ACCESS_TOKEN_EXPIRE_MINUTES = 30


def get_password_hash(password: str) -> str:
    # Generate the hashed password and return it
    return pwd_context.hash(password)


def verify_password(clean_password: str, hashed_password: str) -> bool:
    # Verify if the clean password matches the hashed password
    return pwd_context.verify(clean_password, hashed_password)


def create_access_token(data: dict):
    to_encode = data.copy()

    # Set expiration time
    expire = datetime.now(timezone.utc) + timedelta(
        minutes=ACCESS_TOKEN_EXPIRE_MINUTES
    )
    to_encode.update({'exp': expire})

    encoded_jwt = encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt
