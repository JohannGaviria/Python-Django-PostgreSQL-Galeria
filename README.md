# Python-Django-PostgreSQL-Galeria



## Tabla de Contenidos

- [Instalación](#instalación)
- [Uso](#uso)
- [Endpoints](#endpoints)
    - [Usuarios](#usuarios)

## Instalación

### Prerrequisitos

Antes de comenzar, asegúrate de tener instalado lo siguiente en tu sistema:

- Python (versión 3.12.2)
- PostgreSQL (versión 16)
- pip (administrador de paquetes de Python)

### Pasos de Instalación

1. **Clona este repositorio:**

```bash
git clone https://github.com/JohannGaviria/Python-Django-PostgreSQL-Galeria.git
```

2. **Crear el entorno virtual:**

Utiliza `virtualenv` o otro gestor de entornos virtuales

```bash
pip install virtualenv
python -m virtualenv venv
```

3. **Instalar las dependencias:**

```bash
cd Python-Django-PostgreSQL-Galeria
pip install -r requirements.txt
```

4. **Configurar la base de datos:**

- Crea una base de datos PostgreSQL en tu entorno.
- Crea un archivo `.env` en la ruta raiz de tu proyecto y crea las variables de entorno con los datos correpodientes:
    - SECRET_KEY
    - ENGINE
    - NAME
    - USER
    - PASSWORD
    - HOST
    - PORT

5. **Crea las migraciones:**

```bash
python manage.py makemigrations
python manage.py migrate
```

6. **Ejecutar el servidor:**

```bash
python manage.py runserver
```

¡Listo! El proyecto ahora debería estar en funcionamiento en tu entorno local. Puedes acceder a él desde tu navegador web visitando `http://localhost:8000`.

## Endpoints

### Usuarios

| Nombre | Método | Url | Descripción |
|:------ | :----- | :-- | :---------- |
| [Registro de Usuarios](#registro-de-usuario) | `POST` | `/api/users/register/` | Registrar un nuevo usuario en el sistema. |
| [Inicio de Sesión de Usuarios](#inicio-de-sesión-de-usuario) | `POST` | `/api/users/login/` | Iniciar sesión de un usuario con sus credenciales. |
| [Cierre de Sesión de Usuarios](#cierre-de-sesión-de-usuario) | `POST` | `/api/users/logout/` | Cerrar sesión de un usuario autenticado. |
| [Obtener Perfil de Usuarios](#obtener-perfil-del-usuario) | `GET` | `/api/users/profile/` | Obtener la información del perfil del usuario actual. |
| [Actualizar Perfil de Usuarios](#actualizar-la-información-del-perfil) | `PUT` | `/api/users/profile/` | Actualizar la información del perfil del usuario. |
| [Eliminar Perfil de Usuarios](#elimnar-el-perfil-del-usuario) | `DELETE` | `/api/users/register/` | Eliminar el perfil del usuario actual. |

#### Registro de usuario

##### Método HTTP

```http
POST /api/users/register/
```

##### Parámetros

| Parámetro | Tipo     | Descripción                |
| :-------- | :------- | :------------------------- |
| `username` | `string` | **Requerido**. Nombre del usuario |
| `email` | `string` | **Requerido**.  Correo electrónico del usuario |
| `password` | `string` | **Requerido**. Contraseña del usuario |
| `photo` | `file` | Imagen de perfil del usuario |

##### Ejemplo de solicitud

```http
Content-Type: multipart/form-data

--boundary
Content-Disposition: form-data; name="username"
Test Username

--boundary
Content-Disposition: form-data; name="email"
test@email.com

--boundary
Content-Disposition: form-data; name="password"
TestPassword

--boundary
Content-Disposition: form-data; name="photo"; filename="photo.jpg"
Content-Type: image/jpeg

(binary data)
--boundary--
```

##### Ejemplo de respuesta exitosa

```http
HTTP/1.1 201 Created
Content-Type: application/json

{
	"status": "success",
	"message": "Registration successful",
	"data": {
		"token": {
			"token_key": "692c45e4baa097624b741fbeb42eae9b9f30ded7"
		},
		"user": {
			"id": 1,
			"username": "Test Username",
			"email": "test@email.com",
			"register_date": "2024-07-10T21:49:47.559669Z",
			"photo_profile": "photo.jpg",
			"public_profile": true
		}
	}
}
```

#### Inicio de sesión de usuario

##### Método HTTP

```http
POST /api/users/login/
```

##### Parámetros

| Parámetro | Tipo     | Descripción                |
| :-------- | :------- | :------------------------- |
| `email` | `string` | **Requerido**.  Correo electrónico del usuario |
| `password` | `string` | **Requerido**. Contraseña del usuario |

##### Ejemplo de solicitud

```http
Content-Type: application/json

{
    "email": "test@email.com",
    "password": "TestPassword"
}
```

##### Ejemplo de respuesta exitosa

```http
HTTP/1.1 201 Created
Content-Type: application/json

{
	"status": "success",
	"message": "Login successful",
	"data": {
		"token": {
			"token_key": "692c45e4baa097624b741fbeb42eae9b9f30ded7",
			"token_expiration": "2024-07-13T22:03:26.013950Z"
		},
		"user": {
			"id": 1,
			"username": "Test Username",
			"email": "test@email.com",
			"register_date": "2024-07-10T21:49:47.559669Z",
			"photo_profile": "photo.jpg",
			"public_profile": true
		}
	}
}
```

#### Cierre de sesión de usuario

##### Método HTTP

```http
POST /api/users/logout/
```

##### Parámetros

| Parámetro | Tipo     | Descripción                |
| :-------- | :------- | :------------------------- |
| `token` | `string` | **Requerido**.  Token de autenticación |

##### Ejemplo de solicitud

```http
Content-Type: application/json
Authorization: Token <token>
```

##### Ejemplo de respuesta exitosa

```http
HTTP/1.1 200 Ok
Content-Type: application/json

{
	"status": "success",
	"message": "Logout successful"
}
```

#### Obtener perfil del usuario

##### Método HTTP

```http
GET /api/users/profile/
```

##### Parámetros

| Parámetro | Tipo     | Descripción                |
| :-------- | :------- | :------------------------- |
| `token` | `string` | **Requerido**.  Token de autenticación |

##### Ejemplo de solicitud

```http
Content-Type: application/json
Authorization: Token <token>
```

##### Ejemplo de respuesta exitosa

```http
HTTP/1.1 200 Ok
Content-Type: application/json

{
	"status": "success",
	"message": "Profile loaded successfully",
	"data": {
		"user": {
			"id": 1,
			"username": "Test Username",
			"email": "test@email.com",
			"register_date": "2024-07-10T21:49:47.559669Z",
			"photo_profile": "photo.jpg",
			"public_profile": true
		}
	}
}
```

#### Actualizar la información del perfil

##### Método HTTP

```http
PUT /api/users/profile/
```

##### Parámetros

| Parámetro | Tipo     | Descripción                |
| :-------- | :------- | :------------------------- |
| `token` | `string` | **Requerido**.  Token de autenticación |
| `username` | `string` | **Requerido**.  Nombre del usuario |
| `email` | `string` | **Requerido**.  Correo electrónico del usuario |
| `password` | `string` | Contraseña del usuario |
| `photo` | `file` | Imagen de perfil del usuario |
| `public_profile` | `bool` | Perfil del usuario publico o privado |

##### Ejemplo de solicitud

```http
Content-Type: multipart/form-data
Authorization: Token <token>

--boundary
Content-Disposition: form-data; name="username"
Test Updated Username

--boundary
Content-Disposition: form-data; name="email"
test@email.com

--boundary
Content-Disposition: form-data; name="password"
TestPassword

--boundary
Content-Disposition: form-data; name="photo"; filename="photo.jpg"
Content-Type: image/jpeg

(binary data)
--boundary--
```

##### Ejemplo de respuesta exitosa

```http
HTTP/1.1 200 Ok
Content-Type: application/json

{
	"status": "success",
	"message": "Profile updated successfully",
	"data": {
		"token": {
			"token_key": "2e94124712912a44b40654189bde2df69076142f",
			"token_expiration": "2024-07-13T22:26:12.576243Z"
		},
		"user": {
			"id": 1,
			"username": "Test Updated Username",
			"email": "test@email.com",
			"register_date": "2024-07-10T21:49:47.559669Z",
			"photo_profile": "photo.jpg",
			"public_profile": true
		}
	}
}
```

#### Elimnar el perfil del usuario

##### Método HTTP

```http
DELETE /api/users/profile/
```

##### Parámetros

| Parámetro | Tipo     | Descripción                |
| :-------- | :------- | :------------------------- |
| `token` | `string` | **Requerido**.  Token de autenticación |

##### Ejemplo de solicitud

```http
Content-Type: application/json
Authorization: Token <token>
```

##### Ejemplo de respuesta exitosa

```http
HTTP/1.1 200 Ok
Content-Type: application/json

{
	"status": "success",
	"message": "Profile deleted successfully"
}
```
