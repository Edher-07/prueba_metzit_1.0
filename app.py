import web

urls = (
    '/', 'controllers.index.Index',

    # ---------------- Roles ----------------
    '/lista_roles', 'controllers.roles.lista_roles.ListaRol',
    '/insertar_rol', 'controllers.roles.insertar_rol.InsertarRol',
    '/ver_rol/(.*)', 'controllers.roles.ver_rol.VerRol',
    '/editar_rol/(.*)', 'controllers.roles.editar_rol.EditarRol',
    '/borrar_rol/(.*)', 'controllers.roles.borrar_rol.BorrarRol',

    # ---------------- Usuarios ----------------
    '/lista_usuarios', 'controllers.usuarios.lista_usuarios.ListaUsuario',
    '/insertar_usuario', 'controllers.usuarios.insertar_usuario.InsertarUsuario',
    '/ver_usuario/(.*)', 'controllers.usuarios.ver_usuario.VerUsuario',
    '/editar_usuario/(.*)', 'controllers.usuarios.editar_usuario.EditarUsuario',
    '/borrar_usuario/(.*)', 'controllers.usuarios.borrar_usuario.BorrarUsuario',

    # ---------------- Área de riego ----------------
    '/lista_area_riego', 'controllers.area_riego.lista_area_riego.ListaArea',
    '/insertar_area', 'controllers.area_riego.insertar_area.InsertarArea',
    '/ver_area/(.*)', 'controllers.area_riego.ver_area.VerArea',
    '/editar_area/(.*)', 'controllers.area_riego.editar_area.EditarArea',
    '/borrar_area/(.*)', 'controllers.area_riego.borrar_area.BorrarArea',

    # ---------------- Turnos de riego ----------------
    '/lista_turnos_riego', 'controllers.turnos_riego.lista_turnos_riego.ListaTurno',
    '/insertar_turno', 'controllers.turnos_riego.insertar_turno.InsertarTurno',
    '/ver_turno/(.*)', 'controllers.turnos_riego.ver_turno.VerTurno',
    '/editar_turno/(.*)', 'controllers.turnos_riego.editar_turno.EditarTurno',
    '/borrar_turno/(.*)', 'controllers.turnos_riego.borrar_turno.BorrarTurno',

    # ---------------- Cultivos ----------------
    '/lista_cultivos', 'controllers.cultivos.lista_cultivos.ListaCultivo',
    '/insertar_cultivo', 'controllers.cultivos.insertar_cultivo.InsertarCultivo',
    '/ver_cultivo/(.*)', 'controllers.cultivos.ver_cultivo.VerCultivo',
    '/editar_cultivo/(.*)', 'controllers.cultivos.editar_cultivo.EditarCultivo',
    '/borrar_cultivo/(.*)', 'controllers.cultivos.borrar_cultivo.BorrarCultivo',

    # ---------------- Publicaciones ----------------
    '/lista_publicaciones', 'controllers.publicaciones.lista_publicaciones.ListaPublicacion',
    '/insertar_publicacion', 'controllers.publicaciones.insertar_publicacion.InsertarPublicacion',
    '/ver_publicacion/(.*)', 'controllers.publicaciones.ver_publicacion.VerPublicacion',
    '/editar_publicacion/(.*)', 'controllers.publicaciones.editar_publicacion.EditarPublicacion',
    '/borrar_publicacion/(.*)', 'controllers.publicaciones.borrar_publicacion.BorrarPublicacion',

    # ---------------- Reportes ----------------
    '/lista_reportes', 'controllers.reportes.lista_reportes.ListaReporte',
    '/insertar_reporte', 'controllers.reportes.insertar_reporte.InsertarReporte',
    '/ver_reporte/(.*)', 'controllers.reportes.ver_reporte.VerReporte',
    '/editar_reporte/(.*)', 'controllers.reportes.editar_reporte.EditarReporte',
    '/borrar_reporte/(.*)', 'controllers.reportes.borrar_reporte.BorrarReporte',

    # ---------------- Faenas ----------------
    '/lista_faenas', 'controllers.faenas.lista_faenas.ListaFaena',
    '/insertar_faena', 'controllers.faenas.insertar_faena.InsertarFaena',
    '/ver_faena/(.*)', 'controllers.faenas.ver_faena.VerFaena',
    '/editar_faena/(.*)', 'controllers.faenas.editar_faena.EditarFaena',
    '/borrar_faena/(.*)', 'controllers.faenas.borrar_faena.BorrarFaena',

    # ---------------- Participantes ----------------
    '/lista_participantes', 'controllers.participantes.lista_participantes.ListaParticipante',
    '/insertar_participante', 'controllers.participantes.insertar_participante.InsertarParticipante',
    '/ver_participante/(.*)', 'controllers.participantes.ver_participante.VerParticipante',
    '/editar_participante/(.*)', 'controllers.participantes.editar_participante.EditarParticipante',
    '/borrar_participante/(.*)', 'controllers.participantes.borrar_participante.BorrarParticipante',

    # ---------------- Notificaciones ----------------
    '/lista_notificaciones', 'controllers.notificaciones.lista_notificaciones.ListaNotificacion',
    '/insertar_notificacion', 'controllers.notificaciones.insertar_notificacion.InsertarNotificacion',
    '/ver_notificacion/(.*)', 'controllers.notificaciones.ver_notificacion.VerNotificacion',
    '/editar_notificacion/(.*)', 'controllers.notificaciones.editar_notificacion.EditarNotificacion',
    '/borrar_notificacion/(.*)', 'controllers.notificaciones.borrar_notificacion.BorrarNotificacion',
)

app = web.application(urls, globals())

if __name__ == "__main__":
    web.config.debug = True
    app.run()
