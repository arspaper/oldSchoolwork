import ipaddress


count = 0
network = ipaddress.ip_network('192.168.32.160/255.255.255.240')
b_address = list()
for address in network:
    binary_string = f'{int(address):b}'
    b_address.append(binary_string)

for address in b_address:
    if address.count('1') % 2 == 0:
        count += 1

print(count)