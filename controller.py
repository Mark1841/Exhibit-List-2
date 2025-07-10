from view import MainWindow, AddExhibitWindow, DeleteExhibitWindow, QLineEdit
from PyQt6.QtWidgets import QMessageBox
from model import Exhibit, Continuity
import model
import sys


class Controller:
    """ The controller takes care of the application logic """
    def __init__(self):
        self.main_view = MainWindow()
        self.add_exhibit_view = AddExhibitWindow()
        self.delete_exhibit_view = DeleteExhibitWindow()
        self.initialise_buttons()

        self.main_view.label_exhibits_count.setText(str(self.count_exhibits())) #This is not working properly and I dont know why!!!!

    # Attach methods to buttons from the view class
    def initialise_buttons(self):
        # Main menu buttons
        self.main_view.button_add_exhibit.clicked.connect(lambda: self.add_exhibit_view.show())
        self.main_view.button_delete_exhibit.clicked.connect(lambda: self.delete_exhibit_view.show())
        self.add_exhibit_view.button_add_exhibit_okay.clicked.connect(self.add_exhibit)
        self.main_view.button_close.clicked.connect(lambda: sys.exit())

        # Exhibit form buttons
        self.main_view.button_get_exhibit.clicked.connect(self.query_by_property_tag)
        self.main_view.button_add_continuity.clicked.connect(self.add_continuity)


        # linking cancel buttons
        self.add_exhibit_view.button_add_exhibit_cancel.clicked.connect(self.cancel_add_exhibit)
        self.delete_exhibit_view.button_cancel_delete.clicked.connect(self.cancel_delete)

        # linking delete button
        self.delete_exhibit_view.button_delete_exhibit.clicked.connect(self.find_exhibit_for_delete)
        self.delete_exhibit_view.button_confirm_delete.clicked.connect(self.confirm_deletion)

    
    # Cancel buttons
    def cancel_add_exhibit(self):
        self.clear_form(self.add_exhibit_view)
        self.add_exhibit_view.hide()

    def cancel_delete(self):
        self.clear_form(self.delete_exhibit_view)
        self.delete_exhibit_view.hide()

    # Delete button
    def find_exhibit_for_delete(self):
        exhibit_number = self.delete_exhibit_view.textbox_exhibit_number.text()
        # Simple query to find the exhibit in the database by the exhibit number 
        # also grabs the first result of said query
        exhibit = model.session.query(Exhibit).filter_by(exhibit_number=exhibit_number).first()
        if exhibit is None:
            self.delete_exhibit_view.label_exhibit_info.setText("<b>Exhibit not found</b>")
        else:
            info = (
                f"<b>Property Tag:</b> {exhibit.property_tag}<br>"
                f"<b>Description:</b> {exhibit.description}<br>"
                f"<b>Location:</b> {exhibit.location}<br>"
                f"<b>Seized From:</b> {exhibit.seized_from}<br>"
                f"<b>Seized By:</b> {exhibit.seized_by}<br>"
            )
            self.delete_exhibit_view.label_exhibit_info.setText(info)

    # Actually deletes the exhibit from the database
    def confirm_deletion(self):
        exhibit_number = self.delete_exhibit_view.textbox_exhibit_number.text()
        exhibit = model.session.query(Exhibit).filter_by(exhibit_number=exhibit_number).first()

        if exhibit is None:
            self.delete_exhibit_view.label_exhibit_info.setText("<b>Exhibit not found</b>")
        else:
            model.session.delete(exhibit)
            model.session.commit()
            self.delete_exhibit_view.label_exhibit_info.setText("<b>Exhibit has been deleted!</b>")
            self.clear_form(self.delete_exhibit_view)

    # Collect data from the add_exhibit_window and add to the database
    def add_exhibit(self):
        new_exhibit = Exhibit(
            exhibit_number = self.add_exhibit_view.textbox_exhibit_number.text(),
            placard_number = self.add_exhibit_view.textbox_placard_number.text(),
            property_tag = self.add_exhibit_view.textbox_property_tag.text(),
            cfs_number = self.add_exhibit_view.textbox_cfs_number.text(),
            photograph_number = self.add_exhibit_view.textbox_photograph_number.text(),
            description = self.add_exhibit_view.textbox_description.text(),
            location = self.add_exhibit_view.textbox_location.text(),
            results = self.add_exhibit_view.textbox_results.text(),
            seized_from = self.add_exhibit_view.textbox_seized_from.text(),
            seized_by = self.add_exhibit_view.textbox_seized_by.text(),
            seized_date_time = f'{self.add_exhibit_view.textbox_seized_date.text()} {self.add_exhibit_view.textbox_seized_time.text()}',
            seal_number = self.add_exhibit_view.textbox_seal_number.text(),
            seal_date_time = f'{self.add_exhibit_view.textbox_seal_date.text()} {self.add_exhibit_view.textbox_seal_time.text()}'
            )

        # Update the database with exhibit and close the session
        model.session.add(new_exhibit)
        model.session.commit()
        model.session.close()

        #Clear Line Edit boxes on the form and close window
        self.clear_form(self.add_exhibit_view)
        self.add_exhibit_view.hide()

    # Add continuity entries to the database
    def add_continuity(self):
        new_continuity = Continuity(
            xfer_from = self.main_view.textbox_xfer_from.text(),
            xfer_to = self.main_view.textbox_xfer_to.text(),
            xfer_date_time = f'{self.main_view.textbox_xfer_date.text()} - {self.main_view.textbox_xfer_time.text()}',
            exhibit_id = self.main_view.textbox_exhibit_number.text()
        )

        # Update the database with continuity and close the session
        model.session.add(new_continuity)
        model.session.commit()
        model.session.close()

        # Clear the add continuity text boxes
        self.main_view.textbox_xfer_from.clear()
        self.main_view.textbox_xfer_to.clear()
        self.main_view.textbox_xfer_date.clear()
        self.main_view.textbox_xfer_time.clear()

    # Look up a row in the database by property tag and populate textboxes
    def query_by_property_tag(self):
        exhibit_to_find = self.main_view.textbox_property_tag.text()
        exhibit = model.session.query(Exhibit).filter_by(property_tag=exhibit_to_find).first()
        print(exhibit)

        if exhibit == None:
            # Display a dialog box saying exhibit not found
            not_found_message = QMessageBox()
            not_found_message.setWindowTitle("Exhibit Not Found")
            not_found_message.setText(f"Exhibit with property tag '{exhibit_to_find}' not found.")
            not_found_message.setIcon(QMessageBox.Icon.Warning)
            not_found_message.exec()

            self.clear_form(self.main_view)
        else:
            # populate the main_view with all of the exhibit information
            self.main_view.textbox_exhibit_number.setText(str(exhibit.exhibit_number))
            self.main_view.textbox_seal.setText(str(exhibit.seal_number))
            self.main_view.textbox_cfs_number.setText(str(exhibit.cfs_number))
            self.main_view.textbox_placard_number.setText(str(exhibit.placard_number))
            self.main_view.textbox_description.setText(str(exhibit.description))
            self.main_view.textbox_location.setText(str(exhibit.location))
            self.main_view.textbox_photo_number.setText(str(exhibit.photograph_number))
            self.main_view.textbox_seized_from.setText(str(exhibit.seized_from))
            self.main_view.textbox_seized_by.setText(str(exhibit.seized_by))

            # Now fixed
            # Check if the seized_date_time is None or empty and split it into date and time
            # If it is None or empty, set the textboxes to "N/A"
            try:
                date, time = exhibit.seized_date_time.split()
                self.main_view.textbox_seized_date.setText(str(date))
                self.main_view.textbox_seized_time.setText(str(time))
            except Exception:
                self.main_view.textbox_seized_date.setText("N/A")
                self.main_view.textbox_seized_time.setText("N/A")

            try:
                date, time = exhibit.seal_date_time.split()
                self.main_view.textbox_seal_date.setText(str(date))
                self.main_view.textbox_seal_time.setText(str(time))
            except Exception:
                self.main_view.textbox_seal_date.setText("N/A")
                self.main_view.textbox_seal_time.setText("N/A")


        model.session.close()

    # Clear all of the textboxes on GUI window or widget
    def clear_form(self, form):
        for line_edit in form.findChildren(QLineEdit):
            line_edit.clear()

    # Count the number of exhibits in the database - *** Bug issue created for Ethan ***
    def count_exhibits(self):
        exhibit_count =  model.session.query(Exhibit).count()
        model.session.close()        
        return exhibit_count

