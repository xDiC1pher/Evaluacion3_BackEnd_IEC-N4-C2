# PetCare Hub - Despliegue en AWS EC2 (Evaluación 3)

**Autor:** José Ignacio González Leyton  
**Sección:** IEC-N4-C2/D  
**Asignatura:** Desarrollo Back End 3

## Descripción del Proyecto
Despliegue en entorno de producción de la plataforma de gestión veterinaria "PetCare Hub". La arquitectura separa la lógica de la aplicación, el servidor web y el motor de base de datos relacional para garantizar alta disponibilidad y seguridad.

## Arquitectura de Infraestructura
* **Proveedor Cloud:** Amazon Web Services (AWS EC2)
* **Sistema Operativo:** Ubuntu 24.04 LTS
* **Servidor Web / Reverse Proxy:** Nginx
* **Servidor de Aplicaciones (WSGI):** Gunicorn
* **Motor de Base de Datos:** PostgreSQL
* **Framework Backend:** Django 5.x

## Configuraciones Críticas Realizadas
1. **Seguridad Perimetral (AWS):** Configuración del Security Group `launch-wizard-1` para habilitar tráfico SSH (Puerto 22) y HTTP (Puerto 80).
2. **Motor de Datos:** Creación de la base de datos `veterinaria_poo_GONZALEZ` forzando sensibilidad a mayúsculas y asignación de privilegios al usuario `petcare_admin`.
3. **Desacoplamiento de Entorno:** Integración de la librería `python-dotenv` para aislar credenciales sensibles (claves, usuarios, hosts) en un archivo `.env` externo al control de versiones.
4. **Validación CRUD:** Ejecución exitosa de migraciones, creación de superusuario y validación de operaciones transaccionales (Crear, Leer, Actualizar, Eliminar) mediante la interfaz web pública.

## Acceso al Sistema
* **IP Pública:** http://184.194.46.254/