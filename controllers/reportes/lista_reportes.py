import web
import sqlite3

render = web.template.render('views/reportes', base='layout')


class ListaReporte:

    def consultarReporte(self):
        conexion = None
        try:
            conexion = sqlite3.connect("sql/metzit.db")
            conexion.row_factory = sqlite3.Row
            cursor = conexion.cursor()
            query = "SELECT * FROM reportes;"
            cursor.execute(query)
            resultado = cursor.fetchall()

            datos = []
            for fila in resultado:
                item = {
                    "id_reporte": fila[0],
                    "id_usuario": fila[1],
                    "titulo": fila[2],
                    "descripcion": fila[3],
                    "estado": fila[4],
                }
                datos.append(item)
            return datos
        except sqlite3.Error as error:
            print(f"ERROR ListaReporte 400: {error.args}")
            return []
        except Exception as error:
            print(f"ERROR ListaReporte 401: {error.args}")
            return []
        finally:
            if conexion:
                conexion.close()

    def GET(self):
        try:
            datos = self.consultarReporte()
            return render.lista_reportes(datos)
        except Exception as error:
            print(f"ERROR ListaReporte 402: {error.args}")
            return "UPS, algo fallo"
