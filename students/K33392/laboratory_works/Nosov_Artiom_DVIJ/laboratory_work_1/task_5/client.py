import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((socket.gethostname(), 8000))

msg = 'POST /grades?discipline=theory_of_neural_network&name=Artiom&grade=5 HTTP/1.1\r\nHost: local\r\nAccept: text/html\r\nUser-Agent: Mozilla/5.0\r\n\r\n'
s.send(msg.encode('iso-8859-1'))
msg_recv = s.recv(1000)
print(msg_recv.decode())
s.close()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((socket.gethostname(), 8000))

msg = 'POST /grades?discipline=theory_of_neural_network&name=Anna&grade=4 HTTP/1.1\r\nHost: local\r\nAccept: text/html\r\nUser-Agent: Mozilla/5.0\r\n\r\n'
s.send(msg.encode('iso-8859-1'))
msg_recv = s.recv(1000)
print(msg_recv.decode())
s.close()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((socket.gethostname(), 8000))

msg = 'POST /grades?discipline=theory_of_neural_network&name=Anna&grade=5 HTTP/1.1\r\nHost: local\r\nAccept: text/html\r\nUser-Agent: Mozilla/5.0\r\n\r\n'
s.send(msg.encode('iso-8859-1'))
msg_recv = s.recv(1000)
print(msg_recv.decode())
s.close()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((socket.gethostname(), 8000))

msg = 'POST /grades?discipline=math&name=Anna&grade=5 HTTP/1.1\r\nHost: local\r\nAccept: text/html\r\nUser-Agent: Mozilla/5.0\r\n\r\n'
s.send(msg.encode('iso-8859-1'))
msg_recv = s.recv(1000)
print(msg_recv.decode())
s.close()

disciplines = ['theory_of_neural_network', 'math']
full_text = ''
for i in disciplines:

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    s.connect((socket.gethostname(), 8000))

    msg = f'GET /grades?discipline={i} HTTP/1.1\r\nHost: local\r\nAccept: text/html\r\nUser-Agent: Mozilla/5.0\r\n\r\n'
    s.send(msg.encode('iso-8859-1'))
    msg_recv = s.recv(1000)
    print(msg_recv.decode())

    import re

    # Ваша строка с данными
    input_string = msg_recv.decode()

    # Используем регулярное выражение для извлечения текста между тегами <html> и </html>
    pattern = r'<html>(.*?)</html>'
    match = re.search(pattern, input_string)

    result_string = ''
    # Проверяем, найдено ли совпадение
    if match:
        extracted_text = match.group(1)
        result_string = f'<html>{extracted_text}</html>'
    else:
        print("Теги <html> не найдены.")

    full_text += result_string
    s.close()

file = open("index.html", "w")
file.write(full_text)

file.close()
