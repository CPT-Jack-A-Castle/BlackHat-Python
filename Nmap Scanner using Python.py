import argparse
import nmap

def argument_parser():
    parser = argparse.ArgumentParser(description = "Tcp Port Scanner")
    parser.add_argument("-o", "--host", nargs="?" , help = "Host IP address")
    parser.add_argument("-p","--ports", nargs = "?", help = "Comma seperated port list")
    var_args = vars(parser.parse_args())
    return var_args

def nmap_scan(host_id,port_num):
    print("trey 3")
    nm_scan =  nmap.PortScanner()
    nm_scan =  scan(host_id,port_num)
    state = nm_scan[host_id]['tcp'][int(port_num)]['state']
    result = ("[*] {host} tcp/{port} {state}".format(host= host_id,port=port_num,state=state))
    return result

if __name__ == '__main__':
    try:
        print("trey ")
        user_args = argument_parser()
        host = user_args["host"]
        print("trey 1")
        port_list = user_args["ports"].split(",")
        print("trey 2")
        for port in port_list:
            print(port)
            print(host)
            print(nmap_scan(host,port))
    except AttributeError:
        print("Error Please provide the Arguments as Required")
