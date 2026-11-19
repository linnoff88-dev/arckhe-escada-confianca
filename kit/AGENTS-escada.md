# Bloco para colar no CLAUDE.md / AGENTS.md do seu projeto

> Escada da confiança: o agente só diz "pronto" depois de provar. Cole este bloco no arquivo de instruções
> que o seu agente lê (Claude Code: `CLAUDE.md`; Codex: `AGENTS.md`) e ajuste os comandos entre `< >`.

## Antes de dizer "pronto"

1. **Prove (degrau 1).** Rode o que você mudou do jeito que o usuário usa: `<comando que sobe o app>`.
   Use o mapa de telas (`docs/mapa-de-telas.md`) para chegar na tela certa. Reproduza o bug ANTES de corrigir
   e mostre que sumiu DEPOIS. Termine com um **recibo**: comandos rodados, o que você viu (saída, print, trace)
   e o que ficou de fora.
2. **Passe na nota (degrau 2).** Rode `<comando da avaliação>`. Entregue só com nota 10/10. Abaixo disso,
   corrija e rode de novo; não mude os casos da avaliação para passar.
3. **Respeite as regras (degrau 3).** `<lint> && <testes>` têm de passar. Se um revisor apontar um erro que já
   está em `docs/registro-de-erros.csv`, isso é falha do sistema: proponha a regra automática que impede o erro
   (lint, teste, tipo) em vez de só corrigir o caso.

Nunca escreva "pronto", "feito" ou "funcionando" sem o recibo do degrau 1 na mesma resposta.
