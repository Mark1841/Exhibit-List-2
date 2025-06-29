from view import MainWindow, AddExhibitWindow, AddContinuityWindow
from model import Exhibit
import model
from sqlalchemy import select

class Controller:
    """ The controller takes care of the application logic """
    def __init__(self):
        print('Controller created')
        self.main_view = MainWindow()
        self.add_exhibit_view = AddExhibitWindow()
        self.add_continuity_view = AddContinuityWindow()
        self.initialise_buttons()

    # Attach methods to buttons from the view class
    def initialise_buttons(self):
        self.add_continuity_view.button_exhibit_number_check.clicked.connect(self.query_exhibits)
        self.main_view.button_add_exhibit.clicked.connect(self.show_add_exhibit_form)
        self.main_view.button_add_continuity.clicked.connect(self.show_add_continuity_form)
        self.add_exhibit_view.button_add_exhibit_okay.clicked.connect(self.add_exhibit)

    # Show the add_exhibit window when add exhibit button is clicked
    def show_add_exhibit_form(self):
        self.add_exhibit_view.show()

    # Show the add_continuity window when add exhibit button is clicked
    def show_add_continuity_form(self):
        self.add_continuity_view.show()

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

    def query_exhibits(self):
        exhibit_to_find = self.add_continuity_view.textbox_continuity_exhibit_number.text()
        exhibit = model.session.query(Exhibit).filter_by(exhibit_number=exhibit_to_find).first()
        if exhibit == None:
            self.add_continuity_view.label_confirm_exhibit.setText('That exhibit is not in the database')
            self.add_continuity_view.textbox_continuity_exhibit_number.clear()
        else:
            self.add_continuity_view.label_confirm_exhibit.setText(f'{exhibit.property_tag} - {exhibit.description}')
        model.session.close()

        
