import streamlit as st
import mysql.connector
from datetime import date

# Conexão com o banco de dados MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="aluno",
    database="bd"
)
cursor = conn.cursor(dictionary=True)

st.title("📊 Gestão de Projetos")

# --- VISUALIZAÇÃO DE DADOS ---
st.header("Visualização de Projetos, Membros e Tarefas")

st.subheader("Projetos")
cursor.execute("SELECT * FROM projeto")
projetos = cursor.fetchall()
st.write(projetos)

st.subheader("Membros")
cursor.execute("SELECT * FROM membro")
membros = cursor.fetchall()
st.write(membros)

st.subheader("Tarefas")
cursor.execute("""
    SELECT tarefa.id_tarefa, projeto.nome AS projeto, membro.nome AS membro, tarefa.descricao,
           tarefa.data_inicio, tarefa.data_fim, tarefa.status
    FROM tarefa
    JOIN projeto ON tarefa.id_projeto = projeto.id_projeto
    JOIN membro ON tarefa.id_membro = membro.id_membro
""")
tarefas = cursor.fetchall()
st.write(tarefas)

# --- LISTAR MEMBROS DE UM PROJETO ---
st.header("🔍 Membros de um Projeto")
projeto_nomes = {p["nome"]: p["id_projeto"] for p in projetos}
projeto_selecionado = st.selectbox("Selecione o projeto", list(projeto_nomes.keys()))
id_proj = projeto_nomes[projeto_selecionado]

cursor.execute("""
    SELECT DISTINCT membro.nome, membro.email, membro.cargo
    FROM tarefa
    JOIN membro ON tarefa.id_membro = membro.id_membro
    WHERE tarefa.id_projeto = %s
""", (id_proj,))
membros_projeto = cursor.fetchall()
st.write(membros_projeto)

# --- CADASTRO DE NOVA TAREFA ---
st.header("📝 Cadastro de Nova Tarefa")

with st.form("form_tarefa"):
    projeto_nome = st.selectbox("Projeto", list(projeto_nomes.keys()))
    id_projeto = projeto_nomes[projeto_nome]

    membro_nomes = {m["nome"]: m["id_membro"] for m in membros}
    membro_nome = st.selectbox("Membro", list(membro_nomes.keys()))
    id_membro = membro_nomes[membro_nome]

    descricao = st.text_area("Descrição da Tarefa")
    data_inicio = st.date_input("Data de Início", date.today())
    data_fim = st.date_input("Data de Término", date.today())
    status = st.selectbox("Status", ['Em andamento', 'Concluída', 'Atrasada'])

    submitted = st.form_submit_button("Registrar Tarefa")

    if submitted:
        cursor.execute("""
            INSERT INTO tarefa (id_projeto, id_membro, descricao, data_inicio, data_fim, status)
            VALUES (%s, %s, %s, %s, %s, %s)
        """, (id_projeto, id_membro, descricao, data_inicio, data_fim, status))
        conn.commit()
        st.success("Tarefa registrada com sucesso!")

# --- CONSULTAS EXTRAS ---
st.header("📌 Consultas")

st.subheader("Tarefas de um Membro")
membro_nome_sel = st.selectbox("Selecione o membro", list(membro_nomes.keys()), key="membro_consulta")
id_membro_sel = membro_nomes[membro_nome_sel]

cursor.execute("""
    SELECT tarefa.descricao, projeto.nome AS projeto, tarefa.status
    FROM tarefa
    JOIN projeto ON tarefa.id_projeto = projeto.id_projeto
    WHERE tarefa.id_membro = %s
""", (id_membro_sel,))
tarefas_membro = cursor.fetchall()
st.write(tarefas_membro)

st.subheader("Tarefas Atrasadas")
cursor.execute("""
    SELECT tarefa.descricao, membro.nome AS membro, projeto.nome AS projeto, tarefa.data_fim
    FROM tarefa
    JOIN projeto ON tarefa.id_projeto = projeto.id_projeto
    JOIN membro ON tarefa.id_membro = membro.id_membro
    WHERE tarefa.status = 'Atrasada'
""")
atrasadas = cursor.fetchall()
st.write(atrasadas)

# --- Fechar conexão ---
cursor.close()
conn.close()
