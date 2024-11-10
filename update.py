# d={1:["raja",23,"bhopal"],2:["jay",23,"ujjain"]}
# print(d)
# d[2][2]="indore"
# print(d)


d1={101:{"name":"ajay","age":23,"city":"bhopal"},
    102:{"name":"jay","age":23,"city":"ujjain"}}
# print(d1)
d1[102]["city"]="indore"
print(d1)
d1[102].update({"city":"indore"})
print(d1)