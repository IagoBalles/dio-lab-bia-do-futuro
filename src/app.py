import json
import pandas as pd
import requests
import streamlit as st
st.set_page_config(page_title="Bradesco Invest") # Isso ajuda o navegador a "acordar"

# ============= CONFIGURAÇÃO =============
def carregar_ia():
    return ChatOllama(model='tinyllama', base_url='http://localhost:11434')

# ============= CARREGAR DADOS =============
perfil = json.load(open('./data/perfil_cliente.json'))
transacoes = pd.read_csv('./data/transacoes.csv')
historico = pd.read_csv('./data/historico_atendimento.csv')

# ============= MONTAR CONTEXTO =============
contexto = f"""
CLIENTE: {perfil['nome']}, {perfil['idade']} anos,
OBJETIVO: {perfil['objetivo_principal']}
PATRIMÔNIO: R${perfil['patrimonio_total']} | RESERVA: R${perfil['reserva_emergencia_atual']}

TRANSACOES RECENTES:
{transacoes.to_string(index=False)}

ATENDIMENTOS ANTERIORES:
{historico.to_string(index=False)}
"""

# ============= SYSTEM PROMPT =============
SYSTEM_PROMPT = f"""Você é o Bradesco Recomenda,  um assistente pessoal voltado para trazer as melhores soluções baseadas no perfil de vida e consumo do cliente

OBJETIVO:
Avaliar perfil de movimentação e momento de vida, e identificar possíveis gargalos que impedem o cliente a conquistar seus objetivos, e recomendar soluções baseadas de acordo com a necessidade do cliente.

REGRAS:
1. É permitido comparações com produtos e serviços internos e externos, desde que não haja exposição de empresa concorrente
2. Use os dados obtidos nas movimentações do cliente e em sua base cadastral.
3. Linguagem simples e informal, para que seja fácil de ser compreendido.
4. Não passar informações que não tem certeza, e admitir caso não saiba a resposta.
5. Direcionar o cliente para um atendimento humano, quando o cliente sinalizar o interesse em fechar algum negócio.
6. Se limite a assuntos específicos do serviço bancário, quando houve outro tipo de interação será informado que não sabe sobre o assunto.
7. Resposta sucinta a direta.
"""

# ============= CHAMAR OLLAMA =============
def perguntar(msg):
    prompt = f"""
    {SYSTEM_PROMPT}

    CONTEXTO DO CLIENTE:
    {contexto}

    pergunta: {msg}"""

    r = requests.post(OLLAMA_URL, json={"model": MODELO, "prompt": prompt, "stream": False})
    return r.json()['response']

    # ============= INTERFACE =============
    st.title("Bradesco Recomenda")

    if pergunta := st.chat_input("Faça sua pergunta sobre finanças pessoais:"):
        st.chat_message("user").write(pergunta)
        with st.spinner("..."):
            st.chat_message("assistant").write(perguntar(pergunta))
