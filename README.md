# ðŸªœ Escada da confianÃ§a

<div align="center">
  <img src="capa/logo.svg" alt="Arckhé AI" height="48" />
  <p><strong>Arckhé AI</strong></p>
</div>


ðŸŽ¬ VÃ­deo: https://www.youtube.com/watch?v=V-7fJ1SjlpQ

ðŸŽ¬ VÃ­deo 2: https://www.youtube.com/watch?v=8GDrMRq15rc

[![Escada da confianÃ§a â€” seu agente sÃ³ diz pronto depois de provar](guia/assets/banner.jpg)](https://linnoff88-dev.github.io/

**ðŸ‡§ðŸ‡· [PortuguÃªs](README.md) Â· ðŸ‡ºðŸ‡¸ [English](README.en.md) Â· ðŸ‡ªðŸ‡¸ [EspaÃ±ol](README.es.md)**

VocÃª pede uma coisa para a IA, ela diz pronto, e vocÃª perde a tarde conferindo. Uma engenheira da SpaceX acordou com 20 entregas prontas dos agentes dela. Com a **escada da confianÃ§a**, o seu agente sÃ³ diz pronto depois de provar.

## O que Ã©

Quando a IA diz â€œprontoâ€ sem ter testado, quem confere Ã© vocÃª, e isso come a tarde. A **escada da confianÃ§a** Ã© um mÃ©todo em trÃªs degraus para o seu agente de programaÃ§Ã£o (Claude Code ou Codex) sÃ³ entregar com prova: ele usa o que fez como um usuÃ¡rio e mostra um recibo, passa numa avaliaÃ§Ã£o com nota 10 de 10 e transforma cada erro repetido numa regra que o computador cobra sozinho. Ã‰ para quem jÃ¡ usa agentes de IA no cÃ³digo e quer conferir menos. O kit traz textos prontos para colar no seu projeto e um exemplo que roda sÃ³ com Python.

## ðŸ“– Guia de uso

Guia completo (landing + passo a passo): **https://linnoff88-dev.github.io/

## O kit

- `kit/degrau1-prova/` â€” skill "provar antes de dizer pronto" + mapa de telas
- `kit/degrau2-nota/` â€” avaliaÃ§Ã£o com nota e prompt do juiz (outro modelo)
- `kit/degrau3-regra/` â€” o erro vira regra + registro de erros
- `kit/AGENTS-escada.md` â€” bloco para colar no CLAUDE.md / AGENTS.md
- `exemplo/escada.py` â€” os 3 degraus num exemplo que roda sÃ³ com Python

```bash
python3 exemplo/escada.py cadastro_quebrado    # 0/3 degraus
python3 exemplo/escada.py cadastro_corrigido   # 3/3: PRONTO com prova
python3 -m unittest discover -s tests -v
```

Requer Python 3.9 ou mais novo, sem bibliotecas extras.

## CrÃ©ditos

O mÃ©todo Ã© da **Lauren Tan** (@poteto), engenheira de software na SpaceXAI (time do Grok Bot), antes no Cursor.

- **Entrevista original** â€” workshop ao vivo na Maven, "How Cursor Turned AI Agents Into Better Engineers" (12/08/2026): https://maven.com/p/e23d9c/how-cursor-turned-ai-agents-into-better-engineers
- **CÃ³pia do workshop no YouTube** (nÃ£o oficial, postada por terceiros): https://www.youtube.com/watch?v=Cmoh-yR-usA
- **pstack**, o pacote de habilidades dela: https://github.com/cursor/plugins/tree/main/pstack
- Palestra "All Code Is Slop (Except Mine)" (AI Engineer): https://www.youtube.com/watch?v=O_zcc6Xl12g
- Perfil: https://x.com/poteto

Detalhes em [CREDITOS.md](CREDITOS.md). LicenÃ§a MIT. Feito pelo [ARCKHÉ AI](https://ARCKHÉ AI).

---

<div align="center">
  <img src="capa/logo.svg" alt="Arckhé AI" height="32" />
  <p><strong>Arckhé AI</strong></p>
</div>