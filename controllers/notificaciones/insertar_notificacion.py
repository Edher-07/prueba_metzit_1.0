import web
import sqlite3

render = web.template.render('views/notificaciones', base='layout')


class InsertarNotificacion:

    def GET(self):
        return render.insertar_notificacion()

    def POST(self):
        conexion = None
        exito = False
        try:
            entrada = web.input()
            conexion = sqlite3.connect("sql/metzit.db")
            cursor = conexion.cursor()
            query = "INSERT INTO notificaciones(id_usuario, titulo, mensaje, leida) VALUES (?, ?, ?, ?)"
            cursor.execute(query, (entrada.get("id_usuario"), entrada.get("titulo"), entrada.get("mensaje"), entrada.get("leida")))
            conexion.commit()
            exito = True
        except sqlite3.Error as error:
            print(f"ERROR InsertarNotificacion 400: {error.args}")
        except Exception as error:
            print(f"ERROR InsertarNotificacion 401: {error.args}")
        finally:
            if conexion:
                conexion.close()

        if exito:
            raise web.seeother('/lista_notificaciones')
        else:
            return "UPS, algo fallo al insertar"
