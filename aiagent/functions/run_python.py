import os
import subprocess


def run_python_file(working_directory, file_path, args=[]):
    full_path = os.path.join(working_directory, file_path)
    abs_full_path = os.path.abspath(full_path)
    abs_path = os.path.abspath(working_directory)

    if not abs_full_path.startswith(abs_path):
        return (f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory.')
    elif not os.path.exists(abs_full_path):
        return f'Error: File "{file_path}" not found.'
    elif not abs_full_path.endswith('.py'):
        return f'Error: "{file_path}" is not a Python file.'

    try:
        
        result = subprocess.run(["python", file_path] + args, capture_output=True, cwd=abs_path, timeout=30, text=True)

        
        if result.returncode != 0:
            return f'STDOUT:\n{result.stdout}\nSTDERR:\n{result.stderr}\nProcess exited with code {result.returncode}'
        elif not result.stdout and not result.stderr:
            return f'No output produced.'
        
        return f'STDOUT:\n{result.stdout}\nSTDERR:\n{result.stderr}\n'

    except Exception as e:
        return f'Error: executing Python file: {e}'