import web
import sqlite3

render = web.template.render('views/usuarios', base='layout')


class ListaUsuario:

    def consultarUsuario(self):
        conexion = None
        try:
            conexion = sqlite3.connect("sql/metzit.db")
            conexion.row_factory = sqlite3.Row
            cursor = conexion.cursor()
            query = "SELECT * FROM usuarios;"
            cursor.execute(query)
            resultado = cursor.fetchall()

            datos = []
            for fila in resultado:
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
                datos.append(item)
            return datos
        except sqlite3.Error as error:
            print(f"ERROR ListaUsuario 400: {error.args}")
            return []
        except Exception as error:
            print(f"ERROR ListaUsuario 401: {error.args}")
            return []
        finally:
            if conexion:
                conexion.close()

    def GET(self):
        try:
            datos = self.consultarUsuario()
            return render.lista_usuarios(datos)
        except Exception as error:
            print(f"ERROR ListaUsuario 402: {error.args}")
            return "UPS, algo fallo"
