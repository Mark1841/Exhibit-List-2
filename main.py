import sys
from controller import Controller
from PyQt6.QtWidgets import QApplication

# Initialise the PyQt6 Application and Controller 
if __name__=="__main__":
    app = QApplication(sys.argv)
    controller = Controller()
    sys.exit(app.exec())



