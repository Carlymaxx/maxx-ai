import os
import subprocess
import shutil
import sys
from pathlib import Path

class FileOperationsTool:
    def read_file(self, file_path):
        try:
            with open(file_path, 'r') as f:
                return f.read()[:2000]
        except Exception as e:
            return f"Error reading file: {str(e)}"

    def write_file(self, file_path, content):
        try:
            with open(file_path, 'w') as f:
                f.write(content)
            return f"File written: {file_path}"
        except Exception as e:
            return f"Error writing file: {str(e)}"

    def list_directory(self, directory="."):
        try:
            items = os.listdir(directory)
            return "\n".join(items) if items else "Empty directory"
        except Exception as e:
            return f"Error: {str(e)}"

    def open_folder(self, path):
        try:
            if os.name == 'nt':
                os.startfile(path)
            elif os.name == 'posix':
                subprocess.run(['open', path] if sys.platform == 'darwin' else ['xdg-open', path])
            return f"Opened folder: {path}"
        except Exception as e:
            return f"Error: {str(e)}"

    def create_folder(self, path):
        try:
            Path(path).mkdir(parents=True, exist_ok=True)
            return f"Folder created: {path}"
        except Exception as e:
            return f"Error: {str(e)}"

    def delete_file(self, path):
        try:
            if os.path.isfile(path):
                os.remove(path)
            elif os.path.isdir(path):
                shutil.rmtree(path)
            return f"Deleted: {path}"
        except Exception as e:
            return f"Error: {str(e)}"

file_ops_tool = FileOperationsTool()