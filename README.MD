# 🚗 Sistema de Gerenciamento de Carros

Aplicação Web fullstack desenvolvida como trabalho da disciplina **Programação Avançada (FACAMP)**.  
O sistema permite o gerenciamento de carros com cadastro, edição, listagem e exclusão, além de autenticação de usuários.
O administrator pode criar, editar, listar e remover anúncios.
O usuario pode apenas listar os anúncios.

---

## 🔐 Contas de Teste

- **Administrador**  
  - Email: `teste@carros.com`  
  - Senha: `abc123`

- **Usuário comum**  
  - Email: `lucas@gmail.com`  
  - Senha: `123456`

> ⚠️ **Observação:** Não é possível criar novas contas de administradores, apenas do tipo usuário.

---

## 👥 Autores

- João Pedro de Paula Silva – RA: 202212014  
- Lucas Gonçalves Monteferrante – RA: 201912020

---

## 🎯 Objetivo

Criar uma aplicação web completa com:

- Integração entre **frontend (Vue.js)** e **backend (Flask)**
- Armazenamento em banco **NoSQL (MongoDB Atlas)**
- **Autenticação e controle de acesso**
- **Upload de imagens** para os carros

---

## ⚙️ Tecnologias Utilizadas

### 📌 Backend

- Python 3
- Flask
- Flask-PyMongo
- Flask-CORS
- Flask-JWT-Extended *(estrutura preparada)*
- MongoDB Atlas
- Werkzeug *(para upload de arquivos)*
- dotenv

### 🌐 Frontend

- Vue.js (Vue CLI)
- Vue Router
- Axios
- HTML5 + CSS3
- Imagens em SVG/PNG para a interface

---

## 🗂️ Estrutura de Pastas

### 📁 `crud_backend/`

├── app/
│ ├── init.py
│ ├── config.py
│ ├── routes.py
├── static/uploads/ # Imagens dos carros
├── run.py
├── requirements.txt



### 📁 `crud_frontend/`

├── src/
│ ├── assets/ # Ícones e imagens
│ ├── components/ # Login.vue, Register.vue, CarForm.vue, CarList.vue
│ ├── router/index.js # Rotas protegidas com token e tipo
│ ├── services/ # AuthService.js, CarService.js, UserService.js
│ ├── App.vue
│ └── main.js
├── static/



---

## 🔒 Funcionalidades

- Autenticação de usuários com **login** e **cadastro**
- Controle de acesso com tipos: **admin** e **usuário comum**
- CRUD completo de carros (modelo, cidade, ano, km, preço, imagem, etc.)
- Upload de imagens com validação
- Integração total com **MongoDB Atlas**
- Interface **simples e responsiva**
- Proteção de rotas no frontend usando **Vue Router**

---

## 🧪 Instalação e Execução

### 🔹 Backend

```bash
cd crud_backend

# (Opcional) Criar e ativar o ambiente virtual:
python -m venv venv
# Linux/macOS:
source venv/bin/activate
# Windows:
venv\Scripts\activate

# Instalar dependências:
pip install -r requirements.txt

# Iniciar servidor:
flask run
O backend estará disponível em http://localhost:5000

### 🔹 Frontend

```bash
cd crud_frontend

# Instalar dependências:
npm install

# Iniciar servidor:
npm run serve
O frontend estará disponível em http://localhost:8080


