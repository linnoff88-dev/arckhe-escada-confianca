---
name: provar-antes-de-pronto
description: Use antes de dizer que uma mudança está pronta. O agente roda o app como usuário, reproduz o bug antes da correção, confirma depois e entrega um recibo com o que fez e o que viu.
---

# Provar antes de dizer pronto (degrau 1 da escada da confiança)

Você só pode dizer "pronto" depois de usar o que mudou como um usuário usaria.

## Passos

1. **Ache a tela.** Leia `docs/mapa-de-telas.md`: onde fica a função, como chegar, que dado de teste usar.
   Se a tela não está no mapa, acrescente a linha depois de achar.
2. **Reproduza antes.** Com o app rodando (`<comando que sobe o app>`), faça o caminho do bug e registre o que viu
   (mensagem de erro, print, log, trace). Bug que você não reproduziu ainda não é bug entendido.
3. **Corrija.**
4. **Confira depois.** Repita exatamente o mesmo caminho. Teste também um caso vizinho (outro dado, outro botão).
   Para lentidão: meça antes e depois (trace de CPU, heap, tempo de resposta).
5. **Recibo.** Termine com:

```
RECIBO
- caminho testado: <tela → ação → ação>
- antes: <o que acontecia>
- depois: <o que acontece agora, com a evidência: saída/print/medida>
- caso vizinho: <qual e o resultado>
- não testei: <o que ficou de fora e por quê>
```

## Ferramentas para "olhos e mãos"

- App web: um navegador controlado por código (Playwright ou o navegador do seu agente) para clicar, digitar e
  tirar print.
- CLI/API: rodar o comando de verdade e colar a saída.
- Biblioteca: um script que chama a função como o usuário chamaria (como `exemplo/escada.py`).

Proibido: dizer "deve funcionar", "acredito que resolve" ou "pronto" sem o RECIBO.
