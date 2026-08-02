import web
import sqlite3

render = web.template.render('views/turnos_riego', base='layout')


class BorrarTurno:

    def consultarTurno(self, id_turno):
        conexion = None
        try:
            conexion = sqlite3.connect("sql/metzit.db")
            conexion.row_factory = sqlite3.Row
            cursor = conexion.cursor()
            query = "SELECT * FROM turnos_riego WHERE id_turno = ?;"
            cursor.execute(query, (id_turno,))
            fila = cursor.fetchone()
            if fila is None:
                return {}
            item = {
                "id_turno": fila[0],
                "fecha": fila[1],
                "hora_inicio": fila[2],
                "hora_fin": fila[3],
                "id_area": fila[4],
                "estado": fila[5],
            }
            return item
        except sqlite3.Error as error:
            print(f"ERROR Turno 400: {error.args}")
            return {}
        except Exception as error:
            print(f"ERROR Turno 401: {error.args}")
            return {}
        finally:
            if conexion:
                conexion.close()

    def GET(self, id_turno):
        try:
            item = self.consultarTurno(id_turno)
            return render.borrar_turno(item, None)
        except Exception as error:
            print(f"ERROR BorrarTurno 400: {error.args}")
            return "UPS, algo fallo"

    def POST(self, id_turno):
        conexion = None
        exito = False
        try:
            conexion = sqlite3.connect("sql/metzit.db")
            cursor = conexion.cursor()
            query = "DELETE FROM turnos_riego WHERE id_turno = ?"
            cursor.execute(query, (id_turno,))
            conexion.commit()
            exito = True
        except sqlite3.Error as error:
            print(f"ERROR BorrarTurno 401: {error.args}")
        except Exception as error:
            print(f"ERROR BorrarTurno 402: {error.args}")
        finally:
            if conexion:
                conexion.close()

        if exito:
            raise web.seeother('/lista_turnos_riego')
        else:
            item = self.consultarTurno(id_turno)
            return render.borrar_turno(item, "No se pudo borrar el registro")
