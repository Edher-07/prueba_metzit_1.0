import web
import sqlite3

render = web.template.render('views/roles', base='layout')


class InsertarRol:

    def GET(self):
        return render.insertar_rol()

    def POST(self):
        conexion = None
        exito = False
        try:
            entrada = web.input()
            conexion = sqlite3.connect("sql/metzit.db")
            cursor = conexion.cursor()
            query = "INSERT INTO roles(nombre_rol, descripcion) VALUES (?, ?)"
            cursor.execute(query, (entrada.get("nombre_rol"), entrada.get("descripcion")))
            conexion.commit()
            exito = True
        except sqlite3.Error as error:
            print(f"ERROR InsertarRol 400: {error.args}")
        except Exception as error:
            print(f"ERROR InsertarRol 401: {error.args}")
        finally:
            if conexion:
                conexion.close()

        if exito:
            raise web.seeother('/lista_roles')
        else:
            return "UPS, algo fallo al insertar"
