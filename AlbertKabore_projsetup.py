""" Start a data analytics project. """

import pathlib


def create_project_directory(directory_nam: str): # add type hinting to params
    """
    Create a project sub-directory.
    : param directory_name: Name to be creatd, e,g, "test"

    """
    pathlib.Path(directory_name).mkdir(exist_ok=True)

def main():
    """ Scaffold a project. """
    create_project_directory(dictory_name='test') # name the parameter
    create_projet_directory(directory_name='docs') # name the parameter


    if __name__ == '__main__':
        main()