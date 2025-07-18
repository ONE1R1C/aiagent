import os



def get_files_info(working_directory, directory="."):
    full_path = os.path.join(working_directory, directory)
    abs_full_path = os.path.abspath(full_path)
    abs_path = os.path.abspath(working_directory)

    if not abs_full_path.startswith(abs_path):
        return (f'Error: Cannot list "{directory}" as it is outside the permitted working directory')
    elif not os.path.isdir(abs_full_path):
        return (f'Error: "{directory}" is not a directory')

    try:
        dir_list = os.listdir(abs_full_path)
        info_list = []
        for names in dir_list:
            full_path_stats = os.path.join(abs_full_path, names)
            results = (f'- {names}: file_size={os.path.getsize(full_path_stats)} bytes, is_dir={os.path.isdir(full_path_stats)}')
            info_list.append(results)
        
        final_stats = '\n'.join(info_list)
        return final_stats
        
    except Exception as e:
        return f'Error: {str(e)}'
