# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'resources/ui_main_window.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.splitter.sizePolicy().hasHeightForWidth())
        self.splitter.setSizePolicy(sizePolicy)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.tabWidget = QtWidgets.QTabWidget(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setObjectName("tabWidget")
        self.rawTab = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rawTab.sizePolicy().hasHeightForWidth())
        self.rawTab.setSizePolicy(sizePolicy)
        self.rawTab.setObjectName("rawTab")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.rawTab)
        self.verticalLayout.setContentsMargins(9, 9, 9, 9)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.rawTab)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.rawElementList = QtWidgets.QListWidget(self.rawTab)
        self.rawElementList.setObjectName("rawElementList")
        self.verticalLayout.addWidget(self.rawElementList)
        self.tabWidget.addTab(self.rawTab, "")
        self.filteredTab = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.filteredTab.sizePolicy().hasHeightForWidth())
        self.filteredTab.setSizePolicy(sizePolicy)
        self.filteredTab.setObjectName("filteredTab")
        self.tabWidget.addTab(self.filteredTab, "")
        self.layoutWidget = QtWidgets.QWidget(self.splitter)
        self.layoutWidget.setObjectName("layoutWidget")
        self.rightVerticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.rightVerticalLayout.setContentsMargins(0, 0, 0, 0)
        self.rightVerticalLayout.setObjectName("rightVerticalLayout")
        self.topRightHorizontalLayout = QtWidgets.QHBoxLayout()
        self.topRightHorizontalLayout.setObjectName("topRightHorizontalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.plotTypeLabel = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plotTypeLabel.sizePolicy().hasHeightForWidth())
        self.plotTypeLabel.setSizePolicy(sizePolicy)
        self.plotTypeLabel.setObjectName("plotTypeLabel")
        self.gridLayout.addWidget(self.plotTypeLabel, 0, 0, 1, 1)
        self.phaseLabel = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.phaseLabel.sizePolicy().hasHeightForWidth())
        self.phaseLabel.setSizePolicy(sizePolicy)
        self.phaseLabel.setObjectName("phaseLabel")
        self.gridLayout.addWidget(self.phaseLabel, 0, 1, 1, 1)
        self.regionLabel = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.regionLabel.sizePolicy().hasHeightForWidth())
        self.regionLabel.setSizePolicy(sizePolicy)
        self.regionLabel.setObjectName("regionLabel")
        self.gridLayout.addWidget(self.regionLabel, 0, 2, 1, 1)
        self.plotTypeComboBox = QtWidgets.QComboBox(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plotTypeComboBox.sizePolicy().hasHeightForWidth())
        self.plotTypeComboBox.setSizePolicy(sizePolicy)
        self.plotTypeComboBox.setObjectName("plotTypeComboBox")
        self.plotTypeComboBox.addItem("")
        self.plotTypeComboBox.addItem("")
        self.plotTypeComboBox.addItem("")
        self.gridLayout.addWidget(self.plotTypeComboBox, 1, 0, 1, 1)
        self.phaseComboBox = QtWidgets.QComboBox(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.phaseComboBox.sizePolicy().hasHeightForWidth())
        self.phaseComboBox.setSizePolicy(sizePolicy)
        self.phaseComboBox.setObjectName("phaseComboBox")
        self.gridLayout.addWidget(self.phaseComboBox, 1, 1, 1, 1)
        self.regionComboBox = QtWidgets.QComboBox(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.regionComboBox.sizePolicy().hasHeightForWidth())
        self.regionComboBox.setSizePolicy(sizePolicy)
        self.regionComboBox.setObjectName("regionComboBox")
        self.gridLayout.addWidget(self.regionComboBox, 1, 2, 1, 1)
        self.topRightHorizontalLayout.addLayout(self.gridLayout)
        self.dummyLabel = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dummyLabel.sizePolicy().hasHeightForWidth())
        self.dummyLabel.setSizePolicy(sizePolicy)
        self.dummyLabel.setObjectName("dummyLabel")
        self.topRightHorizontalLayout.addWidget(self.dummyLabel)
        self.rightVerticalLayout.addLayout(self.topRightHorizontalLayout)
        self.matplotlibWidget = MatplotlibWidget(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.matplotlibWidget.sizePolicy().hasHeightForWidth())
        self.matplotlibWidget.setSizePolicy(sizePolicy)
        self.matplotlibWidget.setObjectName("matplotlibWidget")
        self.rightVerticalLayout.addWidget(self.matplotlibWidget)
        self.verticalLayout_2.addWidget(self.splitter)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        self.menuProject = QtWidgets.QMenu(self.menubar)
        self.menuProject.setObjectName("menuProject")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionProjectNew = QtWidgets.QAction(MainWindow)
        self.actionProjectNew.setObjectName("actionProjectNew")
        self.actionProjectOpen = QtWidgets.QAction(MainWindow)
        self.actionProjectOpen.setObjectName("actionProjectOpen")
        self.actionProjectClose = QtWidgets.QAction(MainWindow)
        self.actionProjectClose.setObjectName("actionProjectClose")
        self.menuProject.addAction(self.actionProjectNew)
        self.menuProject.addAction(self.actionProjectOpen)
        self.menuProject.addAction(self.actionProjectClose)
        self.menubar.addAction(self.menuProject.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        self.plotTypeComboBox.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "QACD quack"))
        self.label.setText(_translate("MainWindow", "Elements"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.rawTab), _translate("MainWindow", "Raw"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.filteredTab), _translate("MainWindow", "Filtered"))
        self.plotTypeLabel.setText(_translate("MainWindow", "Plot type"))
        self.phaseLabel.setText(_translate("MainWindow", "Phase"))
        self.regionLabel.setText(_translate("MainWindow", "Region"))
        self.plotTypeComboBox.setItemText(0, _translate("MainWindow", "Map"))
        self.plotTypeComboBox.setItemText(1, _translate("MainWindow", "Histogram"))
        self.plotTypeComboBox.setItemText(2, _translate("MainWindow", "Map and histogram"))
        self.dummyLabel.setText(_translate("MainWindow", "Dummy"))
        self.menuProject.setTitle(_translate("MainWindow", "Project"))
        self.actionProjectNew.setText(_translate("MainWindow", "New"))
        self.actionProjectOpen.setText(_translate("MainWindow", "Open"))
        self.actionProjectClose.setText(_translate("MainWindow", "Close"))

from .matplotlib_widget import MatplotlibWidget

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

