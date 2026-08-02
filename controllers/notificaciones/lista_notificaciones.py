import web
import sqlite3

render = web.template.render('views/notificaciones', base='layout')


class ListaNotificacion:

    def consultarNotificacion(self):
        conexion = None
        try:
            conexion = sqlite3.connect("sql/metzit.db")
            conexion.row_factory = sqlite3.Row
            cursor = conexion.cursor()
            query = "SELECT * FROM notificaciones;"
            cursor.execute(query)
            resultado = cursor.fetchall()

            datos = []
            for fila in resultado:
                item = {
                    "id_notificacion": fila[0],
                    "id_usuario": fila[1],
                    "titulo": fila[2],
                    "mensaje": fila[3],
                    "leida": fila[4],
                }
                datos.append(item)
            return datos
        except sqlite3.Error as error:
            print(f"ERROR ListaNotificacion 400: {error.args}")
            return []
        except Exception as error:
            print(f"ERROR ListaNotificacion 401: {error.args}")
            return []
        finally:
            if conexion:
                conexion.close()

    def GET(self):
        try:
            datos = self.consultarNotificacion()
            return render.lista_notificaciones(datos)
        except Exception as error:
            print(f"ERROR ListaNotificacion 402: {error.args}")
            return "UPS, algo fallo"
