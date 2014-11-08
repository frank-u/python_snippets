# -*- coding: utf-8 -*-
"""
for Python v3
Created on 07.12.2012

@author: Oleksandr Poliatykin

Change VLAN on cisco 3750 port.

no cdp enable
end
VLAN Direction: 2 -> 1
ready to write
"""
import telnetlib
import sys
# import time
# import ipaddress
import wmi

net10 = ['10.0.0.77', '255.0.0.0', '10.0.0.1']
net172 = ['172.22.2.22', '255.255.255.224', '172.22.2.1']
netname = "Гигабитное сетевое подключение Intel(R) 82578DM"

device = "10.0.0.1"
password = "password_in_plain_text"
eol_char = b"\r"
mymac = "1C:6F:65:XX:XX:XX"

if sys.version < '3':
    print("ERROR: Need Python 3")
    sys.exit(666)

print("connecting")
# Соединяемся с коммутатором и переходим в режим полных прав
tn = telnetlib.Telnet(device, 23)  # подключаемся к узлу
tn.read_until(b"Password:")  # отлавливаем приглашение с вводом пароля
tn.write(password.encode(
    'ascii') + eol_char)  # вставляем пароль (Обратить внимание на \r)
tn.read_until(
    b"3750G-48>")  # отлавливаем приглашение, которое заканчивается "Router  >"
tn.write(b"enable" + eol_char)  # вводим команду (Обратить внимание на \r)
tn.read_until(b"Password:")  # отлавливаем приглашение с вводом пароля
tn.write(password.encode(
    'ascii') + eol_char)  # вставляем пароль (Обратить внимание на \r)
tn.read_until(
    b"3750G-48#")  # отлавливаем приглашение, информирующее о входе в систему

# Читаем и выводим текущую конфигурацию порта
tn.write(b"show running-config interface GigabitEthernet 1/0/48" + eol_char)
s = tn.read_until(b"end")  # считываем результат до определенного слова

vlan_found = False
for line in s.splitlines():
    print(line.decode('ascii'))
    if str(line.decode('ascii')).find("switchport access vlan") != -1:
        vlan_found = True
        current_vlan = int(str(line.decode('ascii')).split()[3])
if not vlan_found:
    current_vlan = 1

if current_vlan == 1:
    # Переходим во второй
    target_vlan = 2
    netsetto = net172
elif current_vlan == 2:
    # Переходим в первый
    target_vlan = 1
    netsetto = net10
else:
    print("Found wrong VLAN, Exiting")
    sys.exit(555)

print("VLAN Direction: " + str(current_vlan) + " -> " + str(target_vlan))

# Конфигурируем порт по другому 
tn.write(b"configure terminal" + eol_char)
tn.read_until(b"3750G-48(config)#")
tn.write(b"interface GigabitEthernet 1/0/48" + eol_char)
tn.read_until(b"3750G-48(config-if)#")
print("ready to write")
# ### PAYLOAD HERE ####
tn.write(
    b"switchport access vlan " + str(target_vlan).encode('ascii') + eol_char)
tn.read_until(b"3750G-48(config-if)#")
# ##############################################
# Obtain network adaptors configurations
nic_configs = wmi.WMI().Win32_NetworkAdapterConfiguration(IPEnabled=True)
for adapter in nic_configs:
    if adapter.Description == netname:
        # проверяем что делать:
        adapter.EnableStatic(IPAddress=[netsetto[0]], SubnetMask=[netsetto[1]])
        adapter.SetGateways(DefaultIPGateway=[netsetto[2]])
        print(adapter.Description)
        print(adapter.MACAddress)
        print(adapter.IPAddress)
        print(adapter)
print("Current IP:")

tn.write(b"end" + eol_char)
tn.read_until(b"3750G-48#")

tn.close()  # закрываем сессию
print("ended.")
