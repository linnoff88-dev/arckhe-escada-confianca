# 🪜 Trust ladder

🎬 Vídeo: https://www.youtube.com/watch?v=V-7fJ1SjlpQ

🎬 2nd video: https://www.youtube.com/watch?v=8GDrMRq15rc

[![Trust ladder — your agent only says done after it proves it](guia/assets/banner-en.jpg)](https://inematds.github.io/escada-confianca/guia/en/)

**🇧🇷 [Português](README.md) · 🇺🇸 [English](README.en.md) · 🇪🇸 [Español](README.es.md)**

You ask the AI for something, it says done, and you lose the afternoon checking. A SpaceX engineer woke up to 20 finished deliveries from her agents. With the **trust ladder**, your agent only says done after it proves it.

## What it is

When the AI says “done” without testing, you are the one who checks, and that eats the afternoon. The **trust ladder** is a three-step method so your coding agent (Claude Code or Codex) only delivers with proof: it uses what it built the way a user would and shows a receipt, it passes an evaluation with a score of 10 out of 10, and it turns each repeated mistake into a rule the computer enforces on its own. It is for people who already use AI agents on code and want to check less. The kit has ready-to-paste texts for your project and an example that runs with plain Python.

## 📖 User guide

Full guide (landing + step by step): **https://inematds.github.io/escada-confianca/guia/en/**

## The kit

- `kit/degrau1-prova/` — "prove before saying done" skill + screen map
- `kit/degrau2-nota/` — evaluation with a score and the judge prompt (another model)
- `kit/degrau3-regra/` — the mistake becomes a rule + mistake log
- `kit/AGENTS-escada.md` — block to paste into CLAUDE.md / AGENTS.md
- `exemplo/escada.py` — the 3 steps in an example that runs with plain Python

```bash
python3 exemplo/escada.py cadastro_quebrado    # 0/3 degraus
python3 exemplo/escada.py cadastro_corrigido   # 3/3: PRONTO com prova
python3 -m unittest discover -s tests -v
```

Requires Python 3.9 or newer, no extra libraries.

## Credits

The method is by **Lauren Tan** (@poteto), software engineer at SpaceXAI (Grok Bot team), previously at Cursor.

- **Original interview** — live workshop on Maven, "How Cursor Turned AI Agents Into Better Engineers" (Aug 12, 2026): https://maven.com/p/e23d9c/how-cursor-turned-ai-agents-into-better-engineers
- **Copy of the workshop on YouTube** (unofficial, posted by a third party): https://www.youtube.com/watch?v=Cmoh-yR-usA
- **pstack**, her skills package: https://github.com/cursor/plugins/tree/main/pstack
- Talk "All Code Is Slop (Except Mine)" (AI Engineer): https://www.youtube.com/watch?v=O_zcc6Xl12g
- Profile: https://x.com/poteto

Details in [CREDITOS.md](CREDITOS.md) (in Portuguese). MIT license. Made by [INEMA.CLUB](https://inema.club).
