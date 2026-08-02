import web
import sqlite3

render = web.template.render('views/publicaciones', base='layout')


class InsertarPublicacion:

    def GET(self):
        return render.insertar_publicacion()

    def POST(self):
        conexion = None
        exito = False
        try:
            entrada = web.input()
            conexion = sqlite3.connect("sql/metzit.db")
            cursor = conexion.cursor()
            query = "INSERT INTO publicaciones(id_usuario, titulo, contenido, categoria) VALUES (?, ?, ?, ?)"
            cursor.execute(query, (entrada.get("id_usuario"), entrada.get("titulo"), entrada.get("contenido"), entrada.get("categoria")))
            conexion.commit()
            exito = True
        except sqlite3.Error as error:
            print(f"ERROR InsertarPublicacion 400: {error.args}")
        except Exception as error:
            print(f"ERROR InsertarPublicacion 401: {error.args}")
        finally:
            if conexion:
                conexion.close()

        if exito:
            raise web.seeother('/lista_publicaciones')
        else:
            return "UPS, algo fallo al insertar"
