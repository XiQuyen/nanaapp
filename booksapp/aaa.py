import sqlite3

db = sqlite3.connect("fluxos.sqlite")
c = db.cursor()

c.execute('''create table medicoes
         (timestamp text primary key,
          local text,
          coord text,
          sentido text,
          veiculos text,
          modalidade text,
          pistas text)''')

c.execute('''create table valores
         (id integer primary key,
          quantidade integer,
          tempo integer,
          foreign key (id) references medicoes(timestamp))''')