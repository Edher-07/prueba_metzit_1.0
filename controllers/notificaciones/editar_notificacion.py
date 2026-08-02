import web
import sqlite3

render = web.template.render('views/notificaciones', base='layout')


class EditarNotificacion:

    def consultarNotificacion(self, id_notificacion):
        conexion = None
        try:
            conexion = sqlite3.connect("sql/metzit.db")
            conexion.row_factory = sqlite3.Row
            cursor = conexion.cursor()
            query = "SELECT * FROM notificaciones WHERE id_notificacion = ?;"
            cursor.execute(query, (id_notificacion,))
            fila = cursor.fetchone()
            if fila is None:
                return {}
            item = {
                "id_notificacion": fila[0],
                "id_usuario": fila[1],
                "titulo": fila[2],
                "mensaje": fila[3],
                "leida": fila[4],
            }
            return item
        except sqlite3.Error as error:
            print(f"ERROR Notificacion 400: {error.args}")
            return {}
        except Exception as error:
            print(f"ERROR Notificacion 401: {error.args}")
            return {}
        finally:
            if conexion:
                conexion.close()

    def GET(self, id_notificacion):
        try:
            item = self.consultarNotificacion(id_notificacion)
            if item == {}:
                return render.editar_notificacion(None)
            return render.editar_notificacion(item)
        except Exception as error:
            print(f"ERROR EditarNotificacion 400: {error.args}")
            return "UPS, algo fallo"

    def POST(self, id_notificacion):
        conexion = None
        exito = False
        try:
            entrada = web.input()
            conexion = sqlite3.connect("sql/metzit.db")
            cursor = conexion.cursor()
            query = "UPDATE notificaciones SET id_usuario = ?, titulo = ?, mensaje = ?, leida = ? WHERE id_notificacion = ?"
            cursor.execute(query, (entrada.get("id_usuario"), entrada.get("titulo"), entrada.get("mensaje"), entrada.get("leida"), id_notificacion))
            conexion.commit()
            exito = True
        except sqlite3.Error as error:
            print(f"ERROR EditarNotificacion 401: {error.args}")
        except Exception as error:
            print(f"ERROR EditarNotificacion 402: {error.args}")
        finally:
            if conexion:
                conexion.close()

        if exito:
            raise web.seeother(f'/ver_notificacion/{id_notificacion}')
        else:
            return "UPS, algo fallo al editar"
