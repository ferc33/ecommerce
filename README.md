
# 📊 Proyecto Principal de E-commerce

Este proyecto es una plataforma de comercio electrónico desarrollada para gestionar inventarios, procesar pedidos y manejar datos de clientes de manera eficiente.

## 🚀 Tecnologías Utilizadas

- **Frontend**: React.js
- **Backend**: Django
- **Base de Datos**: PostgreSQL


## 🛠️ Instalación

1. Clona el repositorio:
   ```sh
   git clone https://github.com/ferc33/ecommerce-main.git
   ```
2. Navega al directorio del proyecto:
   ```sh
   cd ecommerce-main
   ```
3. Configura el entorno virtual e instala las dependencias:
   ```sh
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```
4. Configura los ajustes de la base de datos en `settings.py`.

## ⚙️ Configuración

1. Aplica las migraciones de la base de datos:
   ```sh
   python manage.py migrate
   ```
2. Crea un superusuario para acceso de administrador:
   ```sh
   python manage.py createsuperuser
   ```
3. Ejecuta el servidor de desarrollo:
   ```sh
   python manage.py runserver
   ```

## 🚀 Uso

1. Accede al panel de administración en `http://localhost:8000/admin` para gestionar inventarios y pedidos.
2. Explora el sitio web principal en `http://localhost:8000/`.

## 🌟 Funcionalidades

- **Autenticación de Usuarios**: Inicio de sesión y registro seguro.
- **Gestión de Productos**: Añadir, editar y eliminar productos.
- **Procesamiento de Pedidos**: Manejar pedidos de clientes de manera eficiente.
- **Gestión de Inventarios**: Seguimiento de niveles de stock de productos.
- **Diseño Responsivo**: Interfaz de usuario amigable para móviles.

## 🤝 Contribuciones

1. Haz un fork del repositorio.
2. Crea tu rama de funcionalidad (`git checkout -b feature/FuncionalidadAsombrosa`).
3. Realiza tus cambios (`git commit -m 'Añadir FuncionalidadAsombrosa'`).
4. Sube los cambios a la rama (`git push origin feature/FuncionalidadAsombrosa`).
5. Abre un pull request.

## 📜 Licencia

Distribuido bajo la Licencia MIT. Consulta el archivo `LICENSE` para más información.

## 📧 Contacto

- Correo electrónico: fcassera@protonmail.com
- Enlace del proyecto: [https://github.com/ferc33/ecommerce](https://github.com/ferc33/ecommerce)

