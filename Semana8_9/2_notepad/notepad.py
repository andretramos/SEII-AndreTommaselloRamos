import sys, os
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QLabel, \
							QPlainTextEdit, QStatusBar, QToolBar, QVBoxLayout, QAction, \
							QFileDialog, QMessageBox
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QFontDatabase, QIcon, QKeySequence
from PyQt5.QtPrintSupport import QPrintDialog

class AppDemo(QMainWindow):

	def __init__(self):
		super().__init__()
		self.screen_width, self.screen_height = self.geometry().width(), self.geometry().height()
		self.setWindowIcon(QIcon('./icons/notepad.png'))
		self.resize(self.screen_width * 1 , self.screen_height * 1)

		self.filterTypes = 'Text Document (*.txt);; Python (*.py);; Markdown(*.md)'

		self.path = None

		fixedFont = QFontDatabase.systemFont(QFontDatabase.FixedFont)
		fixedFont.setPointSize(12)

		mainLayout = QVBoxLayout()


		#Editor
		self.editor = QPlainTextEdit()
		self.editor.setFont(fixedFont)
		mainLayout.addWidget(self.editor)

		#Barra de status
		self.statusBar = self.statusBar()

		#App container
		container = QWidget()
		container.setLayout(mainLayout)
		self.setCentralWidget(container)

		#Menu de arquivos
		file_menu = self.menuBar().addMenu('&File')

		#Barra de ferramentas de arquivos
		file_toolbar = QToolBar('File')
		file_toolbar.setIconSize(QSize(60,60))
		self.addToolBar(Qt.BottomToolBarArea, file_toolbar)

		#Abrir, fechar e salvar como
		open_file_action = QAction(QIcon('./Icons/openfile.png'), 'Open file...', self)
		open_file_action.setStatusTip('Open file')
		open_file_action.setShortcut(QKeySequence.Open)
		open_file_action.triggered.connect(self.file_open)

		save_file_action = self.create_action(self,'./Icons/savefile.png', 'Save File...', 'Save file', self.file_save)
		save_file_action.setShortcut(QKeySequence.Save)

		save_fileAs_action = self.create_action(self,'./Icons/savefileas.png', 'Save File As...', 'Save file as', self.file_saveAs)
		save_fileAs_action.setShortcut(QKeySequence('Ctrl+Shift+S'))


		file_menu.addActions([open_file_action, save_file_action, save_fileAs_action])
		file_toolbar.addActions([open_file_action, save_file_action, save_fileAs_action])

		# #Print action
		# print_action = self.create_action(self, './Icons/print.png', 'Print File', 'print file', lambda: print('print document'))
		# save_fileAs_action.setShortcut(QKeySequence.Print)

		# file_menu.addAction(print_action)
		# file_toolbar.addAction(print_action)

	def file_open(self):
		path, _ = QFileDialog.getOpenFileName(
			parent=self,
			caption='Open file',
			directory='',
			filter = self.filterTypes
			)

		if path:
			try:
				with open(path, 'r') as f:
					text = f.read()
					f.close()
			except Exception as e:
				self.dialog_message(str(e))
			else:
				self.path = path
				self.editor.setPlainText(text)
				self.update_title()

	def file_save(self):
		if self.path is None:
			self.file_saveAs()
		else:
			try:
				text = self.editor.toPlainText()
				with open(self.path, 'w') as f:
					f.write(text)
					f.close()

			except Exception as e:
				self.dialog_message(e)

	def file_saveAs(self):
		path, _ = QFileDialog.getSaveFileName(
			self,
			'Save file as',
			'',
			self.filterTypes
		)

		text = self.editor.toPlainText()

		if not path:
			return
		else:
			try:
				with open(path,'w') as f:
					f.write(text)
					f.close()
			except Exception as e:
				self.dialog_message(str(e))
			else:
				self.path =  path
				self.update_title()


	def update_title(self):
		self.setWindowTitle('{0} - Bloco de Notas'.format(os.path.basename(self.path) if self.path else 'Sem nome'))

	def dialog_message(self,message):
		dlg = QMessageBox(self)
		dlg.settext(message)
		dlg.setIcon(QMessagebox.Critical)
		dlg.show()





	def create_action(self,parent,icon_path,action_name,set_status_tip,triggered_method):
		action = QAction(QIcon(icon_path),action_name,parent)
		action.setStatusTip(set_status_tip)
		action.triggered.connect(triggered_method)
		return action




app = QApplication(sys.argv)
notePade = AppDemo()
notePade.show()
sys.exit(app.exec())
