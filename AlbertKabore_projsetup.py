''' Project 2 Setup, Albert Kabore
This module provides functions for creating a series of project folders. '''
# import dependencies
import pathlib
import math
import statistics
import time
import AlbertKabore_utils

#create folders for a given range
def create_folders_for_range(start, end):
    for i in range(start, end):
        pathlib.Path(f"{i}").mkdir(exist_ok=True)

#create folders from a list of folder names
def create_folders_from_list(folder_list):
    for folder in folder_list:
        pathlib.Path(folder).mkdir(exist_ok=True)

#create folders from a list of folder names with prefix 'data'
def create_prefixed_folders(folder_list, prefix):
    for folder in folder_list:
        pathlib.Path(f"{prefix}-{folder}").mkdir(exist_ok=True)

#create a folder every 5 seconds for the duration given
def create_folders_periodically(duration):
    start_time = time.time()
    while(time.time()-start_time < duration): #continue running while the time elapsed from start is less than the given duration
        current_time = time.time()-start_time
        pathlib.Path(f"Folder created at {round(current_time)} seconds").mkdir(exist_ok=True)
        time.sleep(period) #wait specified amount of seconds before beginning next iteration

# Create a path object
project_path = pathlib.Path.cwd()

# Define the new sub folder path
data_path = project_path.joinpath('data')

# Create new if it doesn't exist, otherwise do nothing
data_path.mkdir(exist_ok=True)

def create_project_directory(dir_name: str):
    #creates a project sub-directory
    pathlib.Path(dir_name).mkdir(exist_ok=True)

def main():
    ''' Main function to demonstrate module capabilities. '''

    # Print byline from imported module
    print(f"Byline: {AlbertKabore_utils}")
    # Call function 1 to create folders for a range (e.g. years)
    create_folders_for_range(start_year=2020, end_year=2024)

    # Call function 2 to create folders given a list
    folder_names = ['data-csv', 'data-excel', 'data-json']
    create_folders_from_list(folder_names)

    # Call function 3 to create folders using comprehension
    folder_names = ['csv', 'excel', 'json']
    prefix = 'data-'
    create_prefixed_folders(folder_names, prefix)

    # Call function 4 to create folders periodically using while
    duration_secs = 5  # duration in seconds
    create_folders_periodically(duration=5)

    create_folders_from_list(regions, to_lowercase=True, remove_spaces=True)


if __name__ == "__main__":
    main()

