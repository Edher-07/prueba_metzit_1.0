import web
import sqlite3

render = web.template.render('views/faenas', base='layout')


class EditarFaena:

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
            if item == {}:
                return render.editar_faena(None)
            return render.editar_faena(item)
        except Exception as error:
            print(f"ERROR EditarFaena 400: {error.args}")
            return "UPS, algo fallo"

    def POST(self, id_faena):
        conexion = None
        exito = False
        try:
            entrada = web.input()
            conexion = sqlite3.connect("sql/metzit.db")
            cursor = conexion.cursor()
            query = "UPDATE faenas SET id_usuario = ?, descripcion = ?, fecha = ?, hora = ?, limite_fecha = ?, multa = ? WHERE id_faena = ?"
            cursor.execute(query, (entrada.get("id_usuario"), entrada.get("descripcion"), entrada.get("fecha"), entrada.get("hora"), entrada.get("limite_fecha"), entrada.get("multa"), id_faena))
            conexion.commit()
            exito = True
        except sqlite3.Error as error:
            print(f"ERROR EditarFaena 401: {error.args}")
        except Exception as error:
            print(f"ERROR EditarFaena 402: {error.args}")
        finally:
            if conexion:
                conexion.close()

        if exito:
            raise web.seeother(f'/ver_faena/{id_faena}')
        else:
            return "UPS, algo fallo al editar"
