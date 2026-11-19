# Avaliação com nota (degrau 2 da escada da confiança)

O degrau 1 faz o agente provar. O degrau 2 responde: **a prova é boa?** Uma avaliação (eval) roda a mesma
tarefa contra vários casos e dá uma nota. Com nota, dá para pedir ao agente que melhore sozinho até 10/10.

## Monte a sua em 4 passos

1. **Escolha uma tarefa que se repete** (cadastrar, importar planilha, responder ticket, corrigir bug de um tipo).
2. **Escreva 8 a 15 casos** com a resposta certa: normais, de borda e os que já deram errado.
   Exemplo pronto: a lista `CASOS` em `exemplo/escada.py` (10 casos de cadastro).
3. **Nota automática quando der** (1 ponto por caso certo). Quando a resposta é texto ou julgamento, use um
   **juiz**: outro agente, de **outro modelo**, com a rubrica de `juiz.md`. Modelo diferente evita que o agente
   dê razão a si mesmo.
4. **Repita até 10/10.** Peça em loop:

> Rode `<comando da avaliação>`. Enquanto a nota for menor que 10, leia os casos que falharam, corrija a causa
> (não o caso) e rode de novo. Pare em 10/10 ou depois de 5 voltas, e me mostre a nota de cada volta.

No Claude Code use um loop/agendamento; no Codex, peça as voltas na mesma tarefa. Guarde a nota de cada volta:
se ela não sobe em 3 voltas, o problema está no método ou nos casos, e é hora de você olhar.

## Avalie também a sua ferramenta de prova

A própria skill do degrau 1 pode ganhar nota: dê ao agente 10 bugs conhecidos e conte quantos ele reproduziu
com a skill. Foi assim que a engenheira que inspirou este kit melhorou a dela.

## Regras

- Nunca altere os casos para a nota subir. Caso errado se corrige com justificativa, num commit separado.
- Caso que falhou em produção entra na avaliação para sempre.
