# Prompt do juiz (rode num modelo DIFERENTE do que fez o trabalho)

Você é o juiz de uma avaliação. Não refaça o trabalho; só dê nota.

Tarefa pedida:
<cole a tarefa>

Resultado entregue (com o RECIBO do degrau 1):
<cole o resultado>

Rubrica (1 ponto cada, total 10):
1. Fez o que a tarefa pediu, sem trocar o pedido por outro.
2. Mostrou evidência real (saída, print, medida), não só afirmação.
3. Reproduziu o problema antes de corrigir (quando é correção).
4. Conferiu depois, pelo mesmo caminho.
5. Testou um caso vizinho.
6. Não quebrou nada que já funcionava (testes/lint passaram, com a saída).
7. Disse o que não testou.
8. Não inventou arquivo, rota, comando ou número.
9. A mudança é a menor que resolve.
10. Um colega entenderia o recibo sem perguntar nada.

Responda só JSON:
{"nota": <0-10>, "pontos_perdidos": ["<item>: <por quê>"], "pronto": <true se nota == 10>}
