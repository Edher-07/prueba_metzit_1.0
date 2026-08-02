import web
import sqlite3

render = web.template.render('views/participantes', base='layout')


class VerParticipante:

    def consultarParticipante(self, id_participante):
        conexion = None
        try:
            conexion = sqlite3.connect("sql/metzit.db")
            conexion.row_factory = sqlite3.Row
            cursor = conexion.cursor()
            query = "SELECT * FROM participantes WHERE id_participante = ?;"
            cursor.execute(query, (id_participante,))
            fila = cursor.fetchone()
            if fila is None:
                return {}
            item = {
                "id_participante": fila[0],
                "id_usuario": fila[1],
                "id_faena": fila[2],
                "asistencia": fila[3],
                "representante": fila[4],
                "multa_aplicada": fila[5],
                "observaciones": fila[6],
            }
            return item
        except sqlite3.Error as error:
            print(f"ERROR Participante 400: {error.args}")
            return {}
        except Exception as error:
            print(f"ERROR Participante 401: {error.args}")
            return {}
        finally:
            if conexion:
                conexion.close()

    def GET(self, id_participante):
        try:
            item = self.consultarParticipante(id_participante)
            return render.ver_participante(item)
        except Exception as error:
            print(f"ERROR VerParticipante 402: {error.args}")
            return "UPS, algo fallo"
