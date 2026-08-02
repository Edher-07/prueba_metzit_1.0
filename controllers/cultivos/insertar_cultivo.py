import web
import sqlite3

render = web.template.render('views/cultivos', base='layout')


class InsertarCultivo:

    def GET(self):
        return render.insertar_cultivo()

    def POST(self):
        conexion = None
        exito = False
        try:
            entrada = web.input()
            conexion = sqlite3.connect("sql/metzit.db")
            cursor = conexion.cursor()
            query = "INSERT INTO cultivos(nombre, descripcion, temporada, recomendaciones, caracteristicas) VALUES (?, ?, ?, ?, ?)"
            cursor.execute(query, (entrada.get("nombre"), entrada.get("descripcion"), entrada.get("temporada"), entrada.get("recomendaciones"), entrada.get("caracteristicas")))
            conexion.commit()
            exito = True
        except sqlite3.Error as error:
            print(f"ERROR InsertarCultivo 400: {error.args}")
        except Exception as error:
            print(f"ERROR InsertarCultivo 401: {error.args}")
        finally:
            if conexion:
                conexion.close()

        if exito:
            raise web.seeother('/lista_cultivos')
        else:
            return "UPS, algo fallo al insertar"
