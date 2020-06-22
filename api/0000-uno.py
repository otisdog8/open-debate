
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

