import web
import sqlite3

render = web.template.render('views/area_riego', base='layout')


class EditarArea:

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
            if item == {}:
                return render.editar_area(None)
            return render.editar_area(item)
        except Exception as error:
            print(f"ERROR EditarArea 400: {error.args}")
            return "UPS, algo fallo"

    def POST(self, id_area):
        conexion = None
        exito = False
        try:
            entrada = web.input()
            conexion = sqlite3.connect("sql/metzit.db")
            cursor = conexion.cursor()
            query = "UPDATE area_riego SET nombre = ?, suficiente = ?, ubicacion = ? WHERE id_area = ?"
            cursor.execute(query, (entrada.get("nombre"), entrada.get("suficiente"), entrada.get("ubicacion"), id_area))
            conexion.commit()
            exito = True
        except sqlite3.Error as error:
            print(f"ERROR EditarArea 401: {error.args}")
        except Exception as error:
            print(f"ERROR EditarArea 402: {error.args}")
        finally:
            if conexion:
                conexion.close()

        if exito:
            raise web.seeother(f'/ver_area/{id_area}')
        else:
            return "UPS, algo fallo al editar"
