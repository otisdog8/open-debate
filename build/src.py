_D='Label'
_C='Text'
_B=True
_A=None
print('Made by Jacob Root')
print('https://github.com/otisdog8/open-debate for source and compiling info')
import uno,sys,msgbox
_exportedScripts=[]
def test1():showMessage('your mom');return
def test2():from com.sun.star.beans import PropertyValue;A=XSCRIPTCONTEXT.getDocument();B=A.getText();B.setString('Bello World in Python in Writer');createToolbar('test');return
_exportedScripts.append('test2')
_exportedScripts.append('test1')
def PythonVersion(*F):
	'Prints the Python version into the current document';B=XSCRIPTCONTEXT.getDesktop();A=B.getCurrentComponent()
	if not hasattr(A,_C):A=B.loadComponentFromURL('private:factory/swriter','_blank',0,())
	D=A.Text;C=D.End;C.String=''
	for E in sys.path:C.String+=E
	return _A
_exportedScripts.append('PythonVersion')
MsgBox=msgbox.MsgBox
def showMessage(text):A=MsgBox(XSCRIPTCONTEXT.getComponentContext());A.renderFromBoxSize(250);A.show(inputbox('Help'),_A,'testbox')
def inputbox(message,title='',default='',x=_A,y=_A):
	' Shows dialog with input box.\n        @param message message to show on the dialog\n        @param title window title\n        @param default default value\n        @param x dialog positio in twips, pass y also\n        @param y dialog position in twips, pass y also\n        @return string if OK button pushed, otherwise zero length string\n    ';d='edit';c='PushButtonType';b='Button';Q=default;E=600;B=C=8;I=100;F=26;J=R=8;K=F*2+5;S=24;T=C*2+K+R+S;import uno as L;from com.sun.star.awt.PosSize import POS,SIZE,POSSIZE as Y;from com.sun.star.awt.PushButtonType import OK,CANCEL as Z;from com.sun.star.util.MeasureUnit import TWIP;U=L.getComponentContext()
	def G(name):return U.getServiceManager().createInstanceWithContext(name,U)
	A=G('com.sun.star.awt.UnoControlDialog');M=G('com.sun.star.awt.UnoControlDialogModel');A.setModel(M);A.setVisible(False);A.setTitle(title);A.setPosSize(0,0,E,T,SIZE)
	def H(name,type,x_,y_,width_,height_,props):
		B=M.createInstance('com.sun.star.awt.UnoControl'+type+'Model');M.insertByName(name,B);C=A.getControl(name);C.setPosSize(x_,y_,width_,height_,Y)
		for (D,E) in props.items():setattr(B,D,E)
	N=E-I-J-B*2;H('label','FixedText',B,C,N,K,{_D:str(message),'NoLabel':_B});H('btn_ok',b,B+N+J,C,I,F,{c:OK,'DefaultButton':_B});H('btn_cancel',b,B+N+J,C+F+5,I,F,{c:Z});H(d,'Edit',B,K+C+R,E-B*2,S,{_C:str(Q)});V=G('com.sun.star.frame.Desktop').getCurrentFrame();O=V.getContainerWindow()if V else _A;A.createPeer(G('com.sun.star.awt.Toolkit'),O)
	if not x is _A and not y is _A:D=A.convertSizeToPixel(L.createUnoStruct('com.sun.star.awt.Size',x,y),TWIP);W,X=D.Width,D.Height
	elif O:D=O.getPosSize();W=D.Width/2-E/2;X=D.Height/2-T/2
	A.setPosSize(W,X,0,0,POS);P=A.getControl(d);P.setSelection(L.createUnoStruct('com.sun.star.awt.Selection',0,len(str(Q))));P.setFocus();a=P.getModel().Text if A.execute()else'';A.dispose();return a
def getDocument():return XSCRIPTCONTEXT.getDocument()
def getComponentContext():return XSCRIPTCONTEXT.getComponentContext()
def getInvocationContext():return XSCRIPTCONTEXT.getInvocationContext()
def getDesktop():return XSCRIPTCONTEXT.getDesktop()
def getServiceManager():return getComponentContext().getServiceManager()
def createToolbarItem(ID,lable):
	from com.sun.star.beans import PropertyValue as B;from com.sun.star.ui.ItemType import DEFAULT as C;A=[]
	for D in range(4):A.append(B())
	A[0].Name='CommandURL';A[0].Value=ID;A[1].Name=_D;A[1].Value=lable;A[2].Name='Type';A[2].Value=C;A[3].Name='Visible';A[3].Value=_B;return tuple(A)
def createToolbar(name):
	from com.sun.star.beans import PropertyValue;D=XSCRIPTCONTEXT.getComponentContext();C='private:resource/toolbar/custom_test';F=D.getServiceManager().createInstanceWithContext('com.sun.star.ui.ModuleUIConfigurationManagerSupplier',D);G='com.sun.star.text.TextDocument';A=F.getUIConfigurationManager(G);B=A.createSettings();B.UIName=name;H='vnd.sun.star.script:Standard.Module1.TBTest?language=Basic&location=application';I='name';E=createToolbarItem(H,I);J=XSCRIPTCONTEXT.getDocument();K=J.getText();K.setString(str(E));uno.invoke(B,'insertByIndex',(0,uno.Any('[]com.sun.star.beans.PropertyValue',E)))
	if A.hasSettings(C):A.replaceSettings(C,B)
	else:A.insertSettings(C,B)
g_exportedScripts=test2,test1,PythonVersion