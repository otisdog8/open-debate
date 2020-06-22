
def test1():

    showMessage("your mom")

    return

def test2():
    from com.sun.star.beans import PropertyValue

    # open a writer document object
    doc = XSCRIPTCONTEXT.getDocument()



    # NOTE THAT ARGS IS A TUPLE OF PROPERTY VALUES


    # close the document

    text = doc.getText()

    text.setString('Bello World in Python in Writer')
    createToolbar("bruh")
    return





_exportedScripts.append("test2")
_exportedScripts.append("test1")
