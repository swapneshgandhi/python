__author__ = 'swaps_000'

#
# File content:
# host1.example.com#192.168.0.1#web server
# host2.example.com#192.168.0.5#dns server
# host3.example.com#192.168.0.7#web server
# host4.example.com#192.168.0.9#application server
# host5.example.com#192.168.0.10#database server
# There are multiple files in side the folder with the same format. At the end I would like to receive list of dictionaries with the following format:
#
# [ {'dns': 'host1.example.com', 'ip': '192.168.0.1', 'description': 'web_server'},
#   {'dns': 'host2.example.com', 'ip': '192.168.0.5', 'description': 'dns server'},
#   {'dns': 'host3.example.com', 'ip': '192.168.0.7', 'description': 'web server'},
#   {'dns': 'host4.example.com', 'ip': '192.168.0.9', 'description': 'application server'},
#   {'dns': 'host5.example.com', 'ip': '192.168.0.10', 'description': 'database server'} ]


out = []
labels = ['dns', 'ip', 'description']
data = open('file')
for line in data:
    out.append(dict(zip(labels, line.split('#'))))