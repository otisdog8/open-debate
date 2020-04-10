import os, python_minifier

print("Compiling into single python file")

imports = ["uno", "sys", "msgbox"]
importstring = "import "
for name in imports:
    importstring += name + ','

importstring = importstring[:-1]

result = importstring + "\n_exportedScripts = []\n"

endfileeval = '''\ndef getScript():
    return _exportedScripts'''
endfilefinal =  "\ng_exportedScripts =  tuple(_exportedScripts)"

for f in os.listdir("src"):
    if f.endswith(".py"):
        fi = open("src/" + f, 'r')
        t = fi.read()
        result += t


endfileeval = result + endfileeval
with open("stage1.py", "w") as f:
    f.write(endfileeval)
from stage1 import getScript
_exportedScripts = getScript()

result += "\ng_exportedScripts = ("
for num, name in enumerate(_exportedScripts):
    result += name + ','
result += ")"

result = python_minifier.minify(result)

with open('build/src.py', "w") as f:
    f.write(result)

if input("install? ") == "y":
    with open('/home/otis/.config/libreoffice/4/user/Scripts/python/debate.py', "w") as f:
        f.write(result)