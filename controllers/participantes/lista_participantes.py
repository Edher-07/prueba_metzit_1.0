import web
import sqlite3

render = web.template.render('views/participantes', base='layout')


class ListaParticipante:

    def consultarParticipante(self):
        conexion = None
        try:
            conexion = sqlite3.connect("sql/metzit.db")
            conexion.row_factory = sqlite3.Row
            cursor = conexion.cursor()
            query = "SELECT * FROM participantes;"
            cursor.execute(query)
            resultado = cursor.fetchall()

            datos = []
            for fila in resultado:
                item = {
                    "id_participante": fila[0],
                    "id_usuario": fila[1],
                    "id_faena": fila[2],
                    "asistencia": fila[3],
                    "representante": fila[4],
                    "multa_aplicada": fila[5],
                    "observaciones": fila[6],
                }
                datos.append(item)
            return datos
        except sqlite3.Error as error:
            print(f"ERROR ListaParticipante 400: {error.args}")
            return []
        except Exception as error:
            print(f"ERROR ListaParticipante 401: {error.args}")
            return []
        finally:
            if conexion:
                conexion.close()

    def GET(self):
        try:
            datos = self.consultarParticipante()
            return render.lista_participantes(datos)
        except Exception as error:
            print(f"ERROR ListaParticipante 402: {error.args}")
            return "UPS, algo fallo"
