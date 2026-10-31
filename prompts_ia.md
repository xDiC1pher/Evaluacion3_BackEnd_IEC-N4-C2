# Registro de Asistencia de Inteligencia Artificial (Evaluación 3)

**Proyecto:** PetCare Hub - Despliegue Evaluación 3 Backend  
**Desarrollador:** José Ignacio González Leyton

Durante la fase de despliegue en la infraestructura de AWS EC2, se empleó asistencia de Inteligencia Artificial como arquitecto consultivo para diagnosticar anomalías de servidor, resolver discrepancias entre el ORM de Django y PostgreSQL, y establecer un pipeline seguro de integración continua.

## Casos de Uso y Resoluciones Arquitectónicas

### 1. Diagnóstico de Capa de Red y Reverse Proxy (Nginx)
* **Incidencia:** Al intentar acceder a la IP pública tras configurar Nginx y Gunicorn, el navegador arrojaba un error `ERR_CONNECTION_TIMED_OUT`.
* **Análisis y Resolución IA:** La IA diagnosticó que el problema no radicaba en el Security Group de AWS (puerto 80 abierto correctamente), sino en el mecanismo HSTS de los navegadores modernos que fuerzan peticiones por el puerto 443 (HTTPS). Se recomendó forzar el prefijo `http://` en el navegador o validar internamente con `curl -I http://localhost` vía SSH. Esto confirmó que el Reverse Proxy estaba operando a la perfección y aisló el falso positivo.

### 2. Conflicto de Sensibilidad de Mayúsculas en PostgreSQL
* **Incidencia:** Django arrojaba la excepción `FATAL: database "veterinaria_poo_GONZALEZ" does not exist` al intentar migrar los modelos, a pesar de que el comando `CREATE DATABASE` había sido ejecutado.
* **Análisis y Resolución IA:** Se diagnosticó una discrepancia entre la configuración del ORM de Django y el comportamiento estándar de PostgreSQL, el cual convierte automáticamente todos los identificadores a minúsculas (`veterinaria_poo_gonzalez`). La IA generó un bloque SQL específico utilizando comillas dobles (`CREATE DATABASE "veterinaria_poo_GONZALEZ";`) para forzar la nomenclatura exacta diseñada para la asignatura, manteniendo la consistencia de los archivos de configuración.

### 3. Validación de Integridad Referencial en Ciclo CRUD
* **Incidencia:** Durante las pruebas transaccionales (Create) mediante la API del frontend, el sistema devolvió un error de JavaScript al agendar una cita.
* **Análisis y Resolución IA:** El diagnóstico indicó que la base de datos de producción estaba vacía, lo que generaba un rechazo por restricción de llaves foráneas (*Foreign Key Constraint*) al intentar asignar una cita a los IDs 1 de "Mascota" y "Veterinario". Se proporcionó un flujo de datos estructurado paso a paso para poblar primero las entidades maestras desde el panel `/admin`, respetando la dependencia del modelo `Veterinario` con el modelo `User` nativo de Django, lo que permitió concluir con éxito la validación CRUD.

### 4. Implementación de Pipeline Seguro (Desacoplamiento CI/CD)
* **Incidencia:** Necesidad de refactorizar el modal de la interfaz desde el entorno local (Windows/VS Code) mediante Git, con el riesgo de sobrescribir configuraciones críticas del servidor (`ALLOWED_HOSTS`, credenciales de DB) con un `git pull`.
* **Análisis y Resolución IA:** La IA asesoró contra maniobras temporales como `git stash` y diseñó una arquitectura de variables de entorno de nivel de producción. Se instruyó la instalación de `python-dotenv`, la creación de un archivo `.env` aislado en AWS, y la refactorización de `settings.py` utilizando `os.getenv()`. Esto blindó las credenciales y habilitó despliegues continuos seguros.

### 5. Refactorización de Usabilidad (Consumo de API Frontend)
* **Incidencia:** El formulario para agendar citas requería el ingreso manual de IDs numéricos, lo que contravenía normativas de usabilidad.
* **Análisis y Resolución IA:** Se generó el código HTML/JavaScript exacto para reemplazar los `inputs` estáticos por elementos `<select>` dinámicos. El script proporcionado utiliza la API Fetch de forma asíncrona para consumir los endpoints REST de Django (`/api/mascotas/` y `/api/veterinarios/`) y poblar los desplegables, mejorando drásticamente la interfaz gráfica.