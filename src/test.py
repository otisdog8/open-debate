
def test1():

    showMessage("your mom")

    return

def test2():

    doc = XSCRIPTCONTEXT.getDocument()

    text = doc.getText()

    text.setString('Bello World in Python in Writer')

    return





_exportedScripts.append("test2")
_exportedScripts.append("test1")
