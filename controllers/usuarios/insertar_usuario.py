import web
import sqlite3

render = web.template.render('views/usuarios', base='layout')


class InsertarUsuario:

    def GET(self):
        return render.insertar_usuario()

    def POST(self):
        conexion = None
        exito = False
        try:
            entrada = web.input()
            conexion = sqlite3.connect("sql/metzit.db")
            cursor = conexion.cursor()
            query = "INSERT INTO usuarios(nombre, apellido_paterno, apellido_materno, direccion, telefono, correo, contrasena, estado, id_rol) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)"
            cursor.execute(query, (entrada.get("nombre"), entrada.get("apellido_paterno"), entrada.get("apellido_materno"), entrada.get("direccion"), entrada.get("telefono"), entrada.get("correo"), entrada.get("contrasena"), entrada.get("estado"), entrada.get("id_rol")))
            conexion.commit()
            exito = True
        except sqlite3.Error as error:
            print(f"ERROR InsertarUsuario 400: {error.args}")
        except Exception as error:
            print(f"ERROR InsertarUsuario 401: {error.args}")
        finally:
            if conexion:
                conexion.close()

        if exito:
            raise web.seeother('/lista_usuarios')
        else:
            return "UPS, algo fallo al insertar"
