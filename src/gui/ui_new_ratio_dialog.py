# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'resources/ui_new_ratio_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_NewRatioDialog(object):
    def setupUi(self, NewRatioDialog):
        NewRatioDialog.setObjectName("NewRatioDialog")
        NewRatioDialog.resize(447, 529)
        self.buttonBox = QtWidgets.QDialogButtonBox(NewRatioDialog)
        self.buttonBox.setGeometry(QtCore.QRect(40, 450, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.tabWidget = QtWidgets.QTabWidget(NewRatioDialog)
        self.tabWidget.setGeometry(QtCore.QRect(20, 50, 381, 251))
        self.tabWidget.setObjectName("tabWidget")
        self.presetTab = QtWidgets.QWidget()
        self.presetTab.setObjectName("presetTab")
        self.presetList = QtWidgets.QListWidget(self.presetTab)
        self.presetList.setGeometry(QtCore.QRect(40, 31, 256, 171))
        self.presetList.setObjectName("presetList")
        self.label_5 = QtWidgets.QLabel(self.presetTab)
        self.label_5.setGeometry(QtCore.QRect(40, 10, 131, 17))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setObjectName("label_5")
        self.tabWidget.addTab(self.presetTab, "")
        self.customTab = QtWidgets.QWidget()
        self.customTab.setObjectName("customTab")
        self.label_4 = QtWidgets.QLabel(self.customTab)
        self.label_4.setGeometry(QtCore.QRect(30, 20, 64, 17))
        self.label_4.setObjectName("label_4")
        self.customTypeCombo = QtWidgets.QComboBox(self.customTab)
        self.customTypeCombo.setGeometry(QtCore.QRect(90, 10, 271, 25))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.customTypeCombo.sizePolicy().hasHeightForWidth())
        self.customTypeCombo.setSizePolicy(sizePolicy)
        self.customTypeCombo.setObjectName("customTypeCombo")
        self.customTypeCombo.addItem("")
        self.customTypeCombo.addItem("")
        self.customTypeCombo.addItem("")
        self.elementACombo = QtWidgets.QComboBox(self.customTab)
        self.elementACombo.setGeometry(QtCore.QRect(10, 60, 71, 25))
        self.elementACombo.setObjectName("elementACombo")
        self.elementBCombo = QtWidgets.QComboBox(self.customTab)
        self.elementBCombo.setGeometry(QtCore.QRect(100, 60, 71, 25))
        self.elementBCombo.setObjectName("elementBCombo")
        self.elementCCombo = QtWidgets.QComboBox(self.customTab)
        self.elementCCombo.setGeometry(QtCore.QRect(190, 60, 71, 25))
        self.elementCCombo.setObjectName("elementCCombo")
        self.elementDCombo = QtWidgets.QComboBox(self.customTab)
        self.elementDCombo.setGeometry(QtCore.QRect(280, 60, 71, 25))
        self.elementDCombo.setObjectName("elementDCombo")
        self.tabWidget.addTab(self.customTab, "")
        self.label = QtWidgets.QLabel(NewRatioDialog)
        self.label.setGeometry(QtCore.QRect(60, 310, 64, 17))
        self.label.setObjectName("label")
        self.formulaLabel = QtWidgets.QLabel(NewRatioDialog)
        self.formulaLabel.setGeometry(QtCore.QRect(210, 310, 171, 17))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.formulaLabel.sizePolicy().hasHeightForWidth())
        self.formulaLabel.setSizePolicy(sizePolicy)
        self.formulaLabel.setObjectName("formulaLabel")
        self.label_3 = QtWidgets.QLabel(NewRatioDialog)
        self.label_3.setGeometry(QtCore.QRect(60, 360, 64, 17))
        self.label_3.setObjectName("label_3")
        self.nameEdit = QtWidgets.QLineEdit(NewRatioDialog)
        self.nameEdit.setGeometry(QtCore.QRect(210, 350, 113, 25))
        self.nameEdit.setObjectName("nameEdit")
        self.label_2 = QtWidgets.QLabel(NewRatioDialog)
        self.label_2.setGeometry(QtCore.QRect(20, 20, 351, 17))
        self.label_2.setObjectName("label_2")
        self.label_6 = QtWidgets.QLabel(NewRatioDialog)
        self.label_6.setGeometry(QtCore.QRect(50, 410, 131, 17))
        self.label_6.setObjectName("label_6")
        self.correctionModelCombo = QtWidgets.QComboBox(NewRatioDialog)
        self.correctionModelCombo.setGeometry(QtCore.QRect(210, 400, 191, 25))
        self.correctionModelCombo.setObjectName("correctionModelCombo")

        self.retranslateUi(NewRatioDialog)
        self.tabWidget.setCurrentIndex(1)
        self.buttonBox.accepted.connect(NewRatioDialog.accept)
        self.buttonBox.rejected.connect(NewRatioDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(NewRatioDialog)

    def retranslateUi(self, NewRatioDialog):
        _translate = QtCore.QCoreApplication.translate
        NewRatioDialog.setWindowTitle(_translate("NewRatioDialog", "New Element Ratio Map"))
        self.label_5.setText(_translate("NewRatioDialog", "Valid presets"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.presetTab), _translate("NewRatioDialog", "Preset"))
        self.label_4.setText(_translate("NewRatioDialog", "Type"))
        self.customTypeCombo.setItemText(0, _translate("NewRatioDialog", "Two elements: A / (A+B)"))
        self.customTypeCombo.setItemText(1, _translate("NewRatioDialog", "Three elements: A / (A+B+C)"))
        self.customTypeCombo.setItemText(2, _translate("NewRatioDialog", "Four elements: A / (A+B+C+D)"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.customTab), _translate("NewRatioDialog", "Custom"))
        self.label.setText(_translate("NewRatioDialog", "Formula"))
        self.formulaLabel.setText(_translate("NewRatioDialog", "TextLabel"))
        self.label_3.setText(_translate("NewRatioDialog", "Name"))
        self.label_2.setText(_translate("NewRatioDialog", "Select a Preset or define a Custom ratio"))
        self.label_6.setText(_translate("NewRatioDialog", "Correction model"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    NewRatioDialog = QtWidgets.QDialog()
    ui = Ui_NewRatioDialog()
    ui.setupUi(NewRatioDialog)
    NewRatioDialog.show()
    sys.exit(app.exec_())
