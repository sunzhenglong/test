import json
a_1 = {'hh':123,'gg':456}
print(a_1)
b = json.dumps(a_1)
print(b)
c = json.loads(b)
print(type(c))
print(c)