_B='Text'
_A=None
print('Made by Jacob Root')
print('https://github.com/otisdog8/open-debate for source and compiling info')
import uno,sys,msgbox
_exportedScripts=[]
def test1():showMessage('your mom');return
def test2():A=XSCRIPTCONTEXT.getDocument();B=A.getText();B.setString('Bello World in Python in Writer');return
_exportedScripts.append('test2')
_exportedScripts.append('test1')
def PythonVersion(*F):
	'Prints the Python version into the current document';B=XSCRIPTCONTEXT.getDesktop();A=B.getCurrentComponent()
	if not hasattr(A,_B):A=B.loadComponentFromURL('private:factory/swriter','_blank',0,())
	D=A.Text;C=D.End;C.String=''
	for E in sys.path:C.String+=E
	return _A
_exportedScripts.append('PythonVersion')
MsgBox=msgbox.MsgBox
def showMessage(text):A=MsgBox(XSCRIPTCONTEXT.getComponentContext());A.renderFromBoxSize(250);A.show(inputbox('Help'),_A,'testbox')
def inputbox(message,title='',default='',x=_A,y=_A):
	' Shows dialog with input box.\n        @param message message to show on the dialog\n        @param title window title\n        @param default default value\n        @param x dialog positio in twips, pass y also\n        @param y dialog position in twips, pass y also\n        @return string if OK button pushed, otherwise zero length string\n    ';e='edit';d='PushButtonType';c='Button';b=True;Q=default;E=600;B=C=8;I=100;F=26;J=R=8;K=F*2+5;S=24;T=C*2+K+R+S;import uno as L;from com.sun.star.awt.PosSize import POS,SIZE,POSSIZE as Y;from com.sun.star.awt.PushButtonType import OK,CANCEL as Z;from com.sun.star.util.MeasureUnit import TWIP;U=L.getComponentContext()
	def G(name):return U.getServiceManager().createInstanceWithContext(name,U)
	A=G('com.sun.star.awt.UnoControlDialog');M=G('com.sun.star.awt.UnoControlDialogModel');A.setModel(M);A.setVisible(False);A.setTitle(title);A.setPosSize(0,0,E,T,SIZE)
	def H(name,type,x_,y_,width_,height_,props):
		B=M.createInstance('com.sun.star.awt.UnoControl'+type+'Model');M.insertByName(name,B);C=A.getControl(name);C.setPosSize(x_,y_,width_,height_,Y)
		for (D,E) in props.items():setattr(B,D,E)
	N=E-I-J-B*2;H('label','FixedText',B,C,N,K,{'Label':str(message),'NoLabel':b});H('btn_ok',c,B+N+J,C,I,F,{d:OK,'DefaultButton':b});H('btn_cancel',c,B+N+J,C+F+5,I,F,{d:Z});H(e,'Edit',B,K+C+R,E-B*2,S,{_B:str(Q)});V=G('com.sun.star.frame.Desktop').getCurrentFrame();O=V.getContainerWindow()if V else _A;A.createPeer(G('com.sun.star.awt.Toolkit'),O)
	if not x is _A and not y is _A:D=A.convertSizeToPixel(L.createUnoStruct('com.sun.star.awt.Size',x,y),TWIP);W,X=D.Width,D.Height
	elif O:D=O.getPosSize();W=D.Width/2-E/2;X=D.Height/2-T/2
	A.setPosSize(W,X,0,0,POS);P=A.getControl(e);P.setSelection(L.createUnoStruct('com.sun.star.awt.Selection',0,len(str(Q))));P.setFocus();a=P.getModel().Text if A.execute()else'';A.dispose();return a
g_exportedScripts=test2,test1,PythonVersion