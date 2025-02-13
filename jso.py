import json
py_data ={'name':'Rb','age':None,'active':True}
js_data = json.dumps(py_data)
print(js_data)
print(type(js_data))

new_py_data = json.loads(js_data)
print(new_py_data)

x = '{"name": "Rb", "age": null, "active": true}'
new_py = json.loads(x)
print(new_py)