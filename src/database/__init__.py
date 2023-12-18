import json, os

def r():
    return json.load(open("src/database/database.json", "r"))
            
def w(content):
    open("src/database/database.json", "w").write(json.dumps(content, indent=2))

def a(content):
    ar = r()
    ar.update(content)
    w(ar)