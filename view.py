from PyQt6.QtWidgets import (
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QFormLayout,
    QPushButton,
    QLabel,
    QLineEdit
)

# Create the main window
class MainWindow(QMainWindow):
    """ This class craetes the main window """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Set main window
        self.setWindowTitle('Exhibit List')
        self.setStyleSheet("QPushButton {min-Width: 100px; min-height: 40px; }")

        # Create button menu
        self.button_add_exhibit = QPushButton('Add Exhibit')
        self.button_edit_exhibit = QPushButton('Edit Exhibit')
        self.button_delete_exhibit = QPushButton('Delete Exhibit')
        self.button_view_exhibits = QPushButton('View Exhibits')
        self.button_add_continuity = QPushButton('Add Continuity')
        self.button_edit_continuity = QPushButton('Edit Continuity')
        self.button_delete_continuity = QPushButton('Delete Continuity')
        self.button_close = QPushButton('Close')

        # Add  buttons to vertical layout
        button_layout = QVBoxLayout()
        button_layout.addWidget(self.button_add_exhibit)
        button_layout.addWidget(self.button_edit_exhibit)
        button_layout.addWidget(self.button_delete_exhibit)
        button_layout.addWidget(self.button_view_exhibits)
        button_layout.addWidget(self.button_add_continuity)
        button_layout.addWidget(self.button_edit_continuity)
        button_layout.addWidget(self.button_delete_continuity)
        button_layout.addWidget(self.button_close)

        # Set layout and add to main window
        widget = QWidget()
        widget.setLayout(button_layout)
        self.setCentralWidget(widget)
        self.show()

# Create the add exhibit window
class AddExhibitWindow(QWidget):
    """ This class creates the add exhibit window """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Set main window
        self.setWindowTitle('Add Exhibits')
        self.setStyleSheet("QPushButton {min-Width: 100px; min-height: 40px; }")

        # Create widgets for add exhibits window
        # Labels
        self.label_exhibit_number = QLabel('Exhibit Number')
        self.label_placard_number = QLabel('Placard Number')
        self.label_property_tag = QLabel('Property Tag')
        self.label_cfs_number = QLabel('CFS Number')
        self.label_photograph_number = QLabel('Photograph Number')
        self.label_description = QLabel('Exhibit Description')
        self.label_location = QLabel('Location')
        self.label_results = QLabel('Results')
        self.label_seized_from = QLabel('Seized From')
        self.label_seized_by = QLabel('Seized By')
        self.label_seized_date = QLabel('Seizure Date')
        self.label_seized_time = QLabel('Seizure Time')
        self.label_seal_number = QLabel('Seal Number')
        self.label_seal_date = QLabel('Seal Date')
        self.label_seal_time = QLabel('Seal Time')
        # Line Edit Boxes
        self.textbox_exhibit_number = QLineEdit()
        self.textbox_placard_number = QLineEdit()
        self.textbox_property_tag = QLineEdit()
        self.textbox_cfs_number = QLineEdit()
        self.textbox_photograph_number = QLineEdit()
        self.textbox_description = QLineEdit()
        self.textbox_location = QLineEdit()
        self.textbox_results = QLineEdit()
        self.textbox_seized_from = QLineEdit()
        self.textbox_seized_by = QLineEdit()
        self.textbox_seized_date = QLineEdit()
        self.textbox_seized_time = QLineEdit()
        self.textbox_seal_number = QLineEdit()
        self.textbox_seal_date = QLineEdit()
        self.textbox_seal_time = QLineEdit()
        # Buttons
        self.button_add_exhibit_next  =QPushButton('Next')
        self.button_add_exhibit_okay = QPushButton('Okay')
        self.button_add_exhibit_cancel = QPushButton('Cancel')

        # Create 'add exhibit' layout and add widgets
        add_exhibit_layout = QFormLayout()
        add_exhibit_layout.addRow(self.label_exhibit_number, self.textbox_exhibit_number)
        add_exhibit_layout.addRow(self.label_placard_number, self.textbox_placard_number)
        add_exhibit_layout.addRow(self.label_property_tag, self.textbox_property_tag)
        add_exhibit_layout.addRow(self.label_cfs_number, self.textbox_cfs_number)
        add_exhibit_layout.addRow(self.label_photograph_number, self.textbox_photograph_number)
        add_exhibit_layout.addRow(self.label_description, self.textbox_description)
        add_exhibit_layout.addRow(self.label_location, self.textbox_location)
        add_exhibit_layout.addRow(self.label_results, self.textbox_results)
        add_exhibit_layout.addRow(self.label_seized_from, self.textbox_seized_from)
        add_exhibit_layout.addRow(self.label_seized_by, self.textbox_seized_by)
        add_exhibit_layout.addRow(self.label_seized_date, self.textbox_seized_date)
        add_exhibit_layout.addRow(self.label_seized_time, self.textbox_seized_time)
        add_exhibit_layout.addRow(self.label_seal_number, self.textbox_seal_number)
        add_exhibit_layout.addRow(self.label_seal_date, self.textbox_seal_date)
        add_exhibit_layout.addRow(self.label_seal_time, self.textbox_seal_time)
        add_exhibit_layout.addRow(self.button_add_exhibit_okay, self.button_add_exhibit_next)
        add_exhibit_layout.addRow(self.button_add_exhibit_cancel)
        
        self.setLayout(add_exhibit_layout)