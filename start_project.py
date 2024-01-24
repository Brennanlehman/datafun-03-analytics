"""Start a project"""

#imports
import pathlib

#functions
def create_project_directory(directory_names: str): #add type hinting to paramater
    pathlib.Path(directory_names).mkdir(exist_ok = True)



#main function
def main():
    create_project_directory('test') #name the parameter
    create_project_directory('docs') #name the parameter
    

from pathlib import Path 

# List of weekday folder names
day_list = ["01-Mon", "02-Tue", "03-Wed", "04-Thu", "05-Fri", "06-Sat", "07-Sun"]

# Iterate through the list and create folders
for day in day_list:
    folder_name = f"data-{day}"
    Path(folder_name).mkdir(exist_ok=True)
    print(f"Folder '{folder_name}' created.")

#module block
if __name__ == "__main__":
    main()