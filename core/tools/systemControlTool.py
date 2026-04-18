import os
import subprocess
import platform

class SystemControlTool:
    def __init__(self):
        self.system = platform.system()

    def set_volume(self, level):
        try:
            level = max(0, min(100, int(level)))
            if self.system == "Windows":
                subprocess.run(['nircmd.exe', 'setsysvolume', str(int(level * 655.35))], check=False)
            elif self.system == "Darwin":
                subprocess.run(['osascript', '-e', f'set volume output volume {level}'])
            else:
                subprocess.run(['amixer', '-D', 'pulse', 'sset', 'Master', f'{level}%'])
            return f"Volume set to {level}%"
        except Exception as e:
            return f"Error: {str(e)}"

    def get_volume(self):
        try:
            if self.system == "Darwin":
                result = subprocess.run(['osascript', '-e', 'output volume of (get volume settings)'], capture_output=True, text=True)
                return f"Volume: {result.stdout.strip()}%"
            return "Volume control not supported"
        except Exception as e:
            return f"Error: {str(e)}"

    def set_brightness(self, level):
        try:
            level = max(0, min(100, int(level)))
            if self.system == "Windows":
                subprocess.run(['powershell', '-Command', f'(Get-WmiObject -Namespace root/WMI -Class WmiMonitorBrightnessMethods).WmiSetBrightness(1,{level})'], check=False)
            elif self.system == "Linux":
                subprocess.run(['xrandr', '--output', subprocess.run(['xrandr', '--current'], capture_output=True, text=True).stdout.split()[3], '--brightness', str(level/100)], check=False)
            return f"Brightness set to {level}%"
        except Exception as e:
            return f"Error: {str(e)}"

    def shutdown(self, delay=0):
        try:
            if self.system == "Windows":
                subprocess.run(['shutdown', '/s', '/t', str(delay)])
            else:
                subprocess.run(['shutdown', '-h', f'+{delay}'])
            return f"Shutdown scheduled in {delay} seconds"
        except Exception as e:
            return f"Error: {str(e)}"

    def reboot(self, delay=0):
        try:
            if self.system == "Windows":
                subprocess.run(['shutdown', '/r', '/t', str(delay)])
            else:
                subprocess.run(['reboot', f'+{delay}'])
            return f"Reboot scheduled in {delay} seconds"
        except Exception as e:
            return f"Error: {str(e)}"

    def sleep(self):
        try:
            if self.system == "Windows":
                subprocess.run(['rundll32.exe', 'powrprof.dll,SetSuspendState', '0', '1', '0'])
            else:
                subprocess.run(['pmsleep', 'now'])
            return "System going to sleep"
        except Exception as e:
            return f"Error: {str(e)}"

    def lock_screen(self):
        try:
            if self.system == "Windows":
                subprocess.run(['rundll32.exe', 'user32.dll,LockWorkStation'])
            elif self.system == "Darwin":
                subprocess.run(['/System/Library/CoreServices/Menu Extras/User.menu/Contents/Resources/CGSession', '-suspend'])
            else:
                return "Lock not supported on this system"
            return "Screen locked"
        except Exception as e:
            return f"Error: {str(e)}"

system_control_tool = SystemControlTool()