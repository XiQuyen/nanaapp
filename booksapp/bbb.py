import json
# no iteritems ->items
traffic = json.load(open('xxx.json'))
print (traffic)
columns = ['hoten', 'email', 'dienthoai', 'sothich', 'congnghe', 'nangkhieu']
for timestamp, data in traffic.items():
    keys = (timestamp,) + tuple(data[c] for c in columns)
    print (str(keys))