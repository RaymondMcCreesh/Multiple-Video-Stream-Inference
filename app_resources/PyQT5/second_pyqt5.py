import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QTabWidget, QPushButton, QLabel, QComboBox

def on_button_click():
    label.setText('second pyqt5')

def on_combo_box_change(text):
    label.setText(text)

def main():
    app = QApplication(sys.argv)

    window = QWidget()
    window.setWindowTitle(' Qt5 App')

    # Set the minimum width of the window
    window.setMinimumWidth(500)

    # Alternatively, you can set the fixed width of the window
    # window.setFixedWidth(500)


    layout = QVBoxLayout()

    tab_widget = QTabWidget()

    # Tab 1
    tab1 = QWidget()
    tab1_layout = QVBoxLayout()

    button1 = QPushButton('Click me!')
    button1.clicked.connect(on_button_click)
    tab1_layout.addWidget(button1)

    label1 = QLabel('Hello, World!')
    tab1_layout.addWidget(label1)

    tab1.setLayout(tab1_layout)

    # Tab 2
    tab2 = QWidget()
    tab2_layout = QVBoxLayout()

    combo_box = QComboBox()
    combo_box.addItem('Option 1')
    combo_box.addItem('Option 2')
    combo_box.addItem('Option 3')
    combo_box.currentTextChanged.connect(on_combo_box_change)
    tab2_layout.addWidget(combo_box)

    label2 = QLabel('Hello, World!')
    tab2_layout.addWidget(label2)

    tab2.setLayout(tab2_layout)

    # Add tabs to tab widget
    tab_widget.addTab(tab1, 'Tab 1')
    tab_widget.addTab(tab2, 'Tab 2')

    layout.addWidget(tab_widget)

    window.setLayout(layout)
    window.show()

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()