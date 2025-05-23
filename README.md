🛠️ Sistema de Gestão de Projetos - Equipe de Desenvolvimento de Software
Este projeto é uma aplicação web simples desenvolvida com Streamlit para gerenciar projetos, membros da equipe e tarefas em um time de desenvolvimento de software. O sistema permite o controle de alocação de membros, visualização de tarefas, e acompanhamento de status, datas de início e término.

📋 Funcionalidades
Cadastro de projetos

Cadastro de membros da equipe

Criação e visualização de tarefas

Alocação de membros a tarefas em diferentes projetos

Registro de datas de início e término

Acompanhamento do status das tarefas

🧱 Estrutura do Banco de Dados
O banco de dados é composto por três tabelas principais com os seguintes relacionamentos:

🔹 projeto
Campo	Tipo	Descrição
id_projeto	INTEGER PK	Identificador único do projeto
nome	TEXT	Nome do projeto
descricao	TEXT	Descrição do projeto

🔹 membro
Campo	Tipo	Descrição
id_membro	INTEGER PK	Identificador único do membro
nome	TEXT	Nome do membro
cargo	TEXT	Cargo/Função do membro

🔹 tarefa
Campo	Tipo	Descrição
id_tarefa	INTEGER PK	Identificador único da tarefa
id_projeto	INTEGER FK	Projeto associado à tarefa
id_membro	INTEGER FK	Membro responsável pela tarefa
titulo	TEXT	Título da tarefa
descricao	TEXT	Descrição da tarefa
data_inicio	DATE	Data de início da tarefa
data_fim	DATE	Data de término da tarefa
status	TEXT	Status atual (Pendente, Em andamento, Concluída)

💻 Tecnologias Utilizadas
Python 3.x
Streamlit
SQLite3 (ou outro banco relacional)
SQL padrão



🧪 Scripts SQL
Inclui scripts para:

Criação das tabelas (create_tables.sql)
Inserção de dados (insert_data.sql)
Consultas básicas (queries.sql)



👨‍💻 Autor
Gabriel Noronha - @NoronhaGabiel
