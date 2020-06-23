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
  return tuple(item)

def createToolbar(name):
  from com.sun.star.beans import PropertyValue
  ctx = XSCRIPTCONTEXT.getComponentContext()
  ToolbarUrl = "private:resource/toolbar/custom_test"
  supplier = ctx.getServiceManager().createInstanceWithContext("com.sun.star.ui.ModuleUIConfigurationManagerSupplier", ctx)
  docType = "com.sun.star.text.TextDocument"
  cfgMgr = supplier.getUIConfigurationManager( docType )
  settings = cfgMgr.createSettings()
  settings.UIName = name
  #cmdID = "macro:///Standard.Module1.TsBTest()"
  cmdID = "vnd.sun.star.script:debate.py$test1?language=Python&location=user"
  cmdLable = "name"
  item = createToolbarItem(cmdID, cmdLable)
  doc = XSCRIPTCONTEXT.getDocument()

  text = doc.getText()

  text.setString(str(item))

  uno.invoke(
    settings, "insertByIndex",
    (0, uno.Any("[]com.sun.star.beans.PropertyValue", item)))

  if cfgMgr.hasSettings( ToolbarUrl ):
    cfgMgr.replaceSettings( ToolbarUrl, settings)
  else:
    cfgMgr.insertSettings( ToolbarUrl, settings)

