import json
import sqlite3

traffic = json.load(open('xxx.json'))
db = sqlite3.connect("fluxos.sqlite")

query = "insert into medicoes values (?,?,?,?,?,?,?)"
columns = ['hoten', 'email', 'dienthoai', 'sothich', 'congnghe', 'nangkhieu']
for timestamp, data in traffic.items():
    keys = (timestamp,) + tuple(data[c] for c in columns)
    c = db.cursor()
    c.execute(query, keys)
    c.close()
c = db.cursor()
c.execute('''CREATE TABLE foo (id integer primary key autoincrement ,
                                    username varchar(50),
                                    password varchar(50))''')
c.execute('INSERT INTO foo (username,password) VALUES (?,?)',
               ('test','test'))
c.execute('INSERT INTO foo (username,password) VALUES (?,?)',
               ('nam','vo dung'))
c.execute('INSERT INTO foo (id,username,password) VALUES (?,?,?)',
               (100,'blah','blah'))
c.execute('INSERT INTO foo (username,password) VALUES (?,?)',
               ('blah','blah'))
c.executemany('INSERT INTO foo (username,password) VALUES (?,?)',
               (('baz','bar'),('bing','bop')))
print(c.lastrowid)
c.execute('SELECT * FROM foo;')
for row in c.execute('SELECT * FROM foo;'):
    print row
c.close()

data = {
    'lsd': lsd,
    'charset_test': csettest, 
    'version': version,
    'ajax': ajax,
    'width': width,
    'pxr': pxr,
    'gps': gps,
    'm_ts': mts,
    'li': li,
}
data['email'] = email
data['pass'] = pass
data['login'] = 'Log In'
s = requests.Session()
r = s.post(url, data=data)
requests.post(URL + '?email=email@domain.com&pass=mypassword')
r.raise_for_status()