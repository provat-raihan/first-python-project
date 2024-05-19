amin={
    "name":"mal","age": 28,
    "skill":{
        "code": "js",
        'pc':"laptop",
        "notun": True
    }

}
"""print(amin.keys())
x=(amin.items())
print(x)
"""
print(amin.get("name"))
print(amin["name"])
amin.update({"bokachoda":False})
#print(amin[ "skill"]["pc"])
print(amin.get("skill").get("pc"))