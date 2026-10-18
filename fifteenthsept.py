#15/10/26 devops tools
from pathlib import Path
#addition of the subprocess lib done on 22/9/26
import subprocess

#print(Path(file_path).read_text(encoding = "utf-8")) previous code
LEVELS = ("INFO","DEBUG")
def read_file(path):
    return (Path(path).read_text(encoding = "utf-8"))

def count_log_levels(text):
    counter = {
        "INFO":0,
        "DEBUG":0
        }
    for line in text.splitlines():
        tokens = line.split()
        for level in LEVELS:
            if level in tokens:
                counter[level] += 1
    return counter
    #print(counter)
    
def show_docker_containers():
    return subprocess.run(["docker","ps","-a"],capture_output=True,text=True)
    
    
'''file_path = "/home/harshalp/Desktop/prodevopscom/app.log"
text = read_file(file_path)
count_log_levels(text)'''