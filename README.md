Techno gas

Repuestool es un ecommerce que vende repuestos de sanitarios y gas. El proyecto está desarrollado en Django, un framework web de Python.

Descripción
Repuestool ofrece una amplia gama de repuestos de sanitarios y gas para satisfacer las necesidades de sus clientes. Los clientes pueden encontrar repuestos para todo tipo de marcas y modelos de sanitarios y gas.

El proyecto está diseñado para ser fácil de usar y navegar. Los clientes pueden encontrar fácilmente los productos que buscan utilizando la barra de búsqueda o navegando por las categorías de productos.

Instalación
Para instalar el proyecto, sigue estos pasos:

Crea un entorno virtual con Python 3.
Instala las dependencias del proyecto:
pip install -r requirements.txt


3. Crea una base de datos MySQL y crea un usuario para el proyecto:

mysql -u root -p


CREATE DATABASE repuestool;


CREATE USER 'repuestool'@'localhost' IDENTIFIED BY 'password';


GRANT ALL PRIVILEGES ON repuestool.* TO 'repuestool'@'localhost';


4. Copia el archivo `.env.example` a `.env` y configura las variables de entorno según tu entorno:

cp .env.example .env


5. Ejecuta las migraciones de Django:

python manage.py migrate


6. Crea un superusuario para el proyecto:

python manage.py createsuperuser


7. Inicia el proyecto:

python manage.py runserver


El proyecto ahora debería estar instalado y ejecutándose en tu máquina local.

## Pruebas

Para ejecutar las pruebas del proyecto, sigue estos pasos:

1. Instala las dependencias de las pruebas:

pip install -r requirements-dev.txt


2. Ejecuta las pruebas:

python manage.py test

Documentación
La documentación del proyecto se encuentra en el directorio docs.

Contribuciones
¡Las contribuciones son bienvenidas! Si encuentras algún error o tienes alguna sugerencia, por favor, abre un issue o un pull request.

Licencia
El proyecto está licenciado bajo la licencia MIT.

Este README.md incluye los siguientes detalles sobre tu proyecto:

Una descripción general del proyecto.
Instrucciones de instalación.
Pruebas.
Documentación.
Contribuciones.
Licencia.
También incluye una explicación sobre cómo instalar el proyecto, que es específico de Django.

Espero que este README.md sea útil para tu proyecto.
