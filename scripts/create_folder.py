import os
import datetime
import random
import string

def create_folder(folder_name):
    """
    Creates a folder with the given name in the current working directory.
    Prints the folder name once it is created.

    :param folder_name: Name of the folder to create
    """
    try:
        os.makedirs(folder_name, exist_ok=True)
        print(f"Folder '{folder_name}' created successfully.")
    except Exception as e:
        print(f"An error occurred while creating the folder: {e}")

if __name__ == "__main__":
    folder_name = "runs/" + \
        datetime.datetime.now().strftime('%Y%m%d_%H%M%S') + \
        '_' + \
        ''.join(random.choices(string.ascii_lowercase + \
                               string.digits, k=3))
    os.makedirs(folder_name, exist_ok=True)
    print(folder_name)