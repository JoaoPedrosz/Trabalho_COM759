Admin: teste@carros.com
Senha: abc123

usuario teste:lucas@gmail.com
senha: 123456

# 🚗 Sistema de Gerenciamento de Carros

Aplicação Web fullstack desenvolvida como **trabalho da disciplina Programação Avançada (FACAMP)**. O sistema permite o gerenciamento de carros com cadastro, edição, listagem e exclusão, além de autenticação de usuários.

## 🎯 Objetivo

Criar uma aplicação web completa com:
- Integração entre frontend (Vue.js) e backend (Flask)
- Armazenamento em banco NoSQL (MongoDB Atlas)
- Autenticação e controle de acesso
- Upload de imagens

## ⚙️ Tecnologias Utilizadas

### 📌 Backend
- Python 3
- Flask
- Flask-PyMongo
- Flask-CORS
- Flask-JWT-Extended (estrutura preparada)
- MongoDB Atlas
- Werkzeug (upload de arquivos)
- dotenv

### 🌐 Frontend
- Vue.js (Vue CLI)
- Vue Router
- Axios
- HTML5 + CSS3
- Imagens em SVG/PNG para UI

## 🗂️ Estrutura de Pastas

```
📁 backend/
├── __init__.py
├── config.py
├── routes.py
├── run.py
├── requirements.txt
└── static/uploads/         # Imagens dos carros

📁 frontend/
├── src/
│   ├── assets/             # Ícones e imagens
│   ├── components/         # Componentes Vue: Login, Register, CarForm, CarList
│   ├── router/index.js     # Rotas protegidas com token e tipo
│   ├── services/           # CarService, UserService
│   ├── App.vue
│   └── main.js
└── static/
```

## 🔒 Funcionalidades

- Autenticação de usuários com `login` e `register`
- Controle de acesso por tipo de usuário (`admin` e `usuario`)
- CRUD de carros (modelo, cidade, ano, km, preço, imagem etc.)
- Upload de imagens com validação
- Integração com MongoDB Atlas
- Interface simples e responsiva
- Proteção de rotas no frontend via Vue Router

## 🧪 Instalação e Execução

### 🔹 Backend

1. Acesse a pasta:
   ```bash
   cd backend
   ```

2. Crie o ambiente virtual (opcional):
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/macOS
   venv\Scripts\activate   # Windows
   ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

4. Crie um arquivo `.env` com a URI do seu MongoDB Atlas:
   ```
   SECRET_KEY=sua_chave_secreta
   MONGO_URI=sua_uri_mongodb
   ```

5. Exporte a variável de ambiente `FLASK_APP`:
   - No **Linux/macOS**:
     ```bash
     export FLASK_APP=run.py
     ```
   - No **Windows (CMD)**:
     ```cmd
     set FLASK_APP=run.py
     ```
   - No **Windows (PowerShell)**:
     ```powershell
     $env:FLASK_APP = "run.py"
     ```

6. Inicie o servidor:
   ```bash
   flask run
   ```

> O backend estará disponível em `http://localhost:5000`

### 🔹 Frontend

1. Acesse a pasta do frontend:
   ```bash
   cd frontend
   ```

2. Instale as dependências:
   ```bash
   npm install
   ```

3. Inicie o servidor:
   ```bash
   npm run serve
   ```

> O frontend estará disponível em `http://localhost:8080`

## 📌 Observações

- As imagens dos carros são salvas localmente na pasta `static/uploads/`.
- A autenticação ainda não usa criptografia. Recomenda-se usar `bcrypt` em produção.
- As rotas protegidas redirecionam usuários comuns quando tentam acessar funcionalidades administrativas.
- O token de autenticação é armazenado no `localStorage`.

## 👥 Autores

- João Pedro de Paula Silva – RA: 202212014  
- Lucas Gonçalves Monteferrante – RA: 201912020
