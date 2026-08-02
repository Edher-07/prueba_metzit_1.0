import web
import sqlite3

render = web.template.render('views/area_riego', base='layout')


class ListaArea:

    def consultarArea(self):
        conexion = None
        try:
            conexion = sqlite3.connect("sql/metzit.db")
            conexion.row_factory = sqlite3.Row
            cursor = conexion.cursor()
            query = "SELECT * FROM area_riego;"
            cursor.execute(query)
            resultado = cursor.fetchall()

            datos = []
            for fila in resultado:
                item = {
                    "id_area": fila[0],
                    "nombre": fila[1],
                    "suficiente": fila[2],
                    "ubicacion": fila[3],
                }
                datos.append(item)
            return datos
        except sqlite3.Error as error:
            print(f"ERROR ListaArea 400: {error.args}")
            return []
        except Exception as error:
            print(f"ERROR ListaArea 401: {error.args}")
            return []
        finally:
            if conexion:
                conexion.close()

    def GET(self):
        try:
            datos = self.consultarArea()
            return render.lista_area_riego(datos)
        except Exception as error:
            print(f"ERROR ListaArea 402: {error.args}")
            return "UPS, algo fallo"
