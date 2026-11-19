# 🪜 Escalera de la confianza

🎬 Vídeo: https://www.youtube.com/watch?v=V-7fJ1SjlpQ

🎬 2.º video: https://www.youtube.com/watch?v=8GDrMRq15rc

[![Escalera de la confianza — tu agente solo dice listo después de probarlo](guia/assets/banner-es.jpg)](https://inematds.github.io/escada-confianca/guia/es/)

**🇧🇷 [Português](README.md) · 🇺🇸 [English](README.en.md) · 🇪🇸 [Español](README.es.md)**

Le pides algo a la IA, te dice listo y pierdes la tarde revisando. Una ingeniera de SpaceX despertó con 20 entregas listas de sus agentes. Con la **escalera de la confianza**, tu agente solo dice listo después de probarlo.

## Qué es

Cuando la IA dice “listo” sin haber probado, quien revisa eres tú, y eso se come la tarde. La **escalera de la confianza** es un método de tres peldaños para que tu agente de programación (Claude Code o Codex) solo entregue con prueba: usa lo que hizo como un usuario y muestra un recibo, pasa una evaluación con nota 10 de 10 y convierte cada error repetido en una regla que la computadora exige sola. Es para quien ya usa agentes de IA en el código y quiere revisar menos. El kit trae textos listos para pegar en tu proyecto y un ejemplo que corre solo con Python.

## 📖 Guía de uso

Guía completa (landing + paso a paso): **https://inematds.github.io/escada-confianca/guia/es/**

## El kit

- `kit/degrau1-prova/` — skill "probar antes de decir listo" + mapa de pantallas
- `kit/degrau2-nota/` — evaluación con nota y prompt del juez (otro modelo)
- `kit/degrau3-regra/` — el error se vuelve regla + registro de errores
- `kit/AGENTS-escada.md` — bloque para pegar en el CLAUDE.md / AGENTS.md
- `exemplo/escada.py` — los 3 peldaños en un ejemplo que corre solo con Python

```bash
python3 exemplo/escada.py cadastro_quebrado    # 0/3 peldaños
python3 exemplo/escada.py cadastro_corrigido   # 3/3: listo con prueba
python3 -m unittest discover -s tests -v
```

Requiere Python 3.9 o más nuevo, sin bibliotecas extra.

## Créditos

El método es de **Lauren Tan** (@poteto), ingeniera de software en SpaceXAI (equipo de Grok Bot), antes en Cursor.

- **Entrevista original** — workshop en vivo en Maven, "How Cursor Turned AI Agents Into Better Engineers" (12/08/2026): https://maven.com/p/e23d9c/how-cursor-turned-ai-agents-into-better-engineers
- **Copia del workshop en YouTube** (no oficial, publicada por terceros): https://www.youtube.com/watch?v=Cmoh-yR-usA
- **pstack**, su paquete de habilidades: https://github.com/cursor/plugins/tree/main/pstack
- Charla "All Code Is Slop (Except Mine)" (AI Engineer): https://www.youtube.com/watch?v=O_zcc6Xl12g
- Perfil: https://x.com/poteto

Detalles en [CREDITOS.md](CREDITOS.md) (en portugués). Licencia MIT. Hecho por [INEMA.CLUB](https://inema.club).
