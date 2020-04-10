import uno,sys,msgbox
_exportedScripts=[]
def test1():showMessage('your mom');return
def test2():A=XSCRIPTCONTEXT.getDocument();B=A.getText();B.setString('Bello World in Python in Writer');return
_exportedScripts.append('test2')
_exportedScripts.append('test1')
def PythonVersion(*F):
	'Prints the Python version into the current document';B=XSCRIPTCONTEXT.getDesktop();A=B.getCurrentComponent()
	if not hasattr(A,'Text'):A=B.loadComponentFromURL('private:factory/swriter','_blank',0,())
	D=A.Text;C=D.End;C.String=''
	for E in sys.path:C.String+=E
	return None
_exportedScripts.append('PythonVersion')
MsgBox=msgbox.MsgBox
def showMessage(text):A=MsgBox(XSCRIPTCONTEXT.getComponentContext());A.renderFromBoxSize(500);A.show(text,None,'testbox')
g_exportedScripts=test2,test1,PythonVersion