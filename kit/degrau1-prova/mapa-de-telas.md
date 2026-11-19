# Mapa de telas (feature map)

O agente usa este mapa para chegar sozinho em qualquer função do app, até a partir de um print vago de um
usuário ("o botão azul não salva"). Uma linha por função. Peça ao agente para completar o mapa explorando o
código e o app; depois revise você.

| Função | Onde fica (tela/rota/comando) | Como chegar | Dado de teste | Como saber que funcionou |
|---|---|---|---|---|
| Cadastro | `/cadastro` | Início → "Criar conta" | `teste+<n>@exemplo.com` / `senha-forte-1` | Mensagem "Conta criada" e usuário na lista de admin |
| Login | `/entrar` | Início → "Entrar" | o usuário do cadastro | Nome no canto superior direito |
| Exportar relatório | `/relatorios` | Menu → Relatórios → "Exportar" | período do mês passado | Download de `.csv` com cabeçalho |
| <função> | <onde> | <caminho> | <dado> | <evidência> |

## Como pedir ao agente

> Explore o código e o app e complete `docs/mapa-de-telas.md`: uma linha por função que um usuário consegue
> usar. Para cada uma, abra a tela de verdade e confirme o caminho e a evidência. Não invente rota.

## Quando um relato chega

> Este é o relato do usuário: <texto ou print>. Use `docs/mapa-de-telas.md` para achar a função, reproduza o
> problema e me devolva: reproduzi (sim/não), passos, evidência. Se já estiver corrigido no main, diga isso.
