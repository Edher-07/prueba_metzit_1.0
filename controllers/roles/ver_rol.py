import web
import sqlite3

render = web.template.render('views/roles', base='layout')


class VerRol:

    def consultarRol(self, id_rol):
        conexion = None
        try:
            conexion = sqlite3.connect("sql/metzit.db")
            conexion.row_factory = sqlite3.Row
            cursor = conexion.cursor()
            query = "SELECT * FROM roles WHERE id_rol = ?;"
            cursor.execute(query, (id_rol,))
            fila = cursor.fetchone()
            if fila is None:
                return {}
            item = {
                "id_rol": fila[0],
                "nombre_rol": fila[1],
                "descripcion": fila[2],
            }
            return item
        except sqlite3.Error as error:
            print(f"ERROR Rol 400: {error.args}")
            return {}
        except Exception as error:
            print(f"ERROR Rol 401: {error.args}")
            return {}
        finally:
            if conexion:
                conexion.close()

    def GET(self, id_rol):
        try:
            item = self.consultarRol(id_rol)
            return render.ver_rol(item)
        except Exception as error:
            print(f"ERROR VerRol 402: {error.args}")
            return "UPS, algo fallo"
