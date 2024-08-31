# ITSense Inventory Management System

Este repositorio contiene dos proyectos: una API desarrollada en Django y un frontend desarrollado en Next.js. Sigue las instrucciones a continuación para configurar y ejecutar ambos proyectos.

## Estructura del Repositorio

├── api_itsense # Proyecto Django para la API 
├── inventory_itsense_front # Proyecto Next.js para el frontend 
└── README.md # Este archivo README


## 1. API - Django (`api_itsense`)

### Requisitos Previos

- Python 3.8 o superior
- PostgreSQL
- Virtualenv (opcional pero recomendado)

### Instalación

1. Clonar el repositorio:

   git clone https://github.com/tu_usuario/tu_repositorio.git
   cd tu_repositorio/api_itsense
Crear y activar un entorno virtual (opcional pero recomendado):


python3 -m venv env
source env/bin/activate  # En Windows usa `env\Scripts\activate`

Instalar las dependencias:

pip install -r requirements.txt
Configuración
Configurar la base de datos en settings.py:

Abre api_itsense/settings.py y asegúrate de configurar la base de datos PostgreSQL:

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'tu_nombre_base_datos',
        'USER': 'tu_usuario',
        'PASSWORD': 'tu_contraseña',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

Ejecutar migraciones:
python manage.py makemigrations
python manage.py migrate
Crear un superusuario para acceder al panel de administración de Django:


python manage.py createsuperuser
Ejecutar el servidor de desarrollo:


python manage.py runserver
La API debería estar disponible en http://localhost:8000.

2. Frontend - Next.js (inventory_itsense_front)
Requisitos Previos
Node.js 18 o superior
npm (o Yarn)
Instalación

Navegar al directorio del frontend:

cd ../inventory_itsense_front

Instalar las dependencias:

npm install
# o
yarn install

Ejecución
Ejecutar el servidor de desarrollo de Next.js:

npm run dev
# o
yarn dev
El frontend debería estar disponible en http://localhost:3000.

3. Notas Adicionales
Asegúrate de que tanto el backend como el frontend estén configurados para comunicarse entre sí correctamente.
Puedes modificar las configuraciones de ambos proyectos según tus necesidades específicas.
