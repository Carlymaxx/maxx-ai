import subprocess
import platform
import pyperclip

class ClipboardTool:
    def read(self):
        try:
            return pyperclip.paste()
        except Exception as e:
            if platform.system() == "Windows":
                result = subprocess.run(['powershell', '-Command', 'Get-Clipboard'], capture_output=True, text=True)
                return result.stdout
            return f"Error: {str(e)}"

    def write(self, text):
        try:
            pyperclip.copy(text)
            return "Text copied to clipboard"
        except Exception as e:
            if platform.system() == "Windows":
                subprocess.run(['powershell', '-Command', f'Set-Clipboard -Value "{text}"'], check=False)
                return "Text copied to clipboard"
            return f"Error: {str(e)}"

    def clear(self):
        try:
            pyperclip.copy("")
            return "Clipboard cleared"
        except Exception as e:
            return f"Error: {str(e)}"

clipboard_tool = ClipboardTool()