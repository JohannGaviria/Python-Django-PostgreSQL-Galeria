# Python-Django-PostgreSQL-Galeria



## Tabla de Contenidos

- [Instalación](#instalación)
- [Uso](#uso)
- [Endpoints](#endpoints)
    - [Usuarios](#usuarios)
	- [Álbums](#álbumes)
	- [Imagenes](#imagenes)

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

### Álbumes

| Nombre | Método | Url | Descripción |
|:------ | :----- | :-- | :---------- |
| [Obtner álbumes del usuario](#obtener-álbumes-del-usuario) | `GET` | `/api/albums/` | Obtiene una lista de los álbumes del usuario. |
| [Crear un nuevo álbum del usuario](#crear-álbum-del-usuario) | `POST` | `/api/albums/` | Crea un nuevo álbum del usuario. |
| [Obtner álbum especifico del usuario](#obtener-álbum-especifco-del-usuario) | `GET` | `/api/albums/{album_id}/` | Obtiene un álbum especifico del usuario. |
| [Actualiza álbum del usuario](#actualizar-álbum-del-usuario) | `PUT` | `/api/albums/{album_id}/` | Actualiza un álbum del usuario. |
| [Elimanr álbum del usuario](#eliminar-álbum-del-usuario) | `DELETE` | `/api/albums/{album_id}/` | Elimina un álbum para el usuario. |

#### Obtener álbumes del usuario

##### Método HTTP

```http
GET /api/albums/
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
	"message": "Albums loaded successfully",
	"data": {
		"albumes": [
			{
				"id": 1,
				"name": "Family Photos",
				"description": "Photos of my family",
				"visibility": false,
				"creation_date": "2024-07-11T21:27:01.499433Z",
				"user": 1
			},
			{
				"id": 2,
				"name": "Vacation Photos",
				"description": "Photos from my vacation",
				"visibility": true,
				"creation_date": "2024-07-11T21:55:02.050243Z",
				"user": 1
			}
		]
	}
}
```

#### Crear álbum del usuario

##### Método HTTP

```http
POST /api/albums/
```

##### Parámetros

| Parámetro | Tipo     | Descripción                |
| :-------- | :------- | :------------------------- |
| `token` | `string` | **Requerido**.  Token de autenticación |
| `name` | `string` | **Requerido**.  Nombre del álbum |
| `description` | `string` | Descripción del álbum |
| `visibility` | `bool` | **Requerido**.  Visibilidad del álbum |
| `user` | `int` | **Requerido**.  ID del usuario creador del álbum |


##### Ejemplo de solicitud

```http
Content-Type: application/json
Authorization: Token <token>

{
	"name": "Family Photos",
	"description": "Photos of my family",
	"visibility": false,
	"user": 1
}
```

##### Ejemplo de respuesta exitosa

```http
HTTP/1.1 200 Ok
Content-Type: application/json

{
	"status": "success",
	"message": "Album created successfully",
	"data": {
		"album": {
			"id": 1,
			"name": "Family Photos",
			"description": "Photos of my family",
			"visibility": false,
			"creation_date": "2024-07-11T22:18:37.346812Z",
			"user": 1
		}
	}
}
```

#### Obtener álbum especifco del usuario

##### Método HTTP

```http
GET /api/albums/{album_id}/
```

##### Parámetros

| Parámetro | Tipo     | Descripción                |
| :-------- | :------- | :------------------------- |
| `token` | `string` | **Requerido**.  Token de autenticación |
| `album_id` | `int` | **Requerido**.  ID del álbum |

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
	"message": "Album details loaded successfully",
	"data": {
		"album": {
			"id": 1,
			"name": "Family Photos",
			"description": "Photos of my family",
			"visibility": false,
			"creation_date": "2024-07-11T22:18:37.346812Z",
			"user": 1
		}
	}
}
```

#### Actualizar álbum del usuario

##### Método HTTP

```http
PUT /api/albums/{album_id}/
```

##### Parámetros

| Parámetro | Tipo     | Descripción                |
| :-------- | :------- | :------------------------- |
| `token` | `string` | **Requerido**.  Token de autenticación |
| `album_id` | `int` | **Requerido**.  ID del álbum |
| `name` | `string` | **Requerido**.  Nombre del álbum |
| `description` | `string` | Descripción del álbum |
| `visibility` | `bool` | **Requerido**.  Visibilidad del álbum |
| `user` | `int` | **Requerido**.  ID del usuario creador del álbum |

##### Ejemplo de solicitud

```http
Content-Type: application/json
Authorization: Token <token>

{
	'name': 'Updated Album Name',
	'description': 'Updated Album Description',
	'visibility': true,
	'user': 1
}
```

##### Ejemplo de respuesta exitosa

```http
HTTP/1.1 200 Ok
Content-Type: application/json

{
	"status": "success",
	"message": "Album updated successfully",
	"data": {
		"album": {
			"id": 1,
			"name": "Updated Album Name",
			"description": "Updated Album Description",
			"visibility": true,
			"creation_date": "2024-07-11T21:27:01.499433Z",
			"user": 1
		}
	}
}
```

#### Eliminar álbum del usuario

##### Método HTTP

```http
DELETE /api/albums/{album_id}/
```

##### Parámetros

| Parámetro | Tipo     | Descripción                |
| :-------- | :------- | :------------------------- |
| `token` | `string` | **Requerido**.  Token de autenticación |
| `album_id` | `int` | **Requerido**.  ID del álbum |

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
	"message": "Album deleted successfully"
}
```

### Imagenes

| Nombre | Método | Url | Descripción |
|:------ | :----- | :-- | :---------- |
| [Obtner las imagenes del usuario](#obtener-las-imagenes-del-usuario) | `GET` | `/api/images/` | Obtiene una lista de las imagenes del usuario. |
| [Subir una nueva imagen del usuario](#subir-una-nueva-imagen-del-usuario) | `POST` | `/api/images/` | Sube una nueva imagen del usuario. |

#### Obtener las imagenes del usuario

##### Método HTTP

```http
GET /api/images/
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
	"message": "Images loaded successfully",
	"data": {
		"images": [
			{
				"id": 1,
				"title": "First photo from the family album",
				"description": "Photo in which the entire family appears reunited after 5 years.",
				"image": "/uploads/images/photo_family.png",
				"upload_date": "2024-07-16T19:45:53.974728Z",
				"user": 1,
				"album": 1
			},
			{
				"id": 2,
				"title": null,
				"description": null,
				"image": "/uploads/images/photo_random_in_paris.jpg",
				"upload_date": "2024-07-16T19:47:02.577685Z",
				"user": 1,
				"album": null
			}
		]
	}
}
```

#### Subir una nueva imagen del usuario

##### Método HTTP

```http
POST /api/images/
```

##### Parámetros

| Parámetro | Tipo     | Descripción                |
| :-------- | :------- | :------------------------- |
| `token` | `string` | **Requerido**.  Token de autenticación |
| `title` | `string` | Titulo de la imagen |
| `description` | `string` | Descripción de la imagen |
| `image` | `file` | **Requerido**.  Archivo (jpg, png) de la imagen |
| `user` | `int` | **Requerido**.  ID del usuario |
| `album` | `int` | ID del álbum |

##### Ejemplo de solicitud

```http
Content-Type: multipart/form-data
Authorization: Token <token>

--boundary
Content-Disposition: form-data; name="title"
First photo from the family album

--boundary
Content-Disposition: form-data; name="description"
Photo in which the entire family appears reunited after 5 years.

--boundary
Content-Disposition: form-data; name="photo"; filename="photo_family.png"
Content-Type: image/png

--boundary
Content-Disposition: form-data; name="user"
1

--boundary
Content-Disposition: form-data; name="album"
1

(binary data)
--boundary--
```

##### Ejemplo de respuesta exitosa

```http
HTTP/1.1 200 Ok
Content-Type: application/json

{
	"status": "success",
	"message": "Image uploaded successfully",
	"data": {
		"image": {
			"id": 1,
			"title": "First photo from the family album",
			"description": "Photo in which the entire family appears reunited after 5 years.",
			"image": "/uploads/images/photo_family.png",
			"upload_date": "2024-07-16T20:53:32.942827Z",
			"user": 1,
			"album": 1
		}
	}
}
```
