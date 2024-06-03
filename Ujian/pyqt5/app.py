from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import QFont


def main():
    global app, window, nama_textbox, npm_textbox, kelas_textbox, ujian_textbox

    app = QApplication([])
    window = QWidget()
    window.setGeometry(400, 200, 400, 400)
    window.setWindowTitle("Pertemuan Ujian")

    layout = QVBoxLayout()
    layout.setSpacing(10)
    layout.setContentsMargins(20, 20, 20, 20)

    label_judul = QLabel("Masukkan Data Ujian")
    label_judul.setAlignment(Qt.AlignCenter)
    label_judul.setFont(QFont("Arial", 16, QFont.Bold))
    label_judul.setStyleSheet("color: #1b1b1b;")

    label_nama = QLabel("Nama")
    label_npm = QLabel("NPM")
    label_kelas = QLabel("Kelas")
    label_ujian = QLabel("Ujian")

    labels = [label_nama, label_npm, label_kelas, label_ujian]
    for label in labels:
        label.setFont(QFont("Arial", 12))
        label.setStyleSheet("color: #2c3e50;")

    nama_textbox = QLineEdit()
    nama_textbox.setPlaceholderText("Masukkan Nama anda")
    npm_textbox = QLineEdit()
    npm_textbox.setPlaceholderText("Masukkan NPM anda")
    kelas_textbox = QLineEdit()
    kelas_textbox.setPlaceholderText("Masukkan Kelas anda")
    ujian_textbox = QLineEdit()
    ujian_textbox.setPlaceholderText("Masukkan Ujian anda")

    textboxes = [
        nama_textbox,
        npm_textbox,
        kelas_textbox,
        ujian_textbox,
    ]
    for textbox in textboxes:
        textbox.setFont(QFont("Arial", 12))
        textbox.setStyleSheet(
            "padding: 5px; border: 1px solid #bdc3c7; border-radius: 5px;"
        )

    button_input = QPushButton("INPUT DATA")
    button_input.setFont(QFont("Arial", 12, QFont.Bold))
    button_input.setStyleSheet(
        """
        QPushButton {
            background-color: #6495ed;
            width: 100%;
            color:  black;
            padding: 10px;
            border: none;
            border-radius: 5px;
        }
        QPushButton:hover {
            background-color: #4169e1 ;
        }
    """
    )
    button_input.clicked.connect(on_clicked)

    layout.addWidget(label_judul)
    for label, textbox in zip(labels, textboxes):
        layout.addWidget(label)
        layout.addWidget(textbox)
    layout.addWidget(button_input, alignment=Qt.AlignCenter)

    window.setLayout(layout)
    window.show()
    app.exec_()


def on_clicked():
    if (
        nama_textbox.text()
        and npm_textbox.text()
        and kelas_textbox.text()
        and ujian_textbox.text()
    ):
        message = QMessageBox()
        message.setStyleSheet(
            """
            QMessageBox {
                background-color: #ecf0f1;
            }
            QMessageBox QLabel {
                color: #2c3e50;
            }
            QMessageBox QPushButton {
                background-color: #3498db;
                color: white;
                padding: 5px;
                border: none;
                border-radius: 5px;
            }
            QMessageBox QPushButton:hover {
                background-color: #2980b9;
            }
        """
        )
        message.information(
            window,
            "Data Ujian",
            f"Nama: {nama_textbox.text()}\n"
            f"NPM: {npm_textbox.text()}\n"
            f"Kelas: {kelas_textbox.text()}\n"
            f"Ujian: {ujian_textbox.text()}\n"
        )
        nama_textbox.setText("")
        npm_textbox.setText("")
        kelas_textbox.setText("")
        ujian_textbox.setText("")
    else:
        message = QMessageBox()
        message.setStyleSheet(
            """
            QMessageBox {
                background-color: #f1c40f;
            }
            QMessageBox QLabel {
                color: #2c3e50;
            }
            QMessageBox QPushButton {
                background-color: #e67e22;
                color: white;
                padding: 5px;
                border: none;
                border-radius: 5px;
            }
            QMessageBox QPushButton:hover {
                background-color: #d35400;
            }
        """
        )
        message.warning(window, "Input Error", "Semua bidang harus diisi!")


if __name__ == "__main__":
    main()