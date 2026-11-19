"""Cadastro depois da escada: o agente provou, ganhou nota 10/10 e o erro virou regra (validar_email obrigatório)."""
import re

USUARIOS: dict[str, str] = {}
_EMAIL = re.compile(r"^[^@\s]+@[^@\s]+\.[a-z]{2,}$", re.I)


def validar_email(email: str) -> bool:
    return bool(_EMAIL.match(email or ""))


def cadastrar(email: str, senha: str) -> dict:
    if not validar_email(email):
        return {"ok": False, "erro": "e-mail inválido"}
    if len(senha or "") < 8:
        return {"ok": False, "erro": "senha curta (mínimo 8)"}
    if email.lower() in USUARIOS:
        return {"ok": False, "erro": "e-mail já cadastrado"}
    USUARIOS[email.lower()] = senha
    return {"ok": True, "email": email.lower()}
