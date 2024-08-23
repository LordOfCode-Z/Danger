import os

def start_tor():
    os.system("sudo service tor start")
    os.system("sudo iptables -F")
    os.system("sudo iptables -t nat -F")
    os.system("sudo iptables -t nat -A OUTPUT -m owner --uid-owner $(id -u) -j RETURN")
    os.system("sudo iptables -t nat -A OUTPUT -p udp --dport 53 -j REDIRECT --to-ports 9053")
    os.system("sudo iptables -t nat -A OUTPUT -d 127.0.0.0/8 -j RETURN")
    os.system("sudo iptables -t nat -A OUTPUT -o lo -j RETURN")
    os.system("sudo iptables -t nat -A OUTPUT -m owner --uid-owner $(id -u) -j RETURN")
    os.system("sudo iptables -t nat -A OUTPUT -p tcp --syn -j REDIRECT --to-ports 9040")
    os.system("sudo iptables -A OUTPUT -m state --state ESTABLISHED,RELATED -j ACCEPT")
    os.system("sudo iptables -A OUTPUT -m owner --uid-owner $(id -u) -j ACCEPT")
    os.system("sudo iptables -A OUTPUT -j REJECT")
    print("Tor started and IP tables updated.")

def stop_tor():
    os.system("sudo service tor stop")
    os.system("sudo iptables -F")
    os.system("sudo iptables -t nat -F")
    print("Tor stopped and IP tables cleared.")

def main():
    print("1. Start Anonsurf")
    print("2. Stop Anonsurf")
    choice = input("Choose an option: ")
    
    if choice == '1':
        start_tor()
    elif choice == '2':
        stop_tor()
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()