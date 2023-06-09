import time, re
from ssh2.session import Session
import socket
import random, os, asyncio
# hostname = 'vpn.madewgn.eu.org'
port = 22
time_value = "2m\n"
limitq = "2\n"


wtime = 1


# def save(inp):
#     # Generate nama file acak
#     timestamp = int(time.time())
#     random_number = random.randint(1, 1000)
#     file_name = f"output_{timestamp}_{random_number}.txt"

#     # Simpan decoded_output ke dalam file
#     with open(file_name, 'w') as file:
#         file.write(inp)
#     baca = open(file_name, 'r')
#     h = str(baca.read())
#     baca.close()
# #     os.remove(file_name)
#     # start_line = h.find("————————————————————————————————————————\n\n                  TROJAN\n ————————————————————————————————————————\n\n TROJAN")
#     # end_line = h.find("————————————————————————————————————————\n\n         Terimakasih sudah menggunakan-\nScript Credit by Potato\n ————————————————————————————————————————")
#     # result = h[start_line:end_line]
#     return h

class Buat:
    def __init__(self,ip,pw):
        self.ip = ip
        self.pw = pw
        self.user = "root"

    async def SSH(self,u,pw):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((self.ip, port))
        session = Session()
        session.handshake(sock)

        session.userauth_password(self.user, self.pw)
        channel = session.open_session()
        channel.execute("add-trws")

        channel.write(f"{u}\n")
        channel.write(f"{pw}\n")
        channel.write(f'{wtime}\n')
        # channel.write(time_value)
        # channel.write(limitq)

        output = b''
        while True:
            size, data = channel.read()
            if not data:
                break
            output += data

        decoded_output = output.decode('utf8', errors='ignore')

        # Menghapus karakter escape dan karakter ^[[2K
        clean_output = re.sub(r'\x1b[^m]*m', '', decoded_output)
        clean_output = re.sub(r'\x1b\[2K', '', clean_output)
        clean_output = re.sub(r'\x1b\[2K|\r', '', clean_output)
        data_cleaned = clean_output.replace("Wget is already installed\ncurl is already installed\nChecking...\nChecking...\nScript Active !\nIP Address Accepted\nClient Name Accepted", "")

        channel.close()
        session.disconnect()
        return data_cleaned




    async def trojan_ws(self,u):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((self.ip, port))
        session = Session()
        session.handshake(sock)

        session.userauth_password(self.user, self.pw)
        channel = session.open_session()
        channel.execute("add-trws")

        channel.write(f"{u}\n")
        channel.write(f'{wtime}\n')
        # channel.write(time_value)
        # channel.write(limitq)

        output = b''
        while True:
            size, data = channel.read()
            if not data:
                break
            output += data

        decoded_output = output.decode('utf8', errors='ignore')

        # Menghapus karakter escape dan karakter ^[[2K
        clean_output = re.sub(r'\x1b[^m]*m', '', decoded_output)
        clean_output = re.sub(r'\x1b\[2K', '', clean_output)
        clean_output = re.sub(r'\x1b\[2K|\r', '', clean_output)
        data_cleaned = clean_output.replace("Wget is already installed\ncurl is already installed\nChecking...\nChecking...\nScript Active !\nIP Address Accepted\nClient Name Accepted", "")

        channel.close()
        session.disconnect()
        return data_cleaned



    async def trojan_grpc(self,u):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((self.ip, port))
        session = Session()
        session.handshake(sock)

        session.userauth_password(self.user, self.pw)
        channel = session.open_session()
        channel.execute("add-trgrpc")

        channel.write(f"{u}\n")
        channel.write(f'{wtime}\n')
        # channel.write(time_value)
        # channel.write(limitq)

        output = b''
        while True:
            size, data = channel.read()
            if not data:
                break
            output += data

        decoded_output = output.decode('utf8', errors='ignore')

        # Menghapus karakter escape dan karakter ^[[2K
        clean_output = re.sub(r'\x1b[^m]*m', '', decoded_output)
        clean_output = re.sub(r'\x1b\[2K', '', clean_output)
        clean_output = re.sub(r'\x1b\[2K|\r', '', clean_output)
        data_cleaned = clean_output.replace("Wget is already installed\ncurl is already installed\nChecking...\nChecking...\nScript Active !\nIP Address Accepted\nClient Name Accepted", "")

        channel.close()
        session.disconnect()
        return data_cleaned



    async def vmess_ws(self,u):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((self.ip, port))
        session = Session()
        session.handshake(sock)

        session.userauth_password(self.user, self.pw)
        channel = session.open_session()
        channel.execute("add-vmess")

        channel.write(f"{u}\n")
        channel.write(f'{wtime}\n')
        # channel.write(time_value)
        # channel.write(limitq)

        output = b''
        while True:
            size, data = channel.read()
            if not data:
                break
            output += data

        decoded_output = output.decode('utf8', errors='ignore')

        # Menghapus karakter escape dan karakter ^[[2K
        clean_output = re.sub(r'\x1b[^m]*m', '', decoded_output)
        clean_output = re.sub(r'\x1b\[2K', '', clean_output)
        clean_output = re.sub(r'\x1b\[2K|\r', '', clean_output)
        data_cleaned = clean_output.replace("Wget is already installed\ncurl is already installed\nChecking...\nChecking...\nScript Active !\nIP Address Accepted\nClient Name Accepted", "")

        channel.close()
        session.disconnect()
        return data_cleaned

    async def vless_ws(self,u):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((self.ip, port))
        session = Session()
        session.handshake(sock)

        session.userauth_password(self.user, self.pw)
        channel = session.open_session()
        channel.execute("add-vmess")

        channel.write(f"{u}\n")
        channel.write(f'{wtime}\n')
        # channel.write(time_value)
        # channel.write(limitq)

        output = b''
        while True:
            size, data = channel.read()
            if not data:
                break
            output += data

        decoded_output = output.decode('utf8', errors='ignore')

        # Menghapus karakter escape dan karakter ^[[2K
        clean_output = re.sub(r'\x1b[^m]*m', '', decoded_output)
        clean_output = re.sub(r'\x1b\[2K', '', clean_output)
        clean_output = re.sub(r'\x1b\[2K|\r', '', clean_output)
        data_cleaned = clean_output.replace("Wget is already installed\ncurl is already installed\nChecking...\nChecking...\nScript Active !\nIP Address Accepted\nClient Name Accepted", "")

        channel.close()
        session.disconnect()
        return data_cleaned




if __name__ == "__main__":
    do = Buat("vpn.madewgn.eu.org", "madewgn")
    print(asyncio.run(do.trojan_ws("wisvqjsg")))

