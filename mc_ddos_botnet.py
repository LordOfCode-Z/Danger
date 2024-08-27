import threading
from minecraft.networking.connection import Connection
from minecraft.networking.packets import clientbound, serverbound

# Gerekli bilgileri kullanıcıdan input ile al
server_address = input("Sunucu adresini girin: ")
server_port = int(input("Sunucu portunu girin (Varsayılan: 25565): ") or 25565)
bot_count = int(input("Kaç bot bağlanacak? "))
message_to_send = input("Botların göndereceği mesaj nedir? ")

def join_server_and_send_message(username):
    connection = Connection(server_address, server_port, username=username)
    connection.connect()

    def handle_join_game(packet):
        print(f"{username} sunucuya katıldı!")
        send_chat_message(message_to_send)

    def send_chat_message(message):
        chat_packet = serverbound.play.ChatPacket()
        chat_packet.message = message
        connection.write_packet(chat_packet)

    connection.register_packet_listener(handle_join_game, clientbound.play.JoinGamePacket)
    connection.send_packet(serverbound.handshake.HandshakePacket(protocol_version=340, server_address=server_address, server_port=server_port, next_state=2))
    connection.send_packet(serverbound.login.LoginStartPacket(username=username))

    while True:
        connection.read_packet()

threads = []
for i in range(bot_count):
    username = f'bot_{i}'
    thread = threading.Thread(target=join_server_and_send_message, args=(username,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()