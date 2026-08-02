# Metzit — Agua y Pueblo 💧

Aplicación web para la gestión del agua de riego en la comunidad de **San Bartolo (La Barranca)**,
municipio de Acatlán, Hidalgo. Desarrollada como prototipo funcional con fines académicos
(Tecnologías de la Información e Innovación Digital — UT Tulancingo).

Este repositorio sigue la misma arquitectura y convenciones del proyecto de referencia
(`agenda_tic31`): **web.py** + **SQLite** + patrón `controllers/` (lógica) y `views/` (plantillas
Templetor), un archivo por acción.

## Estructura del proyecto

```
metzit/
├── app.py                     # Rutas (urls) de toda la aplicación
├── controllers/
│   ├── index.py                # Página de inicio
│   ├── usuarios/                # lista_, insertar_, ver_, editar_, borrar_ usuario.py
│   ├── roles/
│   ├── area_riego/
│   ├── turnos_riego/
│   ├── cultivos/
│   ├── publicaciones/
│   ├── reportes/
│   ├── faenas/
│   ├── participantes/
│   └── notificaciones/
├── views/
│   ├── layout.html              # Layout general (navbar + Bootstrap)
│   ├── index.html
│   └── <mismo_modulo_que_arriba>/   # cada módulo tiene su layout.html + 5 vistas .html
├── sql/
│   ├── script.sql               # CREATE TABLE + datos de prueba (10 tablas)
│   ├── reset.sh                 # Recrea sql/metzit.db desde cero
│   └── metzit.db                # Base de datos SQLite ya generada (demo)
├── requirements.txt
├── runtime.txt
└── .gitignore
```

Cada módulo (`usuarios`, `roles`, `turnos_riego`, `area_riego`, `cultivos`, `publicaciones`,
`reportes`, `faenas`, `participantes`, `notificaciones`) implementa **CRUD completo**:

| Acción   | Controlador                     | Ruta                          |
|----------|----------------------------------|-------------------------------|
| Listar   | `lista_<modulo>.py`             | `/lista_<modulo>`             |
| Insertar | `insertar_<entidad>.py`         | `/insertar_<entidad>` (GET/POST) |
| Ver      | `ver_<entidad>.py`              | `/ver_<entidad>/<id>`         |
| Editar   | `editar_<entidad>.py`           | `/editar_<entidad>/<id>` (GET/POST) |
| Borrar   | `borrar_<entidad>.py`           | `/borrar_<entidad>/<id>` (GET/POST) |

Este código se generó a partir del **diagrama entidad-relación y el diccionario de datos**
del documento `Base_de_datos_agua.pdf`, y de los **requerimientos funcionales** de
`OFICIAL.pdf` (registro de usuarios, gestión de turnos de riego, notificaciones,
publicaciones/reportes comunitarios, consulta de cultivos y registro de faenas).

> Tómalo como **punto de partida**: los controladores ya validan errores de SQL, cierran la
> conexión en `finally` y redirigen tras insertar/editar/borrar, pero conviene reforzar validaciones
> de formulario, hashing de contraseñas y control de sesión antes de un uso real.

## Requisitos

- Python 3.10+
- `pip install web.py`

## Instalación y ejecución local

```bash
git clone https://github.com/<tu-usuario>/metzit.git
cd metzit
python3 -m venv venv
source venv/bin/activate      # En Windows: venv\Scripts\activate
pip install -r requirements.txt

# (Opcional) regenerar la base de datos de ejemplo
bash sql/reset.sh

# Levantar el servidor
python3 app.py 8080
```

Abre `http://localhost:8080` en tu navegador.

## Base de datos

El esquema (`sql/script.sql`) implementa las 10 entidades del diagrama E-R:
`roles`, `usuarios`, `area_riego`, `turnos_riego`, `cultivos`, `publicaciones`, `reportes`,
`faenas`, `participantes` y `notificaciones`, respetando las relaciones 1:1, 1:N y N:M descritas
en el documento (incluye la tabla intermedia `area_cultivo` para la relación N:M entre
Área de Riego y Cultivos).

Para reiniciar la base de datos desde cero:

```bash
bash sql/reset.sh
```

## Cómo subirlo a GitHub

```bash
cd metzit
git init
git add .
git commit -m "CREATE proyecto Metzit: estructura inicial CRUD (10 módulos)"
git branch -M main
git remote add origin https://github.com/<tu-usuario>/metzit.git
git push -u origin main
```

Sugerencia de flujo de trabajo (igual al que se ve en el historial del repo de referencia):
mensajes de commit cortos y en mayúsculas al inicio (`CREATE`, `UPDATE`, `FIXED`) que describan
el módulo afectado, por ejemplo:

```
CREATE módulo turnos_riego funcional
UPDATE manejo de errores en usuarios
FIXED borrar faena con participantes asignados
```

## Próximos pasos sugeridos

- Agregar inicio de sesión (`RF02`) con sesiones de `web.py` (`web.session`) y hash de
  contraseñas (p. ej. `bcrypt`), restringiendo acciones según el rol (`Administrador`,
  `Comisariado`, `Usuario`).
- Convertir los campos `id_usuario`, `id_rol`, `id_area`, `id_faena` de los formularios en
  `<select>` con los nombres reales en vez de capturarlos como número.
- Envío real de notificaciones (correo/SMS) para `RF05`.
- Migrar de SQLite a PostgreSQL para producción, tal como lo especifica el documento de
  requisitos (`OFICIAL.pdf`).
