import uno,sys
_exportedScripts=[]
def test1():A=XSCRIPTCONTEXT.getDocument();B=A.getText();B.setString('Hello World in Python in Writer');return
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
g_exportedScripts=test2,test1,PythonVersion