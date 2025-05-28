import streamlit as st
from azure.storage.blob import BlobServiceClient
import os
import uuid
import pyodbc
from dotenv import load_dotenv

load_dotenv()

blobConnectionString = os.getenv('BLOB_CONNECTION_STRING')
blobContainerName = os.getenv('BLOB_CONTAINER_NAME')
blobaccountName = os.getenv('BLOB_ACCOUNT_NAME')

SQL_SERVER = os.getenv('SQL_SERVER')
SQL_DATABASE = os.getenv('SQL_DATABASE')
SQL_USER = os.getenv('SQL_USER')
SQL_PASSWORD = os.getenv('SQL_PASSWORD')

st.title('Cadastro de Produtos')

#formulário de cadastro de produtos
product_name = st.text_input('Nome do Produto')
product_price = st.number_input('Preço do Produto', min_value=0.0, format='%.2f')
product_description = st.text_area('Descrição do Produto')
product_image = st.file_uploader('Imagem do Produto', type=['jpg', 'png', 'jpeg'])


# Save image on blob storage
def upload_blob(file):
    blob_service_client = BlobServiceClient.from_connection_string(blobConnectionString)
    container_client = blob_service_client.get_container_client(blobContainerName)
    blob_name = str(uuid.uuid4()) + file.name
    blob_client = container_client.get_blob_client(blob_name)
    blob_client.upload_blob(file.read(), overwrite=True)
    image_url = f"https://{blobaccountName}.blob.core.windows.net/{blobContainerName}/{blob_name}"
    return image_url

def insert_product(product_name, product_price, product_description, product_image):
    try:
        image_url = upload_blob(product_image)
        print("Tentando conectar...")
        conn_str = (
            f"DRIVER={{ODBC Driver 18 for SQL Server}};"
            f"SERVER={SQL_SERVER};"
            f"DATABASE={SQL_DATABASE};"
            f"UID={SQL_USER};"
            f"PWD={SQL_PASSWORD};"
            f"Encrypt=yes;"
            f"TrustServerCertificate=no;"
            f"Connection Timeout=30;"
        )
        conn = pyodbc.connect(conn_str)
        print("Conectado.")
        cursor = conn.cursor()
        insert_sql = "INSERT INTO Produtos (nome, preco, descricao, imagem_url) VALUES (?, ?, ?, ?)"
        print(insert_sql)
        cursor.execute(insert_sql, (product_name, product_price, product_description, image_url))
        conn.commit()
        conn.close()
        return True
    except Exception as e:
        st.error(f'Erro ao inserir produto: {e}')
        return False

def list_products():
    try:
        conn_str = (
            f"DRIVER={{ODBC Driver 18 for SQL Server}};"
            f"SERVER={SQL_SERVER};"
            f"DATABASE={SQL_DATABASE};"
            f"UID={SQL_USER};"
            f"PWD={SQL_PASSWORD};"
            f"Encrypt=yes;"
            f"TrustServerCertificate=no;"
            f"Connection Timeout=30;"
        )
        conn = pyodbc.connect(conn_str)
        cursor = conn.cursor()
        cursor.execute("SELECT nome, preco, descricao, imagem_url FROM Produtos")
        products = cursor.fetchall()
        conn.close()
        return products
    except Exception as e:
        st.error(f'Erro ao listar produtos: {e}')
        return []
    
def list_products_screen():
    products = list_products()
    if products:
        for product in products:
            st.subheader(product[0])
            st.write(f"Preço: R$ {product[1]:.2f}")
            st.write(product[2])
            st.image(product[3], use_column_width=True)
    else:
        st.write("Nenhum produto cadastrado.")

if st.button('Salvar Produto'):
    insert_product(product_name, product_price, product_description, product_image)
    return_message = "Produto salvo"
    list_products_screen()

st.header('Produtos cadastrados')

if st.button ('Listar Produtos'):
    list_products_screen()
    return_message = 'Produtos listados com sucesso'
