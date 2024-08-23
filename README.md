# Criando o Ambiente Virtual
`python -m venv venv`

# Ativando o abiente virtual
`venv/Scrtips/activate`

# Instalando o DRF
`pip install django djangorestframework` 

# Criando o Projeto
`django-admin startproject escola`
`
# Criando APP Escola
`python .manage.py startapp estudantes`

# Adicionando nos Apps
INSTALLED_APPS = [
    ...
    'rest_framework',
    'estudantes',
]


# Aplicando as Migrações
`python manage.py makemigrations`
`python manage.py migrate`

# Rodando o Servidor
`python manage.py runserver` 




- Prof. Esp. Emeson Borges
