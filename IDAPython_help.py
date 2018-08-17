# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from help_ui import *
import os



class testPy(Ui_MainWindow):
	def __init__(self, test):
		Ui_MainWindow.__init__(self)
		self.setupUi(test)
		self.pushButton.clicked.connect(self.btn_click)
		self.pushButton_2.clicked.connect(self.btn_home)
		self.listWidget.itemClicked.connect(self.click_func)
	
	def click_func(self):
		default_list = ['DataRead','DataBase','Disassembly','File','Function','String']
		if self.listWidget.currentItem().text() in default_list:
			items = self.listWidget.currentItem().text()
			stat_flag = self.find_file(items)
		else:
			items = self.listWidget.currentItem().text()
			self.view_file(items)
	
	def find_file(self, items):
		dir = '/Applications/IDA Pro 7.1/idabin/plugins/IDAhelp/DATA/'+items+'/'
		self.listWidget.clear()
		files = os.listdir(dir)
		for i in files:
			self.listWidget.addItem(i)
		return stat_flag

	def view_file(self, items):
		default_list = ['DataRead','DataBase','Disassembly','File','Function','String']
		for i in default_list:
			dir  = '/Applications/IDA Pro 7.1/idabin/plugins/IDAhelp/DATA/'+i+'/'+items
			if os.path.isfile(dir):
				f = open(dir,"r")
				s = f.read()
				if s == "":
					self.textBrowser.setText("404 Not Found")
				else:
					self.textBrowser.setText(s)

	def btn_home(self):
		self.listWidget.clear()
		self.textBrowser.setText("")
		default_list = ['DataRead','DataBase','Disassembly','File','Function','String']
		for i in default_list:
			self.listWidget.addItem(i)

	def btn_click(self):
		text = self.textEdit.text()
		self.textBrowser.setText(text)
	

MainWindow = QtWidgets.QMainWindow()
ui = testPy(MainWindow)
MainWindow.show()

