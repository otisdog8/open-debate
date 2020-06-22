
print("Made by Jacob Root")
print("https://github.com/otisdog8/open-debate for source and compiling info")
import uno,sys,msgbox
_exportedScripts = []

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
    createToolbar("test")
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
    box.renderFromBoxSize(250)
    box.show(inputbox("Help"), None, "testbox")


def inputbox(message, title="", default="", x=None, y=None):
    """ Shows dialog with input box.
        @param message message to show on the dialog
        @param title window title
        @param default default value
        @param x dialog positio in twips, pass y also
        @param y dialog position in twips, pass y also
        @return string if OK button pushed, otherwise zero length string
    """
    WIDTH = 600
    HORI_MARGIN = VERT_MARGIN = 8
    BUTTON_WIDTH = 100
    BUTTON_HEIGHT = 26
    HORI_SEP = VERT_SEP = 8
    LABEL_HEIGHT = BUTTON_HEIGHT * 2 + 5
    EDIT_HEIGHT = 24
    HEIGHT = VERT_MARGIN * 2 + LABEL_HEIGHT + VERT_SEP + EDIT_HEIGHT
    import uno
    from com.sun.star.awt.PosSize import POS, SIZE, POSSIZE
    from com.sun.star.awt.PushButtonType import OK, CANCEL
    from com.sun.star.util.MeasureUnit import TWIP
    ctx = uno.getComponentContext()
    def create(name):
        return ctx.getServiceManager().createInstanceWithContext(name, ctx)
    dialog = create("com.sun.star.awt.UnoControlDialog")
    dialog_model = create("com.sun.star.awt.UnoControlDialogModel")
    dialog.setModel(dialog_model)
    dialog.setVisible(False)
    dialog.setTitle(title)
    dialog.setPosSize(0, 0, WIDTH, HEIGHT, SIZE)
    def add(name, type, x_, y_, width_, height_, props):
        model = dialog_model.createInstance("com.sun.star.awt.UnoControl" + type + "Model")
        dialog_model.insertByName(name, model)
        control = dialog.getControl(name)
        control.setPosSize(x_, y_, width_, height_, POSSIZE)
        for key, value in props.items():
            setattr(model, key, value)
    label_width = WIDTH - BUTTON_WIDTH - HORI_SEP - HORI_MARGIN * 2
    add("label", "FixedText", HORI_MARGIN, VERT_MARGIN, label_width, LABEL_HEIGHT, 
        {"Label": str(message), "NoLabel": True})
    add("btn_ok", "Button", HORI_MARGIN + label_width + HORI_SEP, VERT_MARGIN, 
            BUTTON_WIDTH, BUTTON_HEIGHT, {"PushButtonType": OK, "DefaultButton": True})
    add("btn_cancel", "Button", HORI_MARGIN + label_width + HORI_SEP, VERT_MARGIN + BUTTON_HEIGHT + 5, 
            BUTTON_WIDTH, BUTTON_HEIGHT, {"PushButtonType": CANCEL})
    add("edit", "Edit", HORI_MARGIN, LABEL_HEIGHT + VERT_MARGIN + VERT_SEP, 
            WIDTH - HORI_MARGIN * 2, EDIT_HEIGHT, {"Text": str(default)})
    frame = create("com.sun.star.frame.Desktop").getCurrentFrame()
    window = frame.getContainerWindow() if frame else None
    dialog.createPeer(create("com.sun.star.awt.Toolkit"), window)
    if not x is None and not y is None:
        ps = dialog.convertSizeToPixel(uno.createUnoStruct("com.sun.star.awt.Size", x, y), TWIP)
        _x, _y = ps.Width, ps.Height
    elif window:
        ps = window.getPosSize()
        _x = ps.Width / 2 - WIDTH / 2
        _y = ps.Height / 2 - HEIGHT / 2
    dialog.setPosSize(_x, _y, 0, 0, POS)
    edit = dialog.getControl("edit")
    edit.setSelection(uno.createUnoStruct("com.sun.star.awt.Selection", 0, len(str(default))))
    edit.setFocus()
    ret = edit.getModel().Text if dialog.execute() else ""
    dialog.dispose()
    return ret
#Internal settings API
#This handles calls to the DB API that concern settings specifically#Internal database API, handles calls to a specific internal database#API for formatting, also maybe has hooks into buttons for format
#Handle all connections to the wiki#Handle all connections to tab#Handle all connections to email/email chains#Handle all connections to speechdrop#Handles all configuration related to the toolbar. Extensions should modify this part to get their own tilebar buttons
def getDocument():
  return XSCRIPTCONTEXT.getDocument()

def getComponentContext():
  return XSCRIPTCONTEXT.getComponentContext()

def getInvocationContext():
  return XSCRIPTCONTEXT.getInvocationContext()

def getDesktop():
  return XSCRIPTCONTEXT.getDesktop()

def getServiceManager():
  return getComponentContext().getServiceManager()

def createToolbarItem(ID, lable):
  from com.sun.star.beans import PropertyValue
  from com.sun.star.ui.ItemType import DEFAULT
  item = []
  for i in range(4):
    item.append(PropertyValue())
  item[0].Name = "CommandURL"
  item[0].Value = ID
  item[1].Name = "Label"
  item[1].Value = lable
  item[2].Name = "Type"
  item[2].Value = DEFAULT
  item[3].Name = "Visible"
  item[3].Value = True
  return (item[0], item[1], item[2], item[3])

def createToolbar(name):
  from com.sun.star.beans import PropertyValue
  ctx = XSCRIPTCONTEXT.getComponentContext()
  ToolbarUrl = "private:resource/toolbar/custom_test"
  supplier = ctx.getServiceManager().createInstanceWithContext("com.sun.star.ui.ModuleUIConfigurationManagerSupplier", ctx)
  docType = "com.sun.star.text.TextDocument"
  cfgMgr = supplier.getUIConfigurationManager( docType )
  settings = cfgMgr.createSettings()
  settings.UIName = name
  cmdID = "macro:///Standard.Module1.TBTest()"
  cmdLable = "name"
  item = createToolbarItem(cmdID, cmdLable)
  doc = XSCRIPTCONTEXT.getDocument()

  text = doc.getText()

  text.setString(str(item))

  settings.insertByIndex(0, item)

  if cfgMgr.hasSettings( ToolbarUrl ):
    cfgMgr.replaceSettings( ToolbarUrl, settings)
  else:
    cfgMgr.insertSettings( ToolbarUrl, settings)


def getScript():
    return _exportedScripts