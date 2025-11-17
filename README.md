Biblioteca Pública Digital
Uma aplicação web moderna para gerenciamento de bibliotecas públicas, desenvolvida com React + Vite no frontend e Django REST Framework no backend.

📖 Sobre o Projeto
O Biblioteca Pública Digital é uma solução completa para gerenciamento de acervos bibliográficos, empréstimos e usuários. A plataforma permite:

📚 Catálogo digital de livros com busca avançada

👥 Gestão de usuários e membros

🔄 Sistema de empréstimos e devoluções

📊 Dashboard administrativo

🔐 Autenticação e autorização de usuários

🚀 Tecnologias Utilizadas
Frontend
React 18 - Biblioteca JavaScript para interfaces

Vite - Build tool e dev server

Axios - Cliente HTTP

Backend
Django - Framework web Python

Django REST Framework - API REST

SQLite - Banco de dados (desenvolvimento)

Django Admin - Interface administrativa

🛠️ Como Executar o Projeto
Pré-requisitos
Node.js 16+

Python 3.8+

pip (gerenciador de pacotes Python)

⚡ Início Rápido (5 Passos)
1. Clone e acesse o projeto
bash
git clone https://github.com/seu-usuario/biblioteca-publica.git
cd biblioteca-publica
2. Configure e execute o Backend
bash
# Navegue para a pasta do backend
cd projeto

# Crie e ative o ambiente virtual
python -m venv venv
venv\Scripts\activate  # Windows
# source venv/bin/activate  # Linux/Mac

# Instale as dependências
pip install django djangorestframework django-cors-headers

# Execute as migrações e inicie o servidor
python manage.py migrate
python manage.py runserver
3. Configure e execute o Frontend
bash
# Em outro terminal, navegue para a pasta do frontend
cd frontend

# Instale as dependências
npm install

# Execute o servidor de desenvolvimento
npm run dev
4. Acesse a aplicação
Frontend: http://localhost:5173

Backend API: http://localhost:8000

Admin Django: http://localhost:8000/admin

5. Crie um superusuário para acessar o admin
bash
cd projeto
python manage.py createsuperuser
🏗️ Estrutura do Projeto
text
BIBLIOTECA-PUBLICA/
├── 📁 frontend/                 # Aplicação React + Vite
│   ├── 📁 src/
│   │   ├── 📁 components/      # Componentes reutilizáveis
│   │   ├── 📁 pages/          # Páginas da aplicação
│   │   ├── 📁 api/            # Serviços de API
│   │   ├── 📁 assets/         # Imagens e recursos estáticos
│   │   ├── App.jsx            # Componente principal
│   │   ├── main.jsx           # Ponto de entrada
│   │   └── index.css          # Estilos globais
│   ├── package.json
│   └── vite.config.js
│
└── 📁 projeto/                 # Backend Django
    ├── 📁 biblioteca/         # App principal
    ├── db.sqlite3             # Banco de dados
    ├── manage.py              # Script de gerenciamento
    └── requirements.txt       # Dependências Python
📊 Funcionalidades do Sistema
🎯 Módulos Principais
1. Gestão de Livros
Cadastro de livros com título, autor, ano e gênero

Controle de disponibilidade

Catálogo organizado

2. Sistema de Empréstimos
Registro de empréstimos por usuário

Controle de datas de devolução

Status dos empréstimos ("Em andamento")

Integração com fuso horário do servidor

3. Gestão de Usuários
Cadastro completo de usuários

Sistema de autenticação

Controle de status (staff/ativo)

Validação de senhas seguras

4. Interface Administrativa
Dashboard Django Admin

CRUD completo para todos os modelos

Filtros e buscas

Gestão de permissões

🖼️ Screenshots do Sistema
📋 Painel Administrativo Django
Gestão de Empréstimos

<img width="1919" height="957" alt="Captura de tela 2025-11-17 075318" src="https://github.com/user-attachments/assets/752e5f76-cfd1-4eb0-956d-194b200d94f0" />

Cadastro de Livros

<img width="1919" height="922" alt="Captura de tela 2025-11-17 075332" src="https://github.com/user-attachments/assets/de42956b-5425-43d1-94e0-e39cd9dd584b" />

Gestão de Usuários
<img width="1919" height="1067" alt="Captura de tela 2025-11-17 075355" src="https://github.com/user-attachments/assets/8352ede5-229b-4aeb-8bf9-3b19df22e54c" />

🎯 Próximos Passos
Funcionalidades Planejadas
Interface React completa

Sistema de reservas online

Notificações por email

Relatórios estatísticos

Busca avançada

Sistema de multas

🤝 Contribuição
Fork o projeto

Crie uma branch: git checkout -b feature/nova-feature

Commit suas mudanças: git commit -m 'Adiciona nova feature'

Push para a branch: git push origin feature/nova-feature

Abra um Pull Request

