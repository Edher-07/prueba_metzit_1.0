import web
import sqlite3

render = web.template.render('views/roles', base='layout')


class BorrarRol:

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
            return render.borrar_rol(item, None)
        except Exception as error:
            print(f"ERROR BorrarRol 400: {error.args}")
            return "UPS, algo fallo"

    def POST(self, id_rol):
        conexion = None
        exito = False
        try:
            conexion = sqlite3.connect("sql/metzit.db")
            cursor = conexion.cursor()
            query = "DELETE FROM roles WHERE id_rol = ?"
            cursor.execute(query, (id_rol,))
            conexion.commit()
            exito = True
        except sqlite3.Error as error:
            print(f"ERROR BorrarRol 401: {error.args}")
        except Exception as error:
            print(f"ERROR BorrarRol 402: {error.args}")
        finally:
            if conexion:
                conexion.close()

        if exito:
            raise web.seeother('/lista_roles')
        else:
            item = self.consultarRol(id_rol)
            return render.borrar_rol(item, "No se pudo borrar el registro")
