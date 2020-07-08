from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
import train
import test
import sys
import os

modelToUSe=""
modelChanged=False

class MainWindow(QMainWindow):
	def __init__(self, *args, **kwargs):

		super(MainWindow,self).__init__(*args, **kwargs)
		self.setGeometry(0, 0,400, 300)

		self.setWindowTitle("Demo AUTOML")

		self.layout = QGridLayout()
		self.label1= QLabel("Welcome! Please select",self)
		self.label1.setFont(QFont('Times', 20, QFont.Bold))

		self.buttonNormal= QPushButton("I have my own images")
		self.buttonNormal.clicked.connect(self.buttonNormal_onClick)

		self.buttonSkip= QPushButton("Just play around")
		self.buttonSkip.clicked.connect(self.buttonSkip_onClick)

		self.layout.addWidget(self.label1, 1,1)
		self.layout.addWidget(self.buttonNormal, 1,2)
		self.layout.addWidget(self.buttonSkip,1,3)

		widget = QWidget()
		widget.setLayout(self.layout)
		self.setCentralWidget(widget)
#		self.setLayout(widget)

	def buttonNormal_onClick(self):
		self.statusBar().showMessage("Switched to window 1")
		self.cams = windowNormal() 
		self.cams.show()
		self.close()

	def buttonSkip_onClick(self):
		self.cams = windowNormal4() 
		self.cams.show()
		self.close()

class windowNormal(QDialog):
	def __init__(self, parent=None):
		super().__init__(parent)
		self.setWindowTitle('window1')
		self.setGeometry(0, 0,400, 300)
		self.setWindowIcon(self.style().standardIcon(QStyle.SP_FileDialogInfoView))


		layoutV = QVBoxLayout()
		self.pushButton = QPushButton(self)
		self.pushButton.setStyleSheet('background-color: rgb(0,0,255); color: #fff')
		self.pushButton.setText('Go back to first page')
		self.pushButton.clicked.connect(self.goMainWindow)

		self.label2= QLabel("Do you have training dataset prepared?")
		self.label2.setFont(QFont('Times', 20, QFont.Bold))

		self.labelWTF= QLabel("What dataset?")
		self.labelWTF.setOpenExternalLinks(True)
		self.labelWTF.setText("<a href=\"http://www.google.com\">What dataset?</a>") #fix later with a page README

		self.pushButtonYes= QPushButton(self)
		self.pushButtonYes.setText('Yes')
		self.pushButtonYes.clicked.connect(self.goEndNormalWindow)

		self.pushButtonNo= QPushButton(self)
		self.pushButtonNo.setText('No')
		self.pushButtonNo.clicked.connect(self.gowindow2)


		layoutV.addWidget(self.pushButton)
		layoutV.addWidget(self.label2)
		layoutV.addWidget(self.labelWTF)
		layoutV.addWidget(self.pushButtonYes)
		layoutV.addWidget(self.pushButtonNo)

		self.setLayout(layoutV)

	def goMainWindow(self):
		self.cams = MainWindow()
		self.cams.show()
		self.close() 

	def goEndNormalWindow(self):
		self.cams = windowNormal3()
		self.cams.show()
		self.close()

	def gowindow2(self):
		self.cams = windowNormal2()
		self.cams.show()
		self.close()

	def prepareScript(self):
		os.system('python3 main.py')
		self.goEndNormalWindow()

# window that start preparing training set
class windowNormal2(QDialog):
	def __init__(self, parent=None):
		super().__init__(parent)
		self.setWindowTitle('Window2')
		self.setGeometry(0, 0,400, 300)
		self.setWindowIcon(self.style().standardIcon(QStyle.SP_FileDialogInfoView))


		layoutV = QVBoxLayout()
		self.pushButton = QPushButton(self)
		self.pushButton.setStyleSheet('background-color: rgb(0,0,255); color: #fff')
		self.pushButton.setText('Go back to last page')
		self.pushButton.clicked.connect(self.goLastWindow)

		self.label3= QLabel("Now we need to prepare some training set")
		self.label3.setFont(QFont('Times', 20, QFont.Bold))

		self.pushButtonPrepare= QPushButton("OK!")
		self.pushButtonPrepare.clicked.connect(self.prepareScript)

		layoutV.addWidget(self.pushButton)
		layoutV.addWidget(self.label3)
		layoutV.addWidget(self.pushButtonPrepare)

		self.setLayout(layoutV)

	def goLastWindow(self):
		self.cams = windowNormal()
		self.cams.show()
		self.close()

	def prepareScript(self):
		os.system('python3 main.py')
		self.goNextNormalWindow()

	def goNextNormalWindow(self):
		self.cams= windowNormal3()
		self.cams.show()
		self.close()

# This window start training
class windowNormal3(QDialog):
	def __init__(self, parent=None):
		super().__init__(parent)
		self.setWindowTitle('Window3')
		self.setGeometry(0, 0,400, 300)
		self.setWindowIcon(self.style().standardIcon(QStyle.SP_FileDialogInfoView))


		layoutV = QVBoxLayout()
		self.pushButton = QPushButton(self)
		self.pushButton.setStyleSheet('background-color: rgb(0,0,255); color: #fff')
		self.pushButton.setText('Go back to last page')
		self.pushButton.clicked.connect(self.goLastWindow)

		self.label3= QLabel("Great! Lets start training now")
		self.label3.setFont(QFont('Times', 20, QFont.Bold))

		self.line = QLineEdit('Type the name of weights you want to train, default is yolo_weights')
		self.line2= QLineEdit('Type the name of weights you want to save')

		self.pushButtonTrain= QPushButton("Start Training!")
		self.pushButtonTrain.clicked.connect(self.trainScript)

		layoutV.addWidget(self.pushButton)
		layoutV.addWidget(self.label3)
		layoutV.addWidget(self.line)
		layoutV.addWidget(self.line2)
		layoutV.addWidget(self.pushButtonTrain)

		self.setLayout(layoutV)

	def showDialog(self):
		msgBox = QMessageBox()
		msgBox.setIcon(QMessageBox.Information)
		msgBox.setText("Training in progress")
		msgBox.setWindowTitle("Training")
		msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)

		returnValue = msgBox.exec()

		if returnValue == QMessageBox.Ok:
			print('OK clicked')

	def goLastWindow(self):
		self.cams = windowNormal()
		self.cams.show()
		self.close()

	def trainScript(self):
		os.system('python3 train.py '+self.line.text()+" "+self.line2.text())
		self.goNextNormalWindow()

	def goNextNormalWindow(self):
		self.cams= windowNormal4()
		self.cams.show()
		self.close()

# This window start testing
class windowNormal4(QDialog):

	def __init__(self, parent=None):
		super().__init__(parent)
		self.setWindowTitle('Window4')
		self.setGeometry(0, 0,400, 300)
		self.setWindowIcon(self.style().standardIcon(QStyle.SP_FileDialogInfoView))


		layoutV = QVBoxLayout()
		self.pushButton = QPushButton(self)
		self.pushButton.setStyleSheet('background-color: rgb(0,0,255); color: #fff')
		self.pushButton.setText('Go back to last page')
		self.pushButton.clicked.connect(self.goLastWindow)

		self.label3= QLabel("Now we can start testing. Please select the model you want to use")
		self.label3.setFont(QFont('Times', 18, QFont.Bold))

		self.labelWTF2= QLabel("Why I can't find my model?")
		self.labelWTF2.setOpenExternalLinks(True)
		self.labelWTF2.setText("<a href=\"http://www.google.com\">Why I can't find my model?</a>")

		self.pushButtonTest= QPushButton("OK!")
		self.pushButtonTest.clicked.connect(self.goNextNormalWindow)

		self.comboBox= QComboBox()
		self.listforCombo = self.listDir()
		for item in self.listforCombo:
			self.comboBox.addItem(item)
		self.comboBox.currentIndexChanged.connect(self.selectionchange)

		layoutV.addWidget(self.pushButton)
		layoutV.addWidget(self.label3)
		layoutV.addWidget(self.labelWTF2)
		layoutV.addWidget(self.comboBox)
		layoutV.addWidget(self.pushButtonTest)

		self.setLayout(layoutV)

	def goLastWindow(self):
		self.cams = windowNormal()
		self.cams.show()
		self.close()

	def goNextNormalWindow(self):
		self.cams= windowTestImage()
		self.cams.show()
		self.close()

	def listDir(self):
		modelList=[]
		for file in os.listdir("./model_data"):
			if file.endswith(".h5"):
				modelList.append(file)

		return modelList

	def selectionchange(self):
		global modelChanged
		global modelToUSe
		print(self.comboBox.currentText())
		modelChanged=True
		modelToUSe= self.comboBox.currentText()

# This window thanks users
class windowNormal5(QDialog):
	def __init__(self, parent=None):
		super().__init__(parent)
		self.setWindowTitle('Window5')
		self.setGeometry(0, 0,400, 300)
		self.setWindowIcon(self.style().standardIcon(QStyle.SP_FileDialogInfoView))


		layoutV = QVBoxLayout()
		self.pushButton = QPushButton(self)
		self.pushButton.setStyleSheet('background-color: rgb(0,0,255); color: #fff')
		self.pushButton.setText('Go back to last page')
		self.pushButton.clicked.connect(self.goLastWindow)

		self.label3= QLabel("Thank you for using this program")
		self.label3.setFont(QFont('Times', 20, QFont.Bold))

		self.pushButtonTest= QPushButton("OK!")
		self.pushButtonTest.clicked.connect(self.callExample)

		#self.labelDrop= CustomLabel('Drop Here',self)


		layoutV.addWidget(self.pushButton)
		layoutV.addWidget(self.label3)
		layoutV.addWidget(self.pushButtonTest)
		#layoutV.addWidget(self.labelDrop)

		self.setLayout(layoutV)

	def goLastWindow(self):
		self.cams = windowNormal()
		self.cams.show()
		self.close()

	def testScript(self):
		test.functionA()
		self.goNextNormalWindow()

	def goNextNormalWindow(self):
		self.cams= windowNormal5()
		self.cams.show()
		self.close()

	def callExample(self):
		self.close()

class windowTestImage(QDialog):

	def __init__(self, parent=None):

		super().__init__(parent)
		self.setWindowTitle('Window6')
		self.setFixedSize(400, 300)
		self.setWindowIcon(self.style().standardIcon(QStyle.SP_FileDialogInfoView))

		
		layoutV = QVBoxLayout()
		self.label4 = QLabel("Drag and Drop the images you want to test")
		self.label4.setFont(QFont('Times', 16, QFont.Bold))

		self.button = Button("Drop Here",self)
		self.button.setIcon(QIcon("gazo1.jpg")) 

		self.buttonOK = Button("Done", self)
		self.buttonOK.clicked.connect(self.writeImagesToList)

		self.listLabel = QListWidget()

		layoutV.addWidget(self.label4)
		layoutV.addWidget(self.button)
		layoutV.addWidget(self.buttonOK)
		layoutV.addWidget(self.listLabel)



		self.setLayout(layoutV)

	def writeImagesToList(self):
		with open("testImage.txt", 'w+') as filehandle:
			for i in range(self.listLabel.count()):
				filehandle.write(self.listLabel.item(i).text()+"\n")
		
		self.testScript()

		self.cams= windowNormal5()
		self.cams.show()
		self.close()

	def testScript(self):
		if (modelChanged):
			os.system('python3 yolo_new.py '+modelToUSe)
		else:
			os.system('python3 yolo_new.py yolo.h5')
		self.goNextNormalWindow()

	def goNextNormalWindow(self):
		self.cams= windowNormal5()
		self.cams.show()
		self.close()

class Button(QPushButton):
	def __init__(self, title, parent):
		super().__init__(title, parent)
		self.setAcceptDrops(True)
		self.listImage=[]

	def dragEnterEvent(self, e):
		m = e.mimeData()
		if m.hasUrls():
			e.accept()
		else:
			e.ignore()

	def dropEvent(self, e):
		m = e.mimeData()
		if m.hasUrls():
			#print(m.urls()[0].toLocalFile())
			self.image2Add= QListWidgetItem(m.urls()[0].toLocalFile())
			self.image2Add.setIcon(QIcon(QPixmap(m.urls()[0].toLocalFile())))

			self.parent().listLabel.addItem(self.image2Add)




app= QApplication(sys.argv)

window= MainWindow()
window.show()

app.exec_()

