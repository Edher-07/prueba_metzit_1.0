import web
import sqlite3

render = web.template.render('views/area_riego', base='layout')


class InsertarArea:

    def GET(self):
        return render.insertar_area()

    def POST(self):
        conexion = None
        exito = False
        try:
            entrada = web.input()
            conexion = sqlite3.connect("sql/metzit.db")
            cursor = conexion.cursor()
            query = "INSERT INTO area_riego(nombre, suficiente, ubicacion) VALUES (?, ?, ?)"
            cursor.execute(query, (entrada.get("nombre"), entrada.get("suficiente"), entrada.get("ubicacion")))
            conexion.commit()
            exito = True
        except sqlite3.Error as error:
            print(f"ERROR InsertarArea 400: {error.args}")
        except Exception as error:
            print(f"ERROR InsertarArea 401: {error.args}")
        finally:
            if conexion:
                conexion.close()

        if exito:
            raise web.seeother('/lista_area_riego')
        else:
            return "UPS, algo fallo al insertar"
