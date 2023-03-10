import barcode
from barcode.writer import ImageWriter
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from glob import glob
import qrcode, os  # I know, PEP8 :)
from PIL import Image


class Ui_Form(object):
    def __init__(self):
        self.pushButton = None
        self.pushButton_2 = None
        self.numbers_from_txt = []
        if not os.path.exists('Codes'):  # Create folder if dosen't exist
            os.mkdir('Codes')
        if not os.path.exists('OneFile'):  # Create folder if dosen't exist
            os.mkdir('OneFile')

    def setupUi(self, form):
        form.setObjectName("Form")
        form.resize(250, 200)
        form.setMaximumSize(QtCore.QSize(250, 200))
        form.setMinimumSize(QtCore.QSize(250, 200))
        self.pushButton = QtWidgets.QPushButton(form)
        self.pushButton.setGeometry(QtCore.QRect(70, 30, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.open_file)  # Open file button
        self.pushButton_2 = QtWidgets.QPushButton(form)
        self.pushButton_2.setEnabled(False)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 100, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.to_barcode)  # Generate barcode button
        self.pushButton_3 = QtWidgets.QPushButton(form)
        self.pushButton_3.setEnabled(False)
        self.pushButton_3.setGeometry(QtCore.QRect(140, 100, 93, 28))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.to_qr)  # Generate QR button
        self.label = QtWidgets.QLabel(form)
        self.label.setGeometry(QtCore.QRect(10, 70, 241, 16))
        self.label.setObjectName("label")
        self.radioButton = QtWidgets.QRadioButton(form)  # One file radio button
        self.radioButton.setEnabled(True)
        self.radioButton.setGeometry(QtCore.QRect(20, 140, 95, 20))
        self.radioButton.setChecked(False)
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(form)  # Separated file radio button
        self.radioButton_2.setGeometry(QtCore.QRect(110, 140, 111, 20))
        self.radioButton_2.setChecked(True)
        self.radioButton_2.setObjectName("radioButton_2")

        self.retranslateUi(form)
        QtCore.QMetaObject.connectSlotsByName(form)

    def retranslateUi(self, form):
        _translate = QtCore.QCoreApplication.translate
        form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "Open File"))
        self.pushButton_2.setText(_translate("Form", "To barcode"))
        self.pushButton_3.setText(_translate("Form", "To QR"))
        self.label.setText(_translate("Form", "Select file"))
        self.radioButton.setText(_translate("Form", "One file"))
        self.radioButton_2.setText(_translate("Form", "Separate files"))

    def open_file(self):
        self.label.setText('works')
        file_name = QFileDialog.getOpenFileName(None, "Open File", "", "All files (*.*);;Text files (*.txt)")
        if file_name:
            self.label.setText(file_name[0])
            self.pushButton_2.setEnabled(True)  # Enable buttons 2 and 3
            self.pushButton_3.setEnabled(True)
        try:  # Open file and read numbers with separate lines
            for path in glob(f'{file_name[0]}'):
                with open(path, 'rt') as f:
                    for line in f:
                        line = line.strip('\n')
                        self.numbers_from_txt.append(line)
        except:
            self.label.setText("File error")

    def one_file(self):
        try:
            items = os.listdir("Codes/")
            pic_height = 0
            for item in items:
                IMG1 = Image.open("Codes/" + item)
                if not pic_height:
                    new_image = Image.new('RGB', (IMG1.width, IMG1.height * len(items)))
                new_image.paste(IMG1, (0, IMG1.height * pic_height))
                pic_height += 1
            new_image.save('OneFile/file1.png')
        except Exception as e:
            print(e)

    def to_barcode(self):  # Generate barcodes
        try:
            for i in self.numbers_from_txt:
                number = i
                barcode_format = barcode.get_barcode_class('code39')
                my_barcode = barcode_format(number, writer=ImageWriter(), add_checksum=False)
                my_barcode.save(f"Codes/{i}")
                self.label.setText("Done")
        except:
            self.label.setText("Barcode error")
        if self.radioButton.isChecked():  # Create one file with images
            self.one_file()

    def to_qr(self):  # Generate QR codes
        try:
            for i in self.numbers_from_txt:
                my_qr = qrcode.make('abcd')
                my_qr.save(f"Codes/{i}.png")
                self.label.setText("Done")
        except:
            self.label.setText("QR error")
        if self.radioButton.isChecked():  # Create one file with images
            self.one_file()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
