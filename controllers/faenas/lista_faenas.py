import web
import sqlite3

render = web.template.render('views/faenas', base='layout')


class ListaFaena:

    def consultarFaena(self):
        conexion = None
        try:
            conexion = sqlite3.connect("sql/metzit.db")
            conexion.row_factory = sqlite3.Row
            cursor = conexion.cursor()
            query = "SELECT * FROM faenas;"
            cursor.execute(query)
            resultado = cursor.fetchall()

            datos = []
            for fila in resultado:
                item = {
                    "id_faena": fila[0],
                    "id_usuario": fila[1],
                    "descripcion": fila[2],
                    "fecha": fila[3],
                    "hora": fila[4],
                    "limite_fecha": fila[5],
                    "multa": fila[6],
                }
                datos.append(item)
            return datos
        except sqlite3.Error as error:
            print(f"ERROR ListaFaena 400: {error.args}")
            return []
        except Exception as error:
            print(f"ERROR ListaFaena 401: {error.args}")
            return []
        finally:
            if conexion:
                conexion.close()

    def GET(self):
        try:
            datos = self.consultarFaena()
            return render.lista_faenas(datos)
        except Exception as error:
            print(f"ERROR ListaFaena 402: {error.args}")
            return "UPS, algo fallo"
