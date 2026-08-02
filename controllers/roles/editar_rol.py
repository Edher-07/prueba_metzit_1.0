import web
import sqlite3

render = web.template.render('views/roles', base='layout')


class EditarRol:

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
            if item == {}:
                return render.editar_rol(None)
            return render.editar_rol(item)
        except Exception as error:
            print(f"ERROR EditarRol 400: {error.args}")
            return "UPS, algo fallo"

    def POST(self, id_rol):
        conexion = None
        exito = False
        try:
            entrada = web.input()
            conexion = sqlite3.connect("sql/metzit.db")
            cursor = conexion.cursor()
            query = "UPDATE roles SET nombre_rol = ?, descripcion = ? WHERE id_rol = ?"
            cursor.execute(query, (entrada.get("nombre_rol"), entrada.get("descripcion"), id_rol))
            conexion.commit()
            exito = True
        except sqlite3.Error as error:
            print(f"ERROR EditarRol 401: {error.args}")
        except Exception as error:
            print(f"ERROR EditarRol 402: {error.args}")
        finally:
            if conexion:
                conexion.close()

        if exito:
            raise web.seeother(f'/ver_rol/{id_rol}')
        else:
            return "UPS, algo fallo al editar"
