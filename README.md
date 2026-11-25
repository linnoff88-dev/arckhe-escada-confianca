# ê°Å¸ÂªÅ Escada da confianêÂ§a

<div align="center">
  <img src="capa/logo.svg" alt="Arckhé AI" height="48" />
  <p><strong>Arckhé AI</strong></p>
</div>


ê°Å¸Å½Â¬ VêÂ­deo: https://www.youtube.com/watch?v=V-7fJ1SjlpQ

ê°Å¸Å½Â¬ VêÂ­deo 2: https://www.youtube.com/watch?v=8GDrMRq15rc

[![Escada da confianêÂ§a ê¢â¬â seu agente sêÂ³ diz pronto depois de provar](guia/assets/banner.jpg)](https://linnoff88-dev.github.io/

**ê°Å¸â¡Â§ê°Å¸â¡Â· [PortuguêÂªs](README.md) êÂ· ê°Å¸â¡Âºê°Å¸â¡Â¸ [English](README.en.md) êÂ· ê°Å¸â¡Âªê°Å¸â¡Â¸ [EspaêÂ±ol](README.es.md)**

VocêÂª pede uma coisa para a IA, ela diz pronto, e vocêÂª perde a tarde conferindo. Uma engenheira da SpaceX acordou com 20 entregas prontas dos agentes dela. Com a **escada da confianêÂ§a**, o seu agente sêÂ³ diz pronto depois de provar.

## O que êÂ©

Quando a IA diz ê¢â¬Åprontoê¢â¬Â sem ter testado, quem confere êÂ© vocêÂª, e isso come a tarde. A **escada da confianêÂ§a** êÂ© um mêÂ©todo em trêÂªs degraus para o seu agente de programaêÂ§êÂ£o (Claude Code ou Codex) sêÂ³ entregar com prova: ele usa o que fez como um usuêÂ¡rio e mostra um recibo, passa numa avaliaêÂ§êÂ£o com nota 10 de 10 e transforma cada erro repetido numa regra que o computador cobra sozinho. êâ° para quem jêÂ¡ usa agentes de IA no cêÂ³digo e quer conferir menos. O kit traz textos prontos para colar no seu projeto e um exemplo que roda sêÂ³ com Python.

## ê°Å¸ââ Guia de uso

Guia completo (landing + passo a passo): **https://linnoff88-dev.github.io/

## O kit

- `kit/degrau1-prova/` ê¢â¬â skill "provar antes de dizer pronto" + mapa de telas
- `kit/degrau2-nota/` ê¢â¬â avaliaêÂ§êÂ£o com nota e prompt do juiz (outro modelo)
- `kit/degrau3-regra/` ê¢â¬â o erro vira regra + registro de erros
- `kit/AGENTS-escada.md` ê¢â¬â bloco para colar no CLAUDE.md / AGENTS.md
- `exemplo/escada.py` ê¢â¬â os 3 degraus num exemplo que roda sêÂ³ com Python

```bash
python3 exemplo/escada.py cadastro_quebrado    # 0/3 degraus
python3 exemplo/escada.py cadastro_corrigido   # 3/3: PRONTO com prova
python3 -m unittest discover -s tests -v
```

Requer Python 3.9 ou mais novo, sem bibliotecas extras.

## CrêÂ©ditos

O mêÂ©todo êÂ© da **Lauren Tan** (@poteto), engenheira de software na SpaceXAI (time do Grok Bot), antes no Cursor.

- **Entrevista original** ê¢â¬â workshop ao vivo na Maven, "How Cursor Turned AI Agents Into Better Engineers" (12/08/2026): https://maven.com/p/e23d9c/how-cursor-turned-ai-agents-into-better-engineers
- **CêÂ³pia do workshop no YouTube** (nêÂ£o oficial, postada por terceiros): https://www.youtube.com/watch?v=Cmoh-yR-usA
- **pstack**, o pacote de habilidades dela: https://github.com/cursor/plugins/tree/main/pstack
- Palestra "All Code Is Slop (Except Mine)" (AI Engineer): https://www.youtube.com/watch?v=O_zcc6Xl12g
- Perfil: https://x.com/poteto

Detalhes em [CREDITOS.md](CREDITOS.md). LicenêÂ§a MIT. Feito pelo [ARCKHê AI](https://ARCKHê AI).

---

<div align="center">
  <img src="capa/logo.svg" alt="Arckhé AI" height="32" />
  <p><strong>Arckhé AI</strong></p>
</div>