#!/bin/bash
# Elimina y vuelve a crear la base de datos metzit.db a partir de script.sql
cd "$(dirname "$0")"
rm -f metzit.db
sqlite3 metzit.db < script.sql
echo "Base de datos 'metzit.db' creada correctamente."
