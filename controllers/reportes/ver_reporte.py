import web
import sqlite3

render = web.template.render('views/reportes', base='layout')


class VerReporte:

    def consultarReporte(self, id_reporte):
        conexion = None
        try:
            conexion = sqlite3.connect("sql/metzit.db")
            conexion.row_factory = sqlite3.Row
            cursor = conexion.cursor()
            query = "SELECT * FROM reportes WHERE id_reporte = ?;"
            cursor.execute(query, (id_reporte,))
            fila = cursor.fetchone()
            if fila is None:
                return {}
            item = {
                "id_reporte": fila[0],
                "id_usuario": fila[1],
                "titulo": fila[2],
                "descripcion": fila[3],
                "estado": fila[4],
            }
            return item
        except sqlite3.Error as error:
            print(f"ERROR Reporte 400: {error.args}")
            return {}
        except Exception as error:
            print(f"ERROR Reporte 401: {error.args}")
            return {}
        finally:
            if conexion:
                conexion.close()

    def GET(self, id_reporte):
        try:
            item = self.consultarReporte(id_reporte)
            return render.ver_reporte(item)
        except Exception as error:
            print(f"ERROR VerReporte 402: {error.args}")
            return "UPS, algo fallo"
