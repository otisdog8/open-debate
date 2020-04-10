MsgBox = msgbox.MsgBox

def showMessage(text):
    box = MsgBox(XSCRIPTCONTEXT.getComponentContext())
    box.renderFromBoxSize(500)
    box.show(text, None, "testbox")
