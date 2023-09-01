import time
import pyautogui


from src.managers.json_manager import JsonManager


class Script:
    running = True

    @classmethod
    def stop(cls):
        """
        Stops the script by setting the 'running' class variable to False.
        """
        cls.running = False

    @classmethod
    def run_loop(cls):
        """
        Main loop of the script that runs as long as 'running' is True.

        This loop checks if auto accept is enabled, and if so, it looks for the accept button on the screen
        and clicks it if found.
        """
        
        while cls.running:
            time.sleep(2)

            if JsonManager.get('./config.json', 'auto_accept') == 'true':
                accept_button = Script.search_image('./assets/game_buttons/accept.png', 0.6)

                if accept_button is not None:
                    pyautogui.click(pyautogui.center(accept_button))

    @staticmethod
    def search_image(image_path, confidence):
        """
        Searches for an image on the screen and returns its location if found.

        Args:
            image_path (str): The path to the image file to search for.
            confidence (float): The minimum confidence level for a match (0.0 to 1.0).

        Returns:
            tuple or None: The location of the found image as (left, top, width, height) or None if not found.
        """

        image = pyautogui.locateOnScreen(image=image_path, confidence=confidence)
        return image