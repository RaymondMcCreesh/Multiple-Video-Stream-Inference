import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel

def on_button_click():
    label.setText('Hello, World!')

def main():
    app = QApplication(sys.argv)

    window = QWidget()
    window.setWindowTitle('My Second Qt5 App')

    layout = QVBoxLayout()

    button = QPushButton('Click me!')
    button.clicked.connect(on_button_click)
    layout.addWidget(button)

    label = QLabel('Hello, World!')
    layout.addWidget(label)

    window.setLayout(layout)
    window.show()

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()