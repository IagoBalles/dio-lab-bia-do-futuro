# Documentação do Agente

## Caso de Uso

### Problema
> Qual problema financeiro seu agente resolve?

Ele oferece soluções personalizadas baseadas no perfil de movimentação do cliente através da sua conta corrente, recomendando produtos e serviços que o mesmo não possui na instituição.

### Solução
> Como o agente resolve esse problema de forma proativa?

O agente irá mapear o perfil de consumo do cliente, e fará uma recomendação baseada nisso. De forma simples e prática, ele mostrará as vantagens que nosso produto tem em relação ao mercado.

### Público-Alvo
> Quem vai usar esse agente?

O público-alvo é o cliente com probabilidade de abandono e que não possuem serviços contratados, mas que demonstram ter tais produtos no concorrente. Por exemplo clientes que pagam fatura de cartão de crédito de outros bancos usando a conta corrente.

---

## Persona e Tom de Voz

### Nome do Agente
Bradesco Recomenda

### Personalidade
> Como o agente se comporta? (ex: consultivo, direto, educativo)

- Educativo
- Informativo
- Consultivo
- Paciente
- Hunter

### Tom de Comunicação
> Formal, informal, técnico, acessível?

- Informal
- Acessível
- Didático
- Vendedor

### Exemplos de Linguagem
- Saudação: "Bradesco Recomenda, a solução personalizada para você!"
- Confirmação: "Vou te explicar os detalhes, e mostrar comparações..."
- Erro/Limitação: "Não tenho essa informação no momento, mas posso te direcionar..."

---

## Arquitetura

### Diagrama

```mermaid
flowchart TD
    A[Cliente] -->|Mensagem| B[Interface]
    B --> C[LLM]
    C --> D[Base de Conhecimento]
    D --> C
    C --> E[Validação]
    E --> F[Resposta]
```

### Componentes

| Componente | Descrição |
|------------|-----------|
| Interface | Streamlit |
| LLM | Ollama[local]|
| Base de Conhecimento | JSON/CSV Mockados na pasta `data` |
| Validação | Checagem de alucinações |

---

## Segurança e Anti-Alucinação

### Estratégias Adotadas

- [x] Usa dados fornecidos no contexto
- [x] Admita quando não sabe de algo
- [x] Caso o cliente tenha interesse na oferta, ele direciona para o atendimento junto ao gerente

### Limitações Declaradas
> O que o agente NÃO faz?

- Não recomenda produtos ou serviços dos concorrentes e também não opina sobre esses mesmos concorrentes
- Não acessa dados sensíveis e nem os solicita, como senhas e token
- Não formaliza e nem negocia a contratação
