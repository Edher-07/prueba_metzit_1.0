import web
import sqlite3

render = web.template.render('views/participantes', base='layout')


class InsertarParticipante:

    def GET(self):
        return render.insertar_participante()

    def POST(self):
        conexion = None
        exito = False
        try:
            entrada = web.input()
            conexion = sqlite3.connect("sql/metzit.db")
            cursor = conexion.cursor()
            query = "INSERT INTO participantes(id_usuario, id_faena, asistencia, representante, multa_aplicada, observaciones) VALUES (?, ?, ?, ?, ?, ?)"
            cursor.execute(query, (entrada.get("id_usuario"), entrada.get("id_faena"), entrada.get("asistencia"), entrada.get("representante"), entrada.get("multa_aplicada"), entrada.get("observaciones")))
            conexion.commit()
            exito = True
        except sqlite3.Error as error:
            print(f"ERROR InsertarParticipante 400: {error.args}")
        except Exception as error:
            print(f"ERROR InsertarParticipante 401: {error.args}")
        finally:
            if conexion:
                conexion.close()

        if exito:
            raise web.seeother('/lista_participantes')
        else:
            return "UPS, algo fallo al insertar"
