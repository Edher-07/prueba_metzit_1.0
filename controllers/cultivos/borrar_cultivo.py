import web
import sqlite3

render = web.template.render('views/cultivos', base='layout')


class BorrarCultivo:

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
            return render.borrar_cultivo(item, None)
        except Exception as error:
            print(f"ERROR BorrarCultivo 400: {error.args}")
            return "UPS, algo fallo"

    def POST(self, id_cultivo):
        conexion = None
        exito = False
        try:
            conexion = sqlite3.connect("sql/metzit.db")
            cursor = conexion.cursor()
            query = "DELETE FROM cultivos WHERE id_cultivo = ?"
            cursor.execute(query, (id_cultivo,))
            conexion.commit()
            exito = True
        except sqlite3.Error as error:
            print(f"ERROR BorrarCultivo 401: {error.args}")
        except Exception as error:
            print(f"ERROR BorrarCultivo 402: {error.args}")
        finally:
            if conexion:
                conexion.close()

        if exito:
            raise web.seeother('/lista_cultivos')
        else:
            item = self.consultarCultivo(id_cultivo)
            return render.borrar_cultivo(item, "No se pudo borrar el registro")
