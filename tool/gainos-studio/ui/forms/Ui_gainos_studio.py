# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\parai@foxmail.com\github\gainos-tk\tool\gainos-studio\ui\forms\gainos_studio.ui'
#
# Created: Thu Jun 06 20:42:13 2013
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_mwgainostk(object):
    def setupUi(self, mwgainostk):
        mwgainostk.setObjectName(_fromUtf8("mwgainostk"))
        mwgainostk.resize(255, 485)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(mwgainostk.sizePolicy().hasHeightForWidth())
        mwgainostk.setSizePolicy(sizePolicy)
        mwgainostk.setStyleSheet(_fromUtf8("font: 12pt \"Consolas\";"))
        self.centralwidget = QtGui.QWidget(mwgainostk)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.trModule = QtGui.QTreeWidget(self.centralwidget)
        self.trModule.setGeometry(QtCore.QRect(10, 10, 111, 421))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.trModule.sizePolicy().hasHeightForWidth())
        self.trModule.setSizePolicy(sizePolicy)
        self.trModule.setStyleSheet(_fromUtf8("font: 12pt \"Consolas\";"))
        self.trModule.setObjectName(_fromUtf8("trModule"))
        self.teInfo = QtGui.QTextEdit(self.centralwidget)
        self.teInfo.setGeometry(QtCore.QRect(130, 210, 111, 221))
        self.teInfo.setStyleSheet(_fromUtf8("font: 12pt \"Consolas\";"))
        self.teInfo.setObjectName(_fromUtf8("teInfo"))
        self.layoutWidget = QtGui.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(130, 35, 113, 161))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.btnAdd = QtGui.QPushButton(self.layoutWidget)
        self.btnAdd.setObjectName(_fromUtf8("btnAdd"))
        self.verticalLayout.addWidget(self.btnAdd)
        self.btnEdit = QtGui.QPushButton(self.layoutWidget)
        self.btnEdit.setObjectName(_fromUtf8("btnEdit"))
        self.verticalLayout.addWidget(self.btnEdit)
        self.btnDel = QtGui.QPushButton(self.layoutWidget)
        self.btnDel.setObjectName(_fromUtf8("btnDel"))
        self.verticalLayout.addWidget(self.btnDel)
        self.btnFileSave = QtGui.QPushButton(self.layoutWidget)
        self.btnFileSave.setObjectName(_fromUtf8("btnFileSave"))
        self.verticalLayout.addWidget(self.btnFileSave)
        self.btnGen = QtGui.QPushButton(self.layoutWidget)
        self.btnGen.setMinimumSize(QtCore.QSize(111, 0))
        self.btnGen.setObjectName(_fromUtf8("btnGen"))
        self.verticalLayout.addWidget(self.btnGen)
        mwgainostk.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(mwgainostk)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 255, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuGaInOS_Studio = QtGui.QMenu(self.menubar)
        self.menuGaInOS_Studio.setObjectName(_fromUtf8("menuGaInOS_Studio"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        mwgainostk.setMenuBar(self.menubar)
        self.statusBar = QtGui.QStatusBar(mwgainostk)
        self.statusBar.setObjectName(_fromUtf8("statusBar"))
        mwgainostk.setStatusBar(self.statusBar)
        self.actionInfo = QtGui.QAction(mwgainostk)
        self.actionInfo.setObjectName(_fromUtf8("actionInfo"))
        self.actionAbout = QtGui.QAction(mwgainostk)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.actionNew = QtGui.QAction(mwgainostk)
        self.actionNew.setObjectName(_fromUtf8("actionNew"))
        self.actionOpen = QtGui.QAction(mwgainostk)
        self.actionOpen.setObjectName(_fromUtf8("actionOpen"))
        self.actionOpen_Recent_Files = QtGui.QAction(mwgainostk)
        self.actionOpen_Recent_Files.setObjectName(_fromUtf8("actionOpen_Recent_Files"))
        self.actionClose = QtGui.QAction(mwgainostk)
        self.actionClose.setObjectName(_fromUtf8("actionClose"))
        self.actionSave = QtGui.QAction(mwgainostk)
        self.actionSave.setObjectName(_fromUtf8("actionSave"))
        self.actionSave_As = QtGui.QAction(mwgainostk)
        self.actionSave_As.setObjectName(_fromUtf8("actionSave_As"))
        self.actionQuit = QtGui.QAction(mwgainostk)
        self.actionQuit.setObjectName(_fromUtf8("actionQuit"))
        self.menuGaInOS_Studio.addAction(self.actionOpen)
        self.menuGaInOS_Studio.addAction(self.actionNew)
        self.menuGaInOS_Studio.addAction(self.actionOpen_Recent_Files)
        self.menuGaInOS_Studio.addSeparator()
        self.menuGaInOS_Studio.addAction(self.actionClose)
        self.menuGaInOS_Studio.addSeparator()
        self.menuGaInOS_Studio.addAction(self.actionSave)
        self.menuGaInOS_Studio.addAction(self.actionSave_As)
        self.menuGaInOS_Studio.addSeparator()
        self.menuGaInOS_Studio.addAction(self.actionQuit)
        self.menuHelp.addAction(self.actionInfo)
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuGaInOS_Studio.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(mwgainostk)
        QtCore.QMetaObject.connectSlotsByName(mwgainostk)

    def retranslateUi(self, mwgainostk):
        mwgainostk.setWindowTitle(QtGui.QApplication.translate("mwgainostk", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.trModule.headerItem().setText(0, QtGui.QApplication.translate("mwgainostk", "Module", None, QtGui.QApplication.UnicodeUTF8))
        self.btnAdd.setText(QtGui.QApplication.translate("mwgainostk", "Add", None, QtGui.QApplication.UnicodeUTF8))
        self.btnEdit.setText(QtGui.QApplication.translate("mwgainostk", "Edit", None, QtGui.QApplication.UnicodeUTF8))
        self.btnDel.setText(QtGui.QApplication.translate("mwgainostk", "Remove", None, QtGui.QApplication.UnicodeUTF8))
        self.btnFileSave.setText(QtGui.QApplication.translate("mwgainostk", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.btnGen.setText(QtGui.QApplication.translate("mwgainostk", "^_^Gen^_^", None, QtGui.QApplication.UnicodeUTF8))
        self.menuGaInOS_Studio.setTitle(QtGui.QApplication.translate("mwgainostk", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.menuHelp.setTitle(QtGui.QApplication.translate("mwgainostk", "Help", None, QtGui.QApplication.UnicodeUTF8))
        self.actionInfo.setText(QtGui.QApplication.translate("mwgainostk", "Info", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbout.setText(QtGui.QApplication.translate("mwgainostk", "About", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNew.setText(QtGui.QApplication.translate("mwgainostk", "New", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOpen.setText(QtGui.QApplication.translate("mwgainostk", "Open", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOpen_Recent_Files.setText(QtGui.QApplication.translate("mwgainostk", "Open Recent Files", None, QtGui.QApplication.UnicodeUTF8))
        self.actionClose.setText(QtGui.QApplication.translate("mwgainostk", "Close", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave.setText(QtGui.QApplication.translate("mwgainostk", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave_As.setText(QtGui.QApplication.translate("mwgainostk", "Save As ...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionQuit.setText(QtGui.QApplication.translate("mwgainostk", "Quit", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    mwgainostk = QtGui.QMainWindow()
    ui = Ui_mwgainostk()
    ui.setupUi(mwgainostk)
    mwgainostk.show()
    sys.exit(app.exec_())

