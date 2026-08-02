import web
import sqlite3

render = web.template.render('views/reportes', base='layout')


class InsertarReporte:

    def GET(self):
        return render.insertar_reporte()

    def POST(self):
        conexion = None
        exito = False
        try:
            entrada = web.input()
            conexion = sqlite3.connect("sql/metzit.db")
            cursor = conexion.cursor()
            query = "INSERT INTO reportes(id_usuario, titulo, descripcion, estado) VALUES (?, ?, ?, ?)"
            cursor.execute(query, (entrada.get("id_usuario"), entrada.get("titulo"), entrada.get("descripcion"), entrada.get("estado")))
            conexion.commit()
            exito = True
        except sqlite3.Error as error:
            print(f"ERROR InsertarReporte 400: {error.args}")
        except Exception as error:
            print(f"ERROR InsertarReporte 401: {error.args}")
        finally:
            if conexion:
                conexion.close()

        if exito:
            raise web.seeother('/lista_reportes')
        else:
            return "UPS, algo fallo al insertar"
