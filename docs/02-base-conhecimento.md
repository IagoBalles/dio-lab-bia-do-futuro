# Base de Conhecimento

## Dados Utilizados

Descreva se usou os arquivos da pasta `data`, por exemplo:

| Arquivo | Formato | Utilização no Agente |
|---------|---------|---------------------|
| `historico_atendimento.csv` | CSV | Contextualizar interações anteriores, filtrando produtos que atendam suas necessidades |
| `perfil_cliente.json` | JSON | Personalizar recomendações e sanar duvidas de acordo com o perfil do cliente |
| `transacoes.csv` | CSV | Analisar comportamento e padrao de gastos, afim de mapear produtos e servicos que possam o atender ou que tenham em outros bancos |

> [!TIP]
> **Quer um dataset mais robusto?** Você pode utilizar datasets públicos do [Hugging Face](https://huggingface.co/datasets) relacionados a finanças, desde que sejam adequados ao contexto do desafio.

---

## Adaptações nos Dados

> Você modificou ou expandiu os dados mockados? Descreva aqui.

Foram adcionados alguns gastos extras como cartar de credito e financiamento de veiculo, e alterado o perfil do cliente, junto de seus objetivos

---

## Estratégia de Integração

### Como os dados são carregados?
> Descreva como seu agente acessa a base de conhecimento.

Existem duas possibilidades, injetar via codigo ou diretamente no prompt (CTRL + C, CTRL +V)

```python
import panda as pd
import json

#  CSVs
historico = pd.read_csv('data/historico_atendimento.csv')
transacoes = pd.read_csv('data/transacoes.csv')

#JSONs
with open ('data/perfil_cliente.json, 'r', enconding='utf-8) as f:
    perfil = json.load(f)

```

### Como os dados são usados no prompt?
> Os dados vão no system prompt? São consultados dinamicamente?

Para simplificar, podemos "injetar" os dados no prompt, mas o ideal é que as informacoes sejam carregadas dinamicamente.

```text
PERFIL DO CLIENTE (data/perfil_cliente.json):
{
  "nome": "Fernando Santos",
  "idade": 26,
  "profissao": "Supervisor",
  "renda_mensal": 5000.00,
  "uso_de_servicos_bancarios": "Moderado",
  "objetivo_principal": "Comprar imovel proprio",
  "patrimonio_total": 55000.00,
  "reserva_emergencia_atual": 10000.00,
  "metas": [
    {
      "meta": "Comprar imovel proprio",
      "valor_necessario": 350000.00,
      "prazo": "2028-06"
    },
    {
      "meta": "Entrada do apartamento",
      "valor_necessario": 100000.00,
      "prazo": "2027-12"
    }
  ]
}

PERFIL DE CONSUMO (data/transacoes.csv):
data,descricao,categoria,valor,tipo
2025-10-01,Salário,receita,5000.00,entrada
2025-10-02,Aluguel,moradia,1200.00,saida
2025-10-03,Supermercado,alimentacao,450.00,saida
2025-10-05,Netflix,lazer,55.90,saida
2025-10-07,Cartao de credito, geral, 1150.00, saida
2025-10-10,Restaurante,alimentacao,120.00,saida
2025-10-15,Conta de Luz,moradia,180.00,saida
2025-10-20,Academia,saude,99.00,saida
2025-10-25,Combustível,transporte,250.00,saida
2025-10-25,Parcela financiamento, transporte, 1310.00, saida

PERFIL DE ATENDIMENTO (data/historico_atendimento.csv):
data,canal,tema,resumo,resolvido
2025-09-15,chat,CDB,Cliente perguntou sobre rentabilidade e prazos,sim
2025-09-22,telefone,Problema no app,Erro ao visualizar extrato foi corrigido,sim
2025-10-01,chat,Consorcio imovel,Cliente pediu explicação sobre o funcionamento de lances,sim
2025-10-12,chat,Metas financeiras,Cliente pediu recomendacao de fundos de previdencia,sim
2025-10-25,email,Atualização cadastral,Cliente atualizou e-mail e telefone,sim

```

---

## Exemplo de Contexto Montado

> Mostre um exemplo de como os dados são formatados para o agente.

O exemplo abaixo, esta baseado nos dados anteriormente informados.

```
Dados do Cliente:
- Nome: Fernando Santos
- Utilizacao: Moderado
- Saldo disponível: R$ 5.000

Balanco de Gastos:
- Entradas: R$ 5.000
- Saidas: R$ 4.814

Recomendacoes:
- Previdencia mensal (afim de incetivar o cliente a poupar)
- Consorcio Auto (para reduzir as parcelas mensais do seu veiculo)
- Consorcio Imobiliario (pensando na aquisicao do imovel)
- Cartao de Credito (Mas vinculado a sua conta, com o objetivo de manter seus gastos num unico banco)

```
