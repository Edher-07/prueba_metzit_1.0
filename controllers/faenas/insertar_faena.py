import web
import sqlite3

render = web.template.render('views/faenas', base='layout')


class InsertarFaena:

    def GET(self):
        return render.insertar_faena()

    def POST(self):
        conexion = None
        exito = False
        try:
            entrada = web.input()
            conexion = sqlite3.connect("sql/metzit.db")
            cursor = conexion.cursor()
            query = "INSERT INTO faenas(id_usuario, descripcion, fecha, hora, limite_fecha, multa) VALUES (?, ?, ?, ?, ?, ?)"
            cursor.execute(query, (entrada.get("id_usuario"), entrada.get("descripcion"), entrada.get("fecha"), entrada.get("hora"), entrada.get("limite_fecha"), entrada.get("multa")))
            conexion.commit()
            exito = True
        except sqlite3.Error as error:
            print(f"ERROR InsertarFaena 400: {error.args}")
        except Exception as error:
            print(f"ERROR InsertarFaena 401: {error.args}")
        finally:
            if conexion:
                conexion.close()

        if exito:
            raise web.seeother('/lista_faenas')
        else:
            return "UPS, algo fallo al insertar"
