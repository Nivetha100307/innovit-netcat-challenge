# math_challenge.py
import socket, threading, random

def handle(conn, addr):
    print(f"[+] {addr} connected")
    a, b = random.randint(10, 99), random.randint(10, 99)
    conn.send(f"Solve this: {a} + {b} = ?\n".encode())
    ans = conn.recv(1024).decode().strip()
    if ans == str(a + b):
        conn.send(b"Correct! Flag: flag{math_master}\n")
    else:
        conn.send(b"Wrong! Bye.\n")
    conn.close()

server = socket.socket()
server.bind(("0.0.0.0", 4444))
server.listen(100)
print("Listening on port 4444...")

while True:
    conn, addr = server.accept()
    threading.Thread(target=handle, args=(conn, addr)).start()
