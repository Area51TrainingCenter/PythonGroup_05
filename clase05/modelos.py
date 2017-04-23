from pony.orm import *

db = Database()


class Tarea(db.Entity):
    texto = Required(str)

db.bind('sqlite', 'db.sqlite', create_db=True)
db.generate_mapping(create_tables=True)
