from view import MainWindow, AddExhibitWindow
from model import Exhibit
import model

class Controller:
    """ The controller takes care of the application logic """
    def __init__(self):
        print('Controller created')
        self.main_view = MainWindow()
        self.add_exhibit_view = AddExhibitWindow()
        self.initialise_buttons()

    # Attach methods to buttons from the view class
    def initialise_buttons(self):
        self.main_view.button_add_exhibit.clicked.connect(self.show_add_exhibit_form)
        self.add_exhibit_view.button_add_exhibit_okay.clicked.connect(self.add_exhibit)

    # Show the add_exhibit window when add exhibit button is clicked
    def show_add_exhibit_form(self):
        self.add_exhibit_view.show()

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
        