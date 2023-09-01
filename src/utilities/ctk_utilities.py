import customtkinter

from PIL import Image


class CTKUtilities:
    @staticmethod
    def load_image(path, size=(500, 300)):    
        """
        Load and return an image from the given file path.

        Args:
            path (str): The file path to the image.
            size (tuple): The size to resize the image to (default is (500, 300)).

        Returns:
            customtkinter.CTkImage: The loaded image.
        """
        return customtkinter.CTkImage(light_image=Image.open(path), size=size)