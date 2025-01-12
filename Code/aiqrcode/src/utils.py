import os

def save_image(image_data: bytes, file_path: str) -> None:
    """Saves binary image data to a file."""
    with open(file_path, 'wb') as file:
        file.write(image_data)

def create_output_directory(directory: str) -> None:
    """Creates an output directory if it doesn't already exist."""
    if not os.path.exists(directory):
        os.makedirs(directory)

def create_export_directory(directory: str) -> None:
    """Creates an export directory if it doesn't already exist."""
    if not os.path.exists(directory):
        os.makedirs(directory)