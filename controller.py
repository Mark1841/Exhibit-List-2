from view import MainWindow, AddExhibitWindow, AddContinuityWindow, DeleteExhibitWindow, QLineEdit
from model import Exhibit, Continuity
import model
import sys


class Controller:
    """ The controller takes care of the application logic """
    def __init__(self):
        self.main_view = MainWindow()
        self.add_exhibit_view = AddExhibitWindow()
        self.add_continuity_view = AddContinuityWindow()
        self.delete_exhibit_view = DeleteExhibitWindow()
        self.initialise_buttons()

    # Attach methods to buttons from the view class
    def initialise_buttons(self):
        self.add_continuity_view.button_exhibit_number_check.clicked.connect(self.query_by_exhibit_number)
        self.main_view.button_add_exhibit.clicked.connect(self.show_add_exhibit_form)
        self.main_view.button_add_continuity.clicked.connect(self.show_add_continuity_form)
        self.add_exhibit_view.button_add_exhibit_okay.clicked.connect(self.add_exhibit)
        self.add_continuity_view.button_add_continuity.clicked.connect(self.add_continuity)
        self.main_view.button_close.clicked.connect(self.close_app)
        self.main_view.button_delete_exhibit.clicked.connect(self.show_delete_exhibit_form)

        # linking cancel buttons
        self.add_exhibit_view.button_add_exhibit_cancel.clicked.connect(self.cancel_add_exhibit)
        self.add_continuity_view.button_add_continuity_cancel.clicked.connect(self.cancel_add_continuity)
        self.delete_exhibit_view.button_cancel_delete.clicked.connect(self.cancel_delete)

        # linking delete button
        self.delete_exhibit_view.button_delete_exhibit.clicked.connect(self.find_exhibit_for_delete)
        self.delete_exhibit_view.button_confirm_delete.clicked.connect(self.confirm_deletion)


    # Show the add_exhibit window when add exhibit button is clicked
    def show_add_exhibit_form(self):
        self.add_exhibit_view.show()

    # Show the add_continuity window when add exhibit button is clicked
    def show_add_continuity_form(self):
        self.add_continuity_view.show()

    # Show the delete_exhibit window when delete exhibit button is clicked
    def show_delete_exhibit_form(self):
        self.delete_exhibit_view.show()
    
    # Cancel buttons
    def cancel_add_exhibit(self):
        self.clear_form(self.add_exhibit_view)
        self.add_exhibit_view.hide()

    def cancel_add_continuity(self):
        self.clear_form(self.add_continuity_view)
        self.add_continuity_view.hide()

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
            xfer_from = self.add_continuity_view.textbox_xfer_from.text(),
            xfer_to = self.add_continuity_view.textbox_xfer_to.text(),
            xfer_date_time = f'{self.add_continuity_view.textbox_xfer_date.text()} - {self.add_continuity_view.textbox_xfer_time.text()}',
            exhibit_id = self.add_continuity_view.textbox_continuity_exhibit_number.text()
        )

        # Update the database with continuity and close the session
        model.session.add(new_continuity)
        model.session.commit()
        model.session.close()

        # Clear Line Edit boxes on the form and close window
        self.clear_form(self.add_continuity_view)
        self.add_continuity_view.hide()

    # Look up a row in the database by exhibit number
    def query_by_exhibit_number(self):
        exhibit_to_find = self.add_continuity_view.textbox_continuity_exhibit_number.text()
        exhibit = model.session.query(Exhibit).filter_by(exhibit_number=exhibit_to_find).first()
        if exhibit == None:
            self.add_continuity_view.label_confirm_exhibit.setText('<b>That exhibit is not in the database</b>')
            self.add_continuity_view.textbox_continuity_exhibit_number.clear()
        else:
            self.add_continuity_view.label_confirm_exhibit.setText(f'<b>{exhibit.property_tag} - {exhibit.description}</b>')
        model.session.close()

    # Clear all of the textboxes on GUI window or widget
    def clear_form(self, form):
        for line_edit in form.findChildren(QLineEdit):
            line_edit.clear()

    # Terminate the application
    def close_app(self):
        sys.exit()

