import subprocess
import sys
import unittest
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(RAIZ / "exemplo"))
import escada  # noqa: E402


def rodar(nome):
    return subprocess.run([sys.executable, str(RAIZ / "exemplo/escada.py"), nome], capture_output=True, text=True)


class TestEscada(unittest.TestCase):
    def test_quebrado_reprova_os_tres(self):
        import cadastro_quebrado as m
        self.assertFalse(escada.degrau1_prova(m)["passou"])
        n = escada.degrau2_nota(m)
        self.assertFalse(n["passou"])
        self.assertLess(n["nota"], 10)
        self.assertFalse(escada.degrau3_regra(m)["passou"])
        self.assertEqual(rodar("cadastro_quebrado").returncode, 1)

    def test_corrigido_passa_com_nota_10(self):
        import cadastro_corrigido as m
        self.assertTrue(escada.degrau1_prova(m)["passou"])
        self.assertEqual(escada.degrau2_nota(m)["nota"], 10)
        self.assertTrue(escada.degrau3_regra(m)["passou"])
        r = rodar("cadastro_corrigido")
        self.assertEqual(r.returncode, 0)
        self.assertIn("PRONTO com prova", r.stdout)

    def test_kit_tem_os_tres_degraus(self):
        for p in ["kit/degrau1-prova/SKILL.md", "kit/degrau1-prova/mapa-de-telas.md",
                  "kit/degrau2-nota/avaliacao.md", "kit/degrau2-nota/juiz.md",
                  "kit/degrau3-regra/erros-viram-regra.md", "kit/degrau3-regra/registro-de-erros.csv",
                  "kit/AGENTS-escada.md", "CREDITOS.md"]:
            self.assertTrue((RAIZ / p).is_file(), p)


if __name__ == "__main__":
    unittest.main()
