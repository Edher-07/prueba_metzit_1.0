import web
import sqlite3

render = web.template.render('views/cultivos', base='layout')


class EditarCultivo:

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
            if item == {}:
                return render.editar_cultivo(None)
            return render.editar_cultivo(item)
        except Exception as error:
            print(f"ERROR EditarCultivo 400: {error.args}")
            return "UPS, algo fallo"

    def POST(self, id_cultivo):
        conexion = None
        exito = False
        try:
            entrada = web.input()
            conexion = sqlite3.connect("sql/metzit.db")
            cursor = conexion.cursor()
            query = "UPDATE cultivos SET nombre = ?, descripcion = ?, temporada = ?, recomendaciones = ?, caracteristicas = ? WHERE id_cultivo = ?"
            cursor.execute(query, (entrada.get("nombre"), entrada.get("descripcion"), entrada.get("temporada"), entrada.get("recomendaciones"), entrada.get("caracteristicas"), id_cultivo))
            conexion.commit()
            exito = True
        except sqlite3.Error as error:
            print(f"ERROR EditarCultivo 401: {error.args}")
        except Exception as error:
            print(f"ERROR EditarCultivo 402: {error.args}")
        finally:
            if conexion:
                conexion.close()

        if exito:
            raise web.seeother(f'/ver_cultivo/{id_cultivo}')
        else:
            return "UPS, algo fallo al editar"
