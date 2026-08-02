import web
import sqlite3

render = web.template.render('views/usuarios', base='layout')


class EditarUsuario:

    def consultarUsuario(self, id_usuario):
        conexion = None
        try:
            conexion = sqlite3.connect("sql/metzit.db")
            conexion.row_factory = sqlite3.Row
            cursor = conexion.cursor()
            query = "SELECT * FROM usuarios WHERE id_usuario = ?;"
            cursor.execute(query, (id_usuario,))
            fila = cursor.fetchone()
            if fila is None:
                return {}
            item = {
                "id_usuario": fila[0],
                "nombre": fila[1],
                "apellido_paterno": fila[2],
                "apellido_materno": fila[3],
                "direccion": fila[4],
                "telefono": fila[5],
                "correo": fila[6],
                "contrasena": fila[7],
                "estado": fila[8],
                "id_rol": fila[9],
            }
            return item
        except sqlite3.Error as error:
            print(f"ERROR Usuario 400: {error.args}")
            return {}
        except Exception as error:
            print(f"ERROR Usuario 401: {error.args}")
            return {}
        finally:
            if conexion:
                conexion.close()

    def GET(self, id_usuario):
        try:
            item = self.consultarUsuario(id_usuario)
            if item == {}:
                return render.editar_usuario(None)
            return render.editar_usuario(item)
        except Exception as error:
            print(f"ERROR EditarUsuario 400: {error.args}")
            return "UPS, algo fallo"

    def POST(self, id_usuario):
        conexion = None
        exito = False
        try:
            entrada = web.input()
            conexion = sqlite3.connect("sql/metzit.db")
            cursor = conexion.cursor()
            query = "UPDATE usuarios SET nombre = ?, apellido_paterno = ?, apellido_materno = ?, direccion = ?, telefono = ?, correo = ?, contrasena = ?, estado = ?, id_rol = ? WHERE id_usuario = ?"
            cursor.execute(query, (entrada.get("nombre"), entrada.get("apellido_paterno"), entrada.get("apellido_materno"), entrada.get("direccion"), entrada.get("telefono"), entrada.get("correo"), entrada.get("contrasena"), entrada.get("estado"), entrada.get("id_rol"), id_usuario))
            conexion.commit()
            exito = True
        except sqlite3.Error as error:
            print(f"ERROR EditarUsuario 401: {error.args}")
        except Exception as error:
            print(f"ERROR EditarUsuario 402: {error.args}")
        finally:
            if conexion:
                conexion.close()

        if exito:
            raise web.seeother(f'/ver_usuario/{id_usuario}')
        else:
            return "UPS, algo fallo al editar"
