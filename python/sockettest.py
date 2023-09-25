import socket



hosts = ['www.google.com', 'www.bing.com', 'www.uc.edu']

print('Working from host: ' + socket.getfqdn())

for h in hosts:

  print (h + ': ' = socket.gethostbyname(h))