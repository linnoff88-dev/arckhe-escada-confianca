"""Os 3 degraus da escada da confiança, num exemplo que roda só com Python (sem instalar nada).

Uso:
  python3 exemplo/escada.py cadastro_quebrado     # o que o agente entregou primeiro
  python3 exemplo/escada.py cadastro_corrigido    # depois da escada

Degrau 1 (prova):  o "agente" usa o cadastro como um usuário e guarda o recibo (o que fez, o que viu).
Degrau 2 (nota):   uma avaliação roda os mesmos casos e dá nota de 0 a 10.
Degrau 3 (regra):  o erro que já apareceu uma vez vira regra que a máquina cobra (aqui: lê o código e
                   reprova `cadastrar` que não chama `validar_email`).
Sai com código 0 só se os 3 degraus passarem.
"""
import ast
import importlib
import inspect
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

# Casos da avaliação: (descrição, email, senha, deve_aceitar)
CASOS = [
    ("cadastro normal", "ana@exemplo.com", "senha-forte-1", True),
    ("e-mail sem arroba", "ana.exemplo.com", "senha-forte-1", False),
    ("e-mail vazio", "", "senha-forte-1", False),
    ("senha curta", "bia@exemplo.com", "123", False),
    ("e-mail repetido", "ana@exemplo.com", "outra-senha-9", False),
    ("maiúscula repetida", "ANA@exemplo.com", "outra-senha-9", False),
    ("segundo usuário", "caio@exemplo.org", "senha-forte-2", True),
    ("domínio sem ponto", "dani@exemplo", "senha-forte-3", False),
    ("espaço no e-mail", "e d@exemplo.com", "senha-forte-4", False),
    ("terceiro usuário", "eva@exemplo.net", "senha-forte-5", True),
]


def degrau1_prova(mod) -> dict:
    """Usa o app como usuário (cadastra e tenta repetir) e devolve o recibo."""
    mod.USUARIOS.clear()
    passos = []
    r1 = mod.cadastrar("teste@exemplo.com", "senha-forte-1")
    passos.append({"acao": "cadastrar teste@exemplo.com", "viu": r1})
    r2 = mod.cadastrar("teste@exemplo.com", "senha-forte-1")
    passos.append({"acao": "cadastrar o mesmo e-mail de novo", "viu": r2})
    r3 = mod.cadastrar("sem-arroba", "senha-forte-1")
    passos.append({"acao": "cadastrar e-mail inválido", "viu": r3})
    ok = r1.get("ok") is True and r2.get("ok") is False and r3.get("ok") is False
    return {"degrau": 1, "passou": ok, "recibo": passos}


def degrau2_nota(mod) -> dict:
    """Roda os 10 casos e dá nota de 0 a 10 (um ponto por caso certo)."""
    mod.USUARIOS.clear()
    erros = []
    for desc, email, senha, aceitar in CASOS:
        if bool(mod.cadastrar(email, senha).get("ok")) != aceitar:
            erros.append(desc)
    nota = len(CASOS) - len(erros)
    return {"degrau": 2, "passou": nota == 10, "nota": nota, "erros": erros}


def degrau3_regra(mod) -> dict:
    """Regra criada depois do 1º erro: `cadastrar` tem de chamar `validar_email`."""
    arvore = ast.parse(inspect.getsource(mod))
    func = next((n for n in arvore.body if isinstance(n, ast.FunctionDef) and n.name == "cadastrar"), None)
    chama = func is not None and any(
        isinstance(n, ast.Call) and getattr(n.func, "id", None) == "validar_email" for n in ast.walk(func))
    return {"degrau": 3, "passou": chama,
            "regra": "cadastrar() precisa chamar validar_email()" + ("" if chama else " — REPROVADO")}


def main(nome: str) -> int:
    mod = importlib.import_module(nome)
    res = [degrau1_prova(mod), degrau2_nota(mod), degrau3_regra(mod)]
    print(json.dumps({"modulo": nome, "degraus": res}, ensure_ascii=False, indent=2))
    tudo = all(r["passou"] for r in res)
    print(("PRONTO com prova" if tudo else "NÃO está pronto") + f" — {sum(r['passou'] for r in res)}/3 degraus")
    return 0 if tudo else 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1] if len(sys.argv) > 1 else "cadastro_corrigido"))
