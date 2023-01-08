import barcode
from barcode.writer import ImageWriter
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(215, 264)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(60, 30, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.open_file)
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(60, 100, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.to_barcode)
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(60, 140, 93, 28))
        self.pushButton_3.setObjectName("pushButton_3")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 70, 195, 16))
        self.label.setObjectName("label")
        self.radioButton = QtWidgets.QRadioButton(Form)
        self.radioButton.setGeometry(QtCore.QRect(50, 180, 95, 20))
        self.radioButton.setChecked(True)
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(Form)
        self.radioButton_2.setGeometry(QtCore.QRect(50, 210, 111, 20))
        self.radioButton_2.setObjectName("radioButton_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def to_barcode(self):
        try:
            barcode.Code128(code='123456', writer=ImageWriter).write('file.jpg')
        except Exception as e:
            print(e)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "Open File"))
        self.pushButton_2.setText(_translate("Form", "To barcode"))
        self.pushButton_3.setText(_translate("Form", "To QR"))
        self.label.setText(_translate("Form", "File"))
        self.radioButton.setText(_translate("Form", "One file"))
        self.radioButton_2.setText(_translate("Form", "Separate files"))

    def open_file(self):
        self.label.setText('works')
        file_name = QFileDialog.getOpenFileName(None, "Open File", "", "Text files (*.txt)")
        if file_name:
            self.label.setText(file_name[0])


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
