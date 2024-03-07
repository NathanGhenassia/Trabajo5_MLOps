# Documentation
Programa en Python y con FastAPI que desarrolla las 
siguientes APIs:
1. Registro de Usuarios:
Método: POST
Descripción: Crea un endpoint para registrar usuarios.
Ejemplo:
Endpoint: /register
Parámetros: Nombre de usuario, correo electrónico y contraseña.
Respuesta: Mensaje de éxito o error.
2. Obtener Datos de Usuario:
Método: GET
Descripción: Obtiene información de un usuario específico.
Ejemplo:
Endpoint: /user/{id}
Parámetros: ID del usuario.
Respuesta: Devuelve los datos del usuario si existe, de lo contrario, un mensaje 
de error.
3. Crear Tareas:
Método: POST
Descripción: Permite a los usuarios crear nuevas tareas.
Ejemplo:
Endpoint: /tasks/create
Parámetros: Título de la tarea, descripción y estado (pendiente, en progreso, 
completada).
Respuesta: Confirmación de creación de tarea.
4. Listar Tareas por Usuario:
Método: GET
Descripción: Devuelve todas las tareas asociadas a un usuario.
Ejemplo:
Endpoint: /tasks/{user_id}
Parámetros: ID del usuario.
Respuesta: Lista de tareas del usuario especificado.