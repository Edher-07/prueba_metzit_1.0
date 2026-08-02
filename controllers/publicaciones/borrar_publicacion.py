import web
import sqlite3

render = web.template.render('views/publicaciones', base='layout')


class BorrarPublicacion:

    def consultarPublicacion(self, id_publicacion):
        conexion = None
        try:
            conexion = sqlite3.connect("sql/metzit.db")
            conexion.row_factory = sqlite3.Row
            cursor = conexion.cursor()
            query = "SELECT * FROM publicaciones WHERE id_publicacion = ?;"
            cursor.execute(query, (id_publicacion,))
            fila = cursor.fetchone()
            if fila is None:
                return {}
            item = {
                "id_publicacion": fila[0],
                "id_usuario": fila[1],
                "titulo": fila[2],
                "contenido": fila[3],
                "categoria": fila[4],
            }
            return item
        except sqlite3.Error as error:
            print(f"ERROR Publicacion 400: {error.args}")
            return {}
        except Exception as error:
            print(f"ERROR Publicacion 401: {error.args}")
            return {}
        finally:
            if conexion:
                conexion.close()

    def GET(self, id_publicacion):
        try:
            item = self.consultarPublicacion(id_publicacion)
            return render.borrar_publicacion(item, None)
        except Exception as error:
            print(f"ERROR BorrarPublicacion 400: {error.args}")
            return "UPS, algo fallo"

    def POST(self, id_publicacion):
        conexion = None
        exito = False
        try:
            conexion = sqlite3.connect("sql/metzit.db")
            cursor = conexion.cursor()
            query = "DELETE FROM publicaciones WHERE id_publicacion = ?"
            cursor.execute(query, (id_publicacion,))
            conexion.commit()
            exito = True
        except sqlite3.Error as error:
            print(f"ERROR BorrarPublicacion 401: {error.args}")
        except Exception as error:
            print(f"ERROR BorrarPublicacion 402: {error.args}")
        finally:
            if conexion:
                conexion.close()

        if exito:
            raise web.seeother('/lista_publicaciones')
        else:
            item = self.consultarPublicacion(id_publicacion)
            return render.borrar_publicacion(item, "No se pudo borrar el registro")
