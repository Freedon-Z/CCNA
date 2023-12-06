#NAT Configuration
configure terminal
interface GigabitEthernet0/1
ip nat outside
exit
interface GigabitEthernet0/0
ip nat inside
exit
ip nat inside source list 1 interface GigabitEthernet0/1 overload
access-list 1 permit 192.168.1.0 0.0.0.255
