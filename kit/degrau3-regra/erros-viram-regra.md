# O erro vira regra (degrau 3 da escada da confiança)

O agente pode errar uma vez. Do mesmo jeito, nunca mais.

**O sinal:** você vai escrever, pela segunda vez, o mesmo comentário de revisão ("valida o e-mail", "não usa
`any`", "não chama a API dentro do loop"). Pare. Repetir no próximo pedido não escala com 1 agente, muito
menos com 10. Transforme o comentário numa regra que a máquina cobra.

## Suba o erro o mais alto que der nesta escada de regras

| Altura | O que é | Exemplo (cadastro sem validar e-mail) |
|---|---|---|
| 1 (melhor) | **O erro nem consegue existir** | um tipo `Email` que só se cria validado; `cadastrar(email: Email)` |
| 2 | **A máquina barra** (lint, tipo, teste, CI) | regra que reprova `cadastrar` sem `validar_email` (veja `degrau3_regra` em `exemplo/escada.py`) |
| 3 | **Instrução para o agente** (skill, CLAUDE.md/AGENTS.md) | "todo cadastro valida o e-mail antes de gravar" |
| 4 (pior) | **Guia de estilo / comentário de revisão** | o mesmo comentário em cada PR |

Instrução (altura 3) o agente pode esquecer. Teste e lint (altura 2) ele não consegue pular.

## Rotina de 5 minutos

1. Anote o erro em `registro-de-erros.csv` (data, o que aconteceu, onde, altura escolhida, regra criada).
2. Peça ao agente:

> Este erro já apareceu: <erro>. Não corrija só este caso. Proponha a regra mais alta possível (tipo, lint,
> teste ou CI) que impeça o erro de voltar, escreva a regra com um teste que falha no código antigo e passa no
> novo, e rode tudo.

3. De manhã (ou no fim do dia), leia o que os agentes entregaram. O que ficou ruim: reverta e volte ao passo 1.
