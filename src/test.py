
def test1():

    doc = XSCRIPTCONTEXT.getDocument()

    text = doc.getText()

    text.setString('Hello World in Python in Writer')

    return

def test2():

    doc = XSCRIPTCONTEXT.getDocument()

    text = doc.getText()

    text.setString('Bello World in Python in Writer')

    return





_exportedScripts.append("test2")
_exportedScripts.append("test1")
