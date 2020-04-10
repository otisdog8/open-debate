import uno,sys,msgbox
_exportedScripts = []

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
def PythonVersion(*args):
    """Prints the Python version into the current document"""
#get the doc from the scripting context which is made available to all scripts
    desktop = XSCRIPTCONTEXT.getDesktop()
    model = desktop.getCurrentComponent()
#check whether there's already an opened document. Otherwise, create a new one
    if not hasattr(model, "Text"):
        model = desktop.loadComponentFromURL(
            "private:factory/swriter","_blank", 0, () )
#get the XText interface
    text = model.Text
#create an XTextRange at the end of the document
    tRange = text.End
#and set the string
    tRange.String = ""
    for i in sys.path:
        tRange.String += i
    return None
_exportedScripts.append("PythonVersion")

MsgBox = msgbox.MsgBox

def showMessage(text):
    box = MsgBox(XSCRIPTCONTEXT.getComponentContext())
    box.renderFromBoxSize(500)
    box.show(text, None, "testbox")

def getScript():
    return _exportedScripts