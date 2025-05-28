![2criandostorageaccount](https://github.com/user-attachments/assets/beeca42a-e170-4249-a409-24f570a0616b)# Armazenando-dados-de-um-E-commerce-na-cloud-
The following repository was created by me as part of a Bootcamp project for evaluation and approval purposes. Although the task involves basic steps and configurations, the implementation was carried out according to the requirements described in the Challenge Description.

Este repositório foi criado por mim como parte de um projeto de Bootcamp para fins de avaliação e aprovação. Embora a tarefa envolva etapas e configurações básicas, a implementação foi realizada conforme os requisitos descritos na Descrição do Desafio.


# 📘 Projeto de Desafio - Bootcamp DIO

> ⚠️ O seguinte README refere-se a um projeto para a obtenção de nota ou aprovação em um Bootcamp da DIO e está de acordo com a respectiva **"Descrição do Desafio"** que possuir.  
> Em determinados casos, o projeto possui entregas **simplesmente visuais que sejam apresentadas neste README do GitHub**. Neste caso, a entrega do projeto será realizada por meio deste arquivo (explicações) e com os códigos utilizados sendo subidos para o repositório.

---

## 🖥️ Passos Realizados

A seguir, os passos executados no projeto **Armazenando dados de um E-Commerce na Cloud**, utilizando a plataforma **Azure**:

### 🔹 Criação do Resource Group `Lab001`
- Provisionado dentro da conta **Azure trial**
- Etapa inicial para organização dos recursos em ambiente controlado

![0criando_RG-lab001- tag](https://github.com/user-attachments/assets/66bde8f2-b511-4004-aeb0-dcef9c97c26f)

---

### 🔹 Criação do SQL Server e SQL Database
- SQL Server foi criado em conjunto com o banco de dados SQL Database
- Essa abordagem foi adotada pois não havia outro SQL Server disponível na conta

![1criandosqlserver sqldatabase](https://github.com/user-attachments/assets/fcbca0e2-a13d-4a8a-aea0-74ec1e5c0c8c)

---

### 🔹 Criação do Storage Account e Container
- Criação do Storage Account na mesma região
- Adicionado um container chamado `"fotos"` para armazenar as imagens dos produtos

![2criandostorageaccount](https://github.com/user-attachments/assets/c06d70db-19dd-4026-a09a-ab21e59a2acf)

---

### 🔹 Configuração do `.env`
- Foi criado um arquivo `.env` para armazenar as variáveis de ambiente utilizadas pelo app
- Essa etapa foi essencial para garantir a conexão adequada com os serviços da nuvem

![3configuracoes_iniciais_dotenv](https://github.com/user-attachments/assets/a31ed4cb-2104-4e90-934f-b10d1d41ea63)

---

### 🔹 Erro de acesso negado ao Query Editor
- Ao tentar acessar o Query Editor do Azure, ocorreu um erro de negação de acesso
- Motivo: ausência de autorização para acesso público ao banco de dados

![4errodenypublicaccess](https://github.com/user-attachments/assets/3e874bb8-9ef9-49d3-947e-6c743db23e6d)

---

### 🔹 Resolução do Erro de Rede
- Foi necessário acessar a aba **"Networking"** no painel do SQL Server
- Alterado para "Selected networks", o que permitiu:
  - Adicionar o IP local manualmente
  - Habilitar a opção "Allow Azure Services" para comunicação interna

![5resolveproblema](https://github.com/user-attachments/assets/6546e4a7-6adc-4f0b-a10f-a47f48a3f26f)

---

### 🔹 Erro de Conexão com o Banco
- O erro a seguir foi enfrentado ao tentar conectar com `pymssql`:
  (20009, b'DB-Lib error message 20009, severity 9:\nUnable to connect: Adaptive Server is unavailable or does not exist...')

- Esse erro, pelo que parece, está relacionado à forma como o `pymssql` se conecta — talvez por incompatibilidade com TLS ou falta de suporte moderno.
- Sendo assim, foi feita a troca da biblioteca para `pyodbc`, que pessoalmente prefiro, e o projeto foi adaptado para ela.

![6errodeconexao ](https://github.com/user-attachments/assets/b0a4a945-e86f-474f-a405-670cf9bf51b3)



![7solucaoerroconexao](https://github.com/user-attachments/assets/a5f46c72-00a8-4fd6-8b54-54912c0a5363)

---

### 🔹 Teste isolado de conexão com o banco
- Foi criado um script separado para testar a conexão com o banco antes de integrá-la ao Streamlit
- Esse teste confirmou que com `pyodbc` a conexão acontecia como esperado

---

## 🧾 Notas Finais

Este README documenta a execução do projeto conforme orientações do desafio do Bootcamp DIO.  
As configurações e arquivos utilizados no VS Code estão presentes neste repositório.


Este README é um modelo padrão reutilizável para projetos desenvolvidos em bootcamps da DIO.  
Adapto conforme o desafio proposto, mantendo a estrutura clara e objetiva.

---



