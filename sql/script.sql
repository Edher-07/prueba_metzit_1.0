-- Activar el soporte para claves foráneas en SQLite
PRAGMA foreign_keys = ON;
.mode box
.head on

-- ===================== ROLES =====================
CREATE TABLE roles(
    id_rol INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre_rol TEXT NOT NULL,
    descripcion TEXT
);

-- ===================== USUARIOS =====================
CREATE TABLE usuarios(
    id_usuario INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    apellido_paterno TEXT NOT NULL,
    apellido_materno TEXT NOT NULL,
    direccion TEXT,
    telefono TEXT,
    correo TEXT,
    contrasena TEXT,
    estado INTEGER DEFAULT 1,
    fecha_registro DATETIME DEFAULT CURRENT_TIMESTAMP,
    id_rol INTEGER NOT NULL,
    FOREIGN KEY (id_rol) REFERENCES roles(id_rol)
);

-- ===================== ÁREA DE RIEGO =====================
CREATE TABLE area_riego(
    id_area INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    suficiente INTEGER DEFAULT 1,
    ubicacion TEXT
);

-- ===================== TURNOS DE RIEGO =====================
CREATE TABLE turnos_riego(
    id_turno INTEGER PRIMARY KEY AUTOINCREMENT,
    fecha TEXT NOT NULL,
    hora_inicio TEXT,
    hora_fin TEXT,
    id_area INTEGER NOT NULL,
    estado TEXT,
    FOREIGN KEY (id_area) REFERENCES area_riego(id_area)
);

-- ===================== CULTIVOS =====================
CREATE TABLE cultivos(
    id_cultivo INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    descripcion TEXT,
    temporada TEXT,
    recomendaciones TEXT,
    caracteristicas TEXT
);

-- Tabla intermedia N:M entre área_riego y cultivos (según diagrama E-R)
CREATE TABLE area_cultivo(
    id_area INTEGER NOT NULL,
    id_cultivo INTEGER NOT NULL,
    PRIMARY KEY (id_area, id_cultivo),
    FOREIGN KEY (id_area) REFERENCES area_riego(id_area),
    FOREIGN KEY (id_cultivo) REFERENCES cultivos(id_cultivo)
);

-- ===================== PUBLICACIONES =====================
CREATE TABLE publicaciones(
    id_publicacion INTEGER PRIMARY KEY AUTOINCREMENT,
    id_usuario INTEGER NOT NULL,
    titulo TEXT NOT NULL,
    contenido TEXT,
    categoria TEXT,
    fecha_publicacion DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (id_usuario) REFERENCES usuarios(id_usuario)
);

-- ===================== REPORTES =====================
CREATE TABLE reportes(
    id_reporte INTEGER PRIMARY KEY AUTOINCREMENT,
    id_usuario INTEGER NOT NULL,
    titulo TEXT NOT NULL,
    descripcion TEXT,
    estado TEXT,
    fecha DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (id_usuario) REFERENCES usuarios(id_usuario)
);

-- ===================== FAENAS =====================
CREATE TABLE faenas(
    id_faena INTEGER PRIMARY KEY AUTOINCREMENT,
    id_usuario INTEGER NOT NULL,
    descripcion TEXT,
    fecha TEXT,
    hora TEXT,
    limite_fecha TEXT,
    multa REAL DEFAULT 0,
    FOREIGN KEY (id_usuario) REFERENCES usuarios(id_usuario)
);

-- ===================== PARTICIPANTES =====================
CREATE TABLE participantes(
    id_participante INTEGER PRIMARY KEY AUTOINCREMENT,
    id_usuario INTEGER NOT NULL,
    id_faena INTEGER NOT NULL,
    asistencia INTEGER DEFAULT 0,
    representante INTEGER DEFAULT 0,
    multa_aplicada REAL DEFAULT 0,
    observaciones TEXT,
    FOREIGN KEY (id_usuario) REFERENCES usuarios(id_usuario),
    FOREIGN KEY (id_faena) REFERENCES faenas(id_faena)
);

-- ===================== NOTIFICACIONES =====================
CREATE TABLE notificaciones(
    id_notificacion INTEGER PRIMARY KEY AUTOINCREMENT,
    id_usuario INTEGER NOT NULL,
    titulo TEXT NOT NULL,
    mensaje TEXT,
    leida INTEGER DEFAULT 0,
    fecha_envio DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (id_usuario) REFERENCES usuarios(id_usuario)
);

-- ===================== DATOS DE PRUEBA =====================

INSERT INTO roles(nombre_rol, descripcion) VALUES
('Administrador', 'Control total del sistema'),
('Comisariado', 'Gestiona turnos, publicaciones, reportes y faenas'),
('Usuario', 'Habitante que consulta información y participa en actividades');

INSERT INTO usuarios(nombre, apellido_paterno, apellido_materno, direccion, telefono, correo, contrasena, estado, id_rol)
VALUES
('Manuel', 'Ramiro', 'Soto', 'San Bartolo, La Barranca', '7711234567', 'manuel@metzit.com', '12345', 1, 2),

INSERT INTO turnos_riego(fecha, hora_inicio, hora_fin, estado) VALUES
('2026-08-05', '06:00', '08:00', 1, 'Programado'),
('2026-08-05', '08:00', '10:00', 2, 'Programado');

INSERT INTO cultivos(nombre, descripcion, temporada, recomendaciones, caracteristicas) VALUES
('Maíz', 'Cultivo base de la región', 'Primavera-Verano', 'Regar cada 3 días', 'Requiere suelo fértil'),
('Frijol', 'Cultivo de traspatio y milpa', 'Verano', 'Sembrar junto al maíz', 'Fija nitrógeno al suelo');

INSERT INTO publicaciones(id_usuario, titulo, contenido, categoria) VALUES
(1, 'Aviso de mantenimiento', 'Se realizará mantenimiento a la toma de agua el próximo fin de semana.', 'Aviso'),
(1, 'Convocatoria a faena', 'Se convoca a faena comunitaria el sábado a las 8am.', 'Faena');

INSERT INTO reportes(id_usuario, titulo, descripcion, estado) VALUES
(1, 'Fuga de agua', 'Se detectó una fuga en la tubería principal de la Zona Sur.', 'Pendiente');

INSERT INTO faenas(id_usuario, descripcion, fecha, hora, limite_fecha, multa) VALUES
(1, 'Limpieza del canal principal', '2026-08-08', '08:00', '2026-08-07', 100.00);

INSERT INTO participantes(id_usuario, id_faena, asistencia, representante, multa_aplicada, observaciones) VALUES
(2, 1, 1, 0, 0, 'Asistió puntual'),
(3, 1, 0, 0, 100.00, 'No asistió, se aplicó multa');

INSERT INTO notificaciones(id_usuario, titulo, mensaje, leida) VALUES
(2, 'Turno de riego asignado', 'Tu turno de riego es el 05/08/2026 de 06:00 a 08:00.', 0),
(3, 'Nueva publicación', 'Hay un nuevo aviso de la comunidad, revísalo en el apartado de publicaciones.', 0);

-- ===================== CONSULTAS DE VERIFICACIÓN =====================
SELECT * FROM usuarios;
SELECT * FROM turnos_riego;
