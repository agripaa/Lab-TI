from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import QFont

def main():
    global app, window, nama_textbox, npm_textbox, kelas_textbox

    app = QApplication([])

    window = QWidget()
    window.setGeometry(400, 200, 400, 300)
    window.setWindowTitle("Pertemuan 6 - 50323070")

    layout = QVBoxLayout()
    layout.setSpacing(10)
    layout.setContentsMargins(20,20,20,20)

    label_judul = QLabel("MASUKKAN DATA DIRI ANDA")

    label_judul.setAlignment(Qt.AlignCenter)
    label_judul.setFont(QFont("Arial", 16, QFont.Bold))
    label_judul.setStyleSheet("color: #3498db;")

    label_nama = QLabel("Nama")
    label_npm = QLabel("NPM")
    label_kelas = QLabel("Kelas")

    labels = [label_nama, label_npm, label_kelas]

    for label in labels:
        label.setFont(QFont("Arial", 12))
        label.setStyleSheet("color: #2c3e60;")

    nama_textbox = QLineEdit()
    npm_textbox = QLineEdit()
    kelas_textbox = QLineEdit()

    nama_textbox.setPlaceholderText('Masukan Nama Anda')
    npm_textbox.setPlaceholderText('Masukan NPM Anda')
    kelas_textbox.setPlaceholderText('Masukan Kelas Anda')

    textboxes = [nama_textbox, npm_textbox, kelas_textbox]
    
    for textbox in textboxes:
        textbox.setFont(QFont("Arial", 12))
        textbox.setStyleSheet('padding: 5px; border: 1px solid #bdc3c7; border-radius: 5px')
    
    button_input = QPushButton("Input Data")
    button_input.setFont(QFont(QFont("Arial",12, QFont.Bold)))
    button_input.setStyleSheet("background-color: #2ecc71;")
    button_input.clicked.connect(on_clicked)
    
    layout.addWidget(label_judul)
    layout.addWidget(label_nama)
    layout.addWidget(nama_textbox)
    layout.addWidget(label_npm)
    layout.addWidget(npm_textbox)
    layout.addWidget(label_kelas)
    layout.addWidget(kelas_textbox)
    layout.addWidget(button_input, alignment=Qt.AlignCenter)
    
    window.setLayout(layout)
    window.show()
    app.exec_()
    
def on_clicked():
    if nama_textbox.text() and npm_textbox.text() and kelas_textbox.text():
        message = QMessageBox()
        message.setStyleSheet("background-color: #ecf0f1")
        message.information(window, "Data Diri", "Nama:" + nama_textbox.text() + "\nNPM:" + npm_textbox.text() + "\nKelas" + kelas_textbox.text())

        nama_textbox.setText("")
        npm_textbox.setText("")
        kelas_textbox.setText("")
    else:
        message = QMessageBox()
        message.setStyleSheet("background-color: #ecf0f1")
        message.warning(window, "Input Error", "Semua Input Harus Diisi!")
        
if __name__ == "__main__":
    main()