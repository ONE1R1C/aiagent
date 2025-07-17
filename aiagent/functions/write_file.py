import os

def write_file(working_directory, file_path, content):
    full_path = os.path.join(working_directory, file_path)
    abs_full_path = os.path.abspath(full_path)
    abs_path = os.path.abspath(working_directory)

    if not abs_full_path.startswith(abs_path):
        return (f'Error: Cannot write "{abs_full_path}" as it is outside the permitted working directory')
    
    try:
        if not os.path.exists(abs_path):
            os.makedirs(abs_path)

        with open(abs_full_path, "w") as file:
            file.write(content)
        return f'Successfully wrote to "{abs_full_path}" ({len(content)} characters written)'
    except Exception as e:
        return f'Error: {str(e)}'