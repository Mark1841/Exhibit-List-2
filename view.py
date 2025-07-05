from PyQt6.QtWidgets import (
    QMainWindow,
    QWidget,
    QGridLayout,
    QFormLayout,
    QTextEdit,
    QPushButton,
    QLabel,
    QLineEdit
)
from PyQt6.QtCore import Qt

# Create the main window
class MainWindow(QMainWindow):
    """ This class craetes the main window """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Set main window
        self.setWindowTitle('Exhibit List')
        self.setStyleSheet("QPushButton {min-Width: 90px; min-height: 30px; }")

        # Create button menu
        self.button_new_project = QPushButton('New Project')
        self.button_open_project = QPushButton('Open Project')
        self.button_add_exhibit = QPushButton('Add Exhibit')
        self.button_delete_exhibit = QPushButton('Delete Exhibit')
        self.button_view_exhibits = QPushButton('View Exhibits')
        self.button_close = QPushButton('Close')

        # Create database info section
        self.label_exhibits_total = QLabel('<b>Total Exhibits:</b>')
        self.label_exhibits_count = QLabel()

        # Create Exhibit information section
        self.textbox_exhibit_number = QLineEdit()
        self.button_get_exhibit = QPushButton('Get')
        self.button_update = QPushButton('Update')
        self.button_clear = QPushButton('Clear')
        self.textbox_property_tag = QLineEdit()
        self.textbox_seal = QLineEdit()
        self.textbox_seal_date = QLineEdit()
        self.textbox_seal_time = QLineEdit()
        self.textbox_description = QLineEdit()
        self.textbox_location = QLineEdit()
        self.textbox_seized_from = QLineEdit()
        self.textbox_seized_date = QLineEdit()
        self.textbox_seized_by = QLineEdit()
        self.textbox_seized_time = QLineEdit()
        self.textbox_photo_number = QLineEdit()
        self.textbox_placard_number = QLineEdit()
        self.textbox_cfs_number = QLineEdit()
        self.textbox_note = QLineEdit()
        self.button_add_note = QPushButton('Add Note')
        self.textedit_notes = QTextEdit()
        self.textbox_xfer_from = QLineEdit()
        self.textbox_xfer_to = QLineEdit()
        self.textbox_xfer_date = QLineEdit()
        self.textbox_xfer_time = QLineEdit()
        self.button_add_continuity = QPushButton('Add Continuity')
        self.textedit_continuity = QTextEdit()

        # Set variable for labels to align to the right
        rightalign = Qt.AlignmentFlag.AlignRight

        # Add  widgets to grid layout
        # Widget(row, column, rowspan, columnspan, alignment)
        mainwindow_layout = QGridLayout()
        mainwindow_layout.addWidget(self.button_new_project,0,0)
        mainwindow_layout.addWidget(self.button_open_project,1,0)
        mainwindow_layout.addWidget(self.button_add_exhibit,2,0)
        mainwindow_layout.addWidget(self.button_delete_exhibit,3,0)
        mainwindow_layout.addWidget(self.button_view_exhibits,4, 0)
        mainwindow_layout.addWidget(self.button_close,5,0)
        mainwindow_layout.addWidget(self.label_exhibits_total,7,0)
        mainwindow_layout.addWidget(self.label_exhibits_count,8,0)
        mainwindow_layout.addWidget(QLabel('Property Tag: '),0,1,1,1,rightalign)
        mainwindow_layout.addWidget(self.textbox_property_tag,0,2)
        mainwindow_layout.addWidget(self.button_get_exhibit,0,4)
        mainwindow_layout.addWidget(self.button_update,0,5)
        mainwindow_layout.addWidget(self.button_clear,0,6)
        mainwindow_layout.addWidget(QLabel('Exhibit Number: ') ,1,1,1,1,rightalign)
        mainwindow_layout.addWidget(self.textbox_exhibit_number,1,2)
        mainwindow_layout.addWidget(QLabel('Seal: ') ,1,3,1,1,rightalign)
        mainwindow_layout.addWidget(self.textbox_seal,1,4)
        mainwindow_layout.addWidget(QLabel('Seal Date: ') ,1,5,1,1,rightalign)
        mainwindow_layout.addWidget(QLabel('Seal Time: ') ,2,5,1,1,rightalign)
        mainwindow_layout.addWidget(self.textbox_seal_date,1,6)
        mainwindow_layout.addWidget(self.textbox_seal_time,2,6)
        mainwindow_layout.addWidget(QLabel('Description: ') ,3,1,1,1,rightalign)
        mainwindow_layout.addWidget(self.textbox_description,3,2,1,4)
        mainwindow_layout.addWidget(QLabel('Location: ') ,4,1,1,1,rightalign)
        mainwindow_layout.addWidget(self.textbox_location,4,2,1,4)
        mainwindow_layout.addWidget(QLabel('Seized From: ') ,5,1,1,1,rightalign)
        mainwindow_layout.addWidget(self.textbox_seized_from,5,2)
        mainwindow_layout.addWidget(QLabel('Seized Date: '),5,3,1,1,rightalign)
        mainwindow_layout.addWidget(self.textbox_seized_date,5,4)
        mainwindow_layout.addWidget(QLabel('Seized By: ') ,6,1,1,1,rightalign)
        mainwindow_layout.addWidget(self.textbox_seized_by,6,2)
        mainwindow_layout.addWidget(QLabel('Seized Time: ') ,5,5,1,1,rightalign)
        mainwindow_layout.addWidget(self.textbox_seized_time,5,6)
        mainwindow_layout.addWidget(QLabel('Photo_number: ') ,7,1,1,1,rightalign)
        mainwindow_layout.addWidget(self.textbox_photo_number,7,2)
        mainwindow_layout.addWidget(QLabel('Placard_number: ') ,7,3,1,1,rightalign)
        mainwindow_layout.addWidget(self.textbox_placard_number,7,4)
        mainwindow_layout.addWidget(QLabel('CFS Number: ') ,7,5,1,1,rightalign)
        mainwindow_layout.addWidget(self.textbox_cfs_number,7,6)
        mainwindow_layout.addWidget(QLabel('Note: ') ,8,1,1,1,rightalign)
        mainwindow_layout.addWidget(self.textbox_note,8,2,1,4)
        mainwindow_layout.addWidget(self.button_add_note,8,6)
        mainwindow_layout.addWidget(self.textedit_notes,9,2,1,6)
        mainwindow_layout.addWidget(QLabel('<b>   -----        Continuity        -----   </b>') ,10,3,1,6, Qt.AlignmentFlag.AlignCenter)
        mainwindow_layout.addWidget(QLabel('Transfer From: ') ,11,1,1,1, rightalign)
        mainwindow_layout.addWidget(self.textbox_xfer_from,11,2,1,1)
        mainwindow_layout.addWidget(QLabel('Transfer To: ') ,12,1,1,1, rightalign)
        mainwindow_layout.addWidget(self.textbox_xfer_to,12,2,1,1)
        mainwindow_layout.addWidget(QLabel('Transfer Date: ') ,13,1,1,1, rightalign)
        mainwindow_layout.addWidget(self.textbox_xfer_date,13,2,1,1)
        mainwindow_layout.addWidget(QLabel('Transfer Time: ') ,14,1,1,1, rightalign)
        mainwindow_layout.addWidget(self.textbox_xfer_time, 14,2,1,1)
        mainwindow_layout.addWidget(self.button_add_continuity,15,2)
        mainwindow_layout.addWidget(self.textedit_continuity,11,3,5,4)


        # Set layout and add to main window
        mainwindow_layout.setContentsMargins(20,20,20,20)
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        central_widget.setLayout(mainwindow_layout)
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
        
        # Set the layout for the widget
        self.setLayout(add_exhibit_layout)
# Delete Exhibit widgit code
class DeleteExhibitWindow(QWidget):
    """ This method creates the delete exhibit widget """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Set the main window
        self.setWindowTitle('Delete Exhibit')
        self.setStyleSheet("QPushButton {min-Width: 100px; min-height: 40px; }")

        # Top: Enter your information
        self.label_exhibit_number = QLabel('Exhibit Number You Wish to Delete')
        self.textbox_exhibit_number = QLineEdit()
        self.button_delete_exhibit = QPushButton('Delete Exhibit')

        # Middle: Displaying the exhibit information
        self.label_exhibit_info = QLabel('Exhibit Information')
        self.label_exhibit_info.setWordWrap(True)

        # Bottom: Confirm or Cancel
        self.button_confirm_delete = QPushButton("Confirm deletion")
        self.button_cancel_delete = QPushButton("Cancel deletion")
        

        # Layout
        delete_exhibit_layout = QFormLayout()
        delete_exhibit_layout.addRow(self.label_exhibit_number, self.textbox_exhibit_number)
        delete_exhibit_layout.addRow(self.button_delete_exhibit)
        delete_exhibit_layout.addRow(QLabel('Exhibit Info:'))
        delete_exhibit_layout.addRow(self.label_exhibit_info)
        delete_exhibit_layout.addRow(self.button_confirm_delete, self.button_cancel_delete)

        self.setLayout(delete_exhibit_layout)
