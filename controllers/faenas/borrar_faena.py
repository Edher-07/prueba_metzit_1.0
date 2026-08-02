import web
import sqlite3

render = web.template.render('views/faenas', base='layout')


class BorrarFaena:

    def consultarFaena(self, id_faena):
        conexion = None
        try:
            conexion = sqlite3.connect("sql/metzit.db")
            conexion.row_factory = sqlite3.Row
            cursor = conexion.cursor()
            query = "SELECT * FROM faenas WHERE id_faena = ?;"
            cursor.execute(query, (id_faena,))
            fila = cursor.fetchone()
            if fila is None:
                return {}
            item = {
                "id_faena": fila[0],
                "id_usuario": fila[1],
                "descripcion": fila[2],
                "fecha": fila[3],
                "hora": fila[4],
                "limite_fecha": fila[5],
                "multa": fila[6],
            }
            return item
        except sqlite3.Error as error:
            print(f"ERROR Faena 400: {error.args}")
            return {}
        except Exception as error:
            print(f"ERROR Faena 401: {error.args}")
            return {}
        finally:
            if conexion:
                conexion.close()

    def GET(self, id_faena):
        try:
            item = self.consultarFaena(id_faena)
            return render.borrar_faena(item, None)
        except Exception as error:
            print(f"ERROR BorrarFaena 400: {error.args}")
            return "UPS, algo fallo"

    def POST(self, id_faena):
        conexion = None
        exito = False
        try:
            conexion = sqlite3.connect("sql/metzit.db")
            cursor = conexion.cursor()
            query = "DELETE FROM faenas WHERE id_faena = ?"
            cursor.execute(query, (id_faena,))
            conexion.commit()
            exito = True
        except sqlite3.Error as error:
            print(f"ERROR BorrarFaena 401: {error.args}")
        except Exception as error:
            print(f"ERROR BorrarFaena 402: {error.args}")
        finally:
            if conexion:
                conexion.close()

        if exito:
            raise web.seeother('/lista_faenas')
        else:
            item = self.consultarFaena(id_faena)
            return render.borrar_faena(item, "No se pudo borrar el registro")
