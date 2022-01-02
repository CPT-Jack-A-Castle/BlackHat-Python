import argparse
import socket
import threading


def connection_scan(target_ip, target_port):
    '''
    Tries to connect to the target_ip and target_port
    If successful print opem
    Else print close
    '''

    try:
        c_socket= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        c_socket.connect((target_ip,target_port))
        print("[+] {}/Opened TCP PORT".format(target_port))
    except OSError:
        print("[-] {}/Closed TCP PORT".format(target_port))
    finally:
        c_socket.close() #closing the socket

def port_scan(target,port_num):
    """
    Scanning the Target
    Firstly it attempts to resolve the Ip Address to the hostname and
    Then Enumerates through the ports through connection_scan fucntion
    """
    try:
        target_ip = socket.gethostbyname(target)
    except OSError:
        print("Unresolved Host IP{}".format(target_ip))
    try:
        target_ip = socket.gethostbyname(target)
        print(f"Scan Results of {target_ip}:")
    except OSError:
        print(f"Scan Results of {target_ip}:")
        return
    t = threading.Thread(target = connection_scan, args = (target,int(port_num)))
    t.start()

def argument_parser():
    parser = argparse.ArgumentParser(description = "Tcp Port Scanner")
    parser.add_argument("-o", "--host", nargs="?" , help = "Host IP address")
    parser.add_argument("-p","--ports", nargs = "?", help = "Comma seperated port list")
    var_args = vars(parser.parse_args())
    return var_args
if __name__ == '__main__':
    try:
        user_args = argument_parser()
        host = user_args["host"]
        port_list = user_args["ports"].split(",")
        for port in port_list:
            port_scan(host,port)
    except AttributeError:
        print("Error Please provide the Arguments as Required")
