import os



def get_file_content(working_directory, file_path):
    full_path = os.path.join(working_directory, file_path)
    abs_full_path = os.path.abspath(full_path)
    abs_path = os.path.abspath(working_directory)

    if not abs_full_path.startswith(abs_path):
        return (f'Error: Cannot read "{abs_full_path}" as it is outside the permitted working directory')
    elif not os.path.isfile(abs_full_path):
        return (f'Error: File not found or is not a regular file: "{abs_full_path}"')

    try:
        max_chars = 10000
        with open(abs_full_path, "r") as file:
            file_content_string = file.read(max_chars)
            if len(file_content_string) >= max_chars:
                return f'{file_content_string}\n[...File "{abs_full_path}" truncated at 10000 characters]'
        return file_content_string
        
    except Exception as e:
        return f'Error: {str(e)}'