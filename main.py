import json
import os
import shutil

script_path = os.path.dirname(os.path.realpath(__file__))

def check_folder(folder_path):
    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)
        if os.path.isfile(file_path) and file_name.endswith('.json'):
            print(f"Found JSON file: {file_path}")
            # replace the "\" by "/" to avoid the error "json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)"
            file_path = file_path.replace("\\", "/")
            
            # Call the function to sort the file
            sort_file(file_path)
        elif os.path.isdir(file_path):
            # Recursively check the subfolder
            check_folder(file_path)


# Open the file and check if the first property is an array then for each element of this array, we check if the property "Outer" exists, 
# if it does, we ignore it, and pass to the next element, if it doesn't, we sort the file by the property "Type"
def sort_file(file_path):
    
    type = "Null"
    
    with open(file_path, 'r') as file:
        # Try to load the JSON file if it's not a valid JSON file, it will raise an exception, catch it and print the error, then return
        try:
            data = json.load(file)
        except json.decoder.JSONDecodeError as e:
            print(f"Error while reading the file: {file_path}")
            print(e)
            return
        if isinstance(data, list):
            
            # We check each element, until we found one without the property "Outer"
            for element in data:
                if "Outer" not in element:
                    print(f"The file {file_path} has been sorted")
                    print(f"Object Type: {element['Type']}")
                    
                    type = element['Type']
                    break
        else:
            print(f"The file {file_path} is not a valid JSON file")

    # Call the function to move the file to the correct folder
    move_file(file_path, f"{script_path}/SortedFiles/{type}")


def move_file(file_path, new_folder_path):
    # Move the file to the new folder
    # We check if the folder exists, if it doesn't, we create it
    
    if not os.path.exists(new_folder_path):
        os.makedirs(new_folder_path)
    
    shutil.copy(file_path, new_folder_path)
    
    pass

# Example usage
folder_path = 'C:/Users/YourName/Desktop/Mods Unreal/FModel/Output/Exports/TheBloodline/Content'
check_folder(folder_path)