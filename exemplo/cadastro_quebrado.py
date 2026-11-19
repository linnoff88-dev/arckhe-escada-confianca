"""Cadastro como o agente entregou da primeira vez: diz "pronto", mas aceita e-mail inválido e duplicado."""

USUARIOS: dict[str, str] = {}


def cadastrar(email: str, senha: str) -> dict:
    USUARIOS[email] = senha
    return {"ok": True, "email": email}
