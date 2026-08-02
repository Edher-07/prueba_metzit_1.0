import web
import sqlite3

render = web.template.render('views/area_riego', base='layout')


class BorrarArea:

    def consultarArea(self, id_area):
        conexion = None
        try:
            conexion = sqlite3.connect("sql/metzit.db")
            conexion.row_factory = sqlite3.Row
            cursor = conexion.cursor()
            query = "SELECT * FROM area_riego WHERE id_area = ?;"
            cursor.execute(query, (id_area,))
            fila = cursor.fetchone()
            if fila is None:
                return {}
            item = {
                "id_area": fila[0],
                "nombre": fila[1],
                "suficiente": fila[2],
                "ubicacion": fila[3],
            }
            return item
        except sqlite3.Error as error:
            print(f"ERROR Area 400: {error.args}")
            return {}
        except Exception as error:
            print(f"ERROR Area 401: {error.args}")
            return {}
        finally:
            if conexion:
                conexion.close()

    def GET(self, id_area):
        try:
            item = self.consultarArea(id_area)
            return render.borrar_area(item, None)
        except Exception as error:
            print(f"ERROR BorrarArea 400: {error.args}")
            return "UPS, algo fallo"

    def POST(self, id_area):
        conexion = None
        exito = False
        try:
            conexion = sqlite3.connect("sql/metzit.db")
            cursor = conexion.cursor()
            query = "DELETE FROM area_riego WHERE id_area = ?"
            cursor.execute(query, (id_area,))
            conexion.commit()
            exito = True
        except sqlite3.Error as error:
            print(f"ERROR BorrarArea 401: {error.args}")
        except Exception as error:
            print(f"ERROR BorrarArea 402: {error.args}")
        finally:
            if conexion:
                conexion.close()

        if exito:
            raise web.seeother('/lista_area_riego')
        else:
            item = self.consultarArea(id_area)
            return render.borrar_area(item, "No se pudo borrar el registro")
