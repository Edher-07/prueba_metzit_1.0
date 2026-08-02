import web
import sqlite3

render = web.template.render('views/cultivos', base='layout')


class ListaCultivo:

    def consultarCultivo(self):
        conexion = None
        try:
            conexion = sqlite3.connect("sql/metzit.db")
            conexion.row_factory = sqlite3.Row
            cursor = conexion.cursor()
            query = "SELECT * FROM cultivos;"
            cursor.execute(query)
            resultado = cursor.fetchall()

            datos = []
            for fila in resultado:
                item = {
                    "id_cultivo": fila[0],
                    "nombre": fila[1],
                    "descripcion": fila[2],
                    "temporada": fila[3],
                    "recomendaciones": fila[4],
                    "caracteristicas": fila[5],
                }
                datos.append(item)
            return datos
        except sqlite3.Error as error:
            print(f"ERROR ListaCultivo 400: {error.args}")
            return []
        except Exception as error:
            print(f"ERROR ListaCultivo 401: {error.args}")
            return []
        finally:
            if conexion:
                conexion.close()

    def GET(self):
        try:
            datos = self.consultarCultivo()
            return render.lista_cultivos(datos)
        except Exception as error:
            print(f"ERROR ListaCultivo 402: {error.args}")
            return "UPS, algo fallo"
