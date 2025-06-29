import sys
from PyQt6.QtWidgets import QApplication
from controller import Controller


# Initialise the Controller 
if __name__=="__main__":
    app = QApplication(sys.argv)
    controller = Controller()
    sys.exit(app.exec())