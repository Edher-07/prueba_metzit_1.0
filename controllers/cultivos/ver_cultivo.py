import web
import sqlite3

render = web.template.render('views/cultivos', base='layout')


class VerCultivo:

    def consultarCultivo(self, id_cultivo):
        conexion = None
        try:
            conexion = sqlite3.connect("sql/metzit.db")
            conexion.row_factory = sqlite3.Row
            cursor = conexion.cursor()
            query = "SELECT * FROM cultivos WHERE id_cultivo = ?;"
            cursor.execute(query, (id_cultivo,))
            fila = cursor.fetchone()
            if fila is None:
                return {}
            item = {
                "id_cultivo": fila[0],
                "nombre": fila[1],
                "descripcion": fila[2],
                "temporada": fila[3],
                "recomendaciones": fila[4],
                "caracteristicas": fila[5],
            }
            return item
        except sqlite3.Error as error:
            print(f"ERROR Cultivo 400: {error.args}")
            return {}
        except Exception as error:
            print(f"ERROR Cultivo 401: {error.args}")
            return {}
        finally:
            if conexion:
                conexion.close()

    def GET(self, id_cultivo):
        try:
            item = self.consultarCultivo(id_cultivo)
            return render.ver_cultivo(item)
        except Exception as error:
            print(f"ERROR VerCultivo 402: {error.args}")
            return "UPS, algo fallo"
