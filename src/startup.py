import threading

from src.forms.root.root_form import RootForm
from src.automation.script import Script


class Startup():
    @staticmethod
    def run():                      
        """
        Main function to start and run the Tool.
        """
        thread = threading.Thread(target=Script.run_loop)
        thread.start()
        RootForm(thread)