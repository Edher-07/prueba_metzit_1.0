import web
import sqlite3

render = web.template.render('views/publicaciones', base='layout')


class ListaPublicacion:

    def consultarPublicacion(self):
        conexion = None
        try:
            conexion = sqlite3.connect("sql/metzit.db")
            conexion.row_factory = sqlite3.Row
            cursor = conexion.cursor()
            query = "SELECT * FROM publicaciones;"
            cursor.execute(query)
            resultado = cursor.fetchall()

            datos = []
            for fila in resultado:
                item = {
                    "id_publicacion": fila[0],
                    "id_usuario": fila[1],
                    "titulo": fila[2],
                    "contenido": fila[3],
                    "categoria": fila[4],
                }
                datos.append(item)
            return datos
        except sqlite3.Error as error:
            print(f"ERROR ListaPublicacion 400: {error.args}")
            return []
        except Exception as error:
            print(f"ERROR ListaPublicacion 401: {error.args}")
            return []
        finally:
            if conexion:
                conexion.close()

    def GET(self):
        try:
            datos = self.consultarPublicacion()
            return render.lista_publicaciones(datos)
        except Exception as error:
            print(f"ERROR ListaPublicacion 402: {error.args}")
            return "UPS, algo fallo"
