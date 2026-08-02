import web
import sqlite3

render = web.template.render('views/roles', base='layout')


class ListaRol:

    def consultarRol(self):
        conexion = None
        try:
            conexion = sqlite3.connect("sql/metzit.db")
            conexion.row_factory = sqlite3.Row
            cursor = conexion.cursor()
            query = "SELECT * FROM roles;"
            cursor.execute(query)
            resultado = cursor.fetchall()

            datos = []
            for fila in resultado:
                item = {
                    "id_rol": fila[0],
                    "nombre_rol": fila[1],
                    "descripcion": fila[2],
                }
                datos.append(item)
            return datos
        except sqlite3.Error as error:
            print(f"ERROR ListaRol 400: {error.args}")
            return []
        except Exception as error:
            print(f"ERROR ListaRol 401: {error.args}")
            return []
        finally:
            if conexion:
                conexion.close()

    def GET(self):
        try:
            datos = self.consultarRol()
            return render.lista_roles(datos)
        except Exception as error:
            print(f"ERROR ListaRol 402: {error.args}")
            return "UPS, algo fallo"
