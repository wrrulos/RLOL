import customtkinter
import webbrowser

from CTkMessagebox import CTkMessagebox

from src.participants.get_participants import GetParticipants
from src.managers.json_manager import JsonManager
from src.utilities.ctk_utilities import CTKUtilities


class HomeForm:
    def __init__(self, root) -> None:
        # Store input parameters.
        self.root = root

        # Create the main frame for UI components.
        self.main_frame = customtkinter.CTkFrame(self.root, fg_color='#000000')
        self.main_frame.pack(fill=customtkinter.BOTH, expand=True)

        # Initialize the auto-accept window.
        self.auto_accept_window = None

        # Call the method to initialize UI components.
        self.initialize_ui()

    def initialize_ui(self):
        """
        Initializes the user interface (UI) components.
        """

        self.create_images()
        self.create_buttons()
        self.create_text_labels()

    def create_images(self):
        """
        Creates and displays the logo image on the UI.

        This method loads the logo image from the specified file path and displays it
        as a label within the main UI frame.
        """

        # Load the logo image from the file path.
        logo = CTKUtilities.load_image('./assets/Banner.png', (450, 250))
        
        # Create a label with the logo image and place it on the UI.
        logo_label = customtkinter.CTkLabel(self.main_frame, image=logo, text='')
        logo_label.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.3)

    def create_text_labels(self):
        """
        Creates and displays text labels on the UI.

        This method creates and positions text labels within the main UI frame
        to provide information to the user.
        """
        
        # Create and place a text label with a description.
        text_label = customtkinter.CTkLabel(self.main_frame, text='A simple tool that will improve your experience.', font=('sans serif', 16))
        text_label.place(relx=0.1, rely=0.42, relwidth=0.8, relheight=0.1)

        # Create and place a text label indicating the version.
        version_text_label = customtkinter.CTkLabel(self.main_frame, text='Version: 1.0.0', font=('sans serif', 16))
        version_text_label.place(relx=0.092, rely=0.85, relwidth=0.8, relheight=0.1)

    def create_buttons(self):
        """
        Creates and displays buttons on the UI.

        This method creates and positions buttons within the main UI frame
        to allow the user to interact with different functionalities of the tool.
        """

        # Create a button to view room members.
        self.view_members_button = customtkinter.CTkButton(self.main_frame, text='View room members', width=150, height=30, font=('sans serif', 16), border_color='#f508e3', fg_color='#010101', hover_color='#f508e3', corner_radius=12, border_width=3, command=self.soloq_button)
        self.view_members_button.place(relx=0.32, rely=0.55, relwidth=0.35, relheight=0.1)

        # Create a button for auto game acceptance.
        self.autoaccept_button = customtkinter.CTkButton(self.main_frame, text='Auto accept game', width=150, height=30, font=('sans serif', 16), border_color='#f508e3', fg_color='#010101', hover_color='#f508e3', text_color=self.get_text_color(), corner_radius=12, border_width=3, command=self.autoaccept_button)
        self.autoaccept_button.place(relx=0.32, rely=0.7, relwidth=0.35, relheight=0.1)

    def soloq_button(self):
        """
        Handles the action when the "View room members" button is clicked.

        This method retrieves the list of participants and opens a web browser
        with a link to a pregame analysis website.
        """

        list_of_participants = GetParticipants.get_participants()
        
        if list_of_participants is not None:
            if len(list_of_participants) >= 1:
                participants = ','.join(list_of_participants)
                webbrowser.open(f'https://porofessor.gg/es/pregame/las/{participants}')
            else:
                CTkMessagebox(
                    title='Champion Select', message='To use this function you must be in champion select',
                    icon="cancel", corner_radius=3
                )
        else:
            CTkMessagebox(
                title='Client not found', message='To use this feature you must have League of Legends open!',
                icon="cancel", corner_radius=3
            )

    def autoaccept_button(self):
        """
        Handles the action when the "Auto accept game" button is clicked.

        This method toggles the auto game acceptance setting in the configuration JSON file,
        updates the UI text color of the button based on the new setting, and saves the changes.
        """

        if JsonManager.get('./config.json', 'auto_accept') == 'true':
            state = 'false'
        else:
            state = 'true'

        new_settings = {
            'region': JsonManager.get('./config.json', 'region'),
            'auto_accept': state
        }

        JsonManager.save_json(new_settings, './config.json')
        self.autoaccept_button.configure(text_color=self.get_text_color())

    def on_auto_accept_window_closed(self):
        """
        Handles the action when the auto game acceptance settings window is closed.

        This method resets the reference to the auto game acceptance settings window.
        """

        self.auto_accept_window = None

    def get_text_color(self):
        """
        Determines the text color for the "Auto accept game" button based on the current setting.

        Returns:
            str: The color code for the text.
        """

        if JsonManager.get('./config.json', 'auto_accept') == 'true':
            # If auto accept is enabled, return green color.
            return '#58ff33'
        
        # If auto accept is disabled, return red color.
        return '#eb342e'

