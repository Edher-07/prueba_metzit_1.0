import web
import sqlite3

render = web.template.render('views/turnos_riego', base='layout')


class InsertarTurno:

    def GET(self):
        return render.insertar_turno()

    def POST(self):
        conexion = None
        exito = False
        try:
            entrada = web.input()
            conexion = sqlite3.connect("sql/metzit.db")
            cursor = conexion.cursor()
            query = "INSERT INTO turnos_riego(fecha, hora_inicio, hora_fin, id_area, estado) VALUES (?, ?, ?, ?, ?)"
            cursor.execute(query, (entrada.get("fecha"), entrada.get("hora_inicio"), entrada.get("hora_fin"), entrada.get("id_area"), entrada.get("estado")))
            conexion.commit()
            exito = True
        except sqlite3.Error as error:
            print(f"ERROR InsertarTurno 400: {error.args}")
        except Exception as error:
            print(f"ERROR InsertarTurno 401: {error.args}")
        finally:
            if conexion:
                conexion.close()

        if exito:
            raise web.seeother('/lista_turnos_riego')
        else:
            return "UPS, algo fallo al insertar"
