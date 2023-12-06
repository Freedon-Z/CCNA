#Ethernet Interface Configuration:


# Enter global configuration mode
configure terminal

# Access a specific interface (e.g., GigabitEthernet0/1)
interface GigabitEthernet0/1

# Set the IP address and subnet mask
ip address 192.168.1.1 255.255.255.0

# Enable the interface
no shutdown

# Set the description for the interface
description LAN Connection

# Set the bandwidth (optional)
bandwidth 10000

# Exit interface configuration mode
exit

# Serial Interface Configuration:
# Enter global configuration mode
configure terminal

# Access a specific serial interface (e.g., Serial0/0)
interface Serial0/0

# Set the IP address and subnet mask
ip address 10.0.0.1 255.255.255.252

# Specify the clock rate for DCE (Data Communications Equipment) serial interfaces
clock rate 64000

# Enable the interface
no shutdown

# Set the description for the interface
description WAN Connection

# Exit interface configuration mode
exit



#VLAN Interface

# Enter global configuration mode
configure terminal

# Access a VLAN interface (e.g., VLAN 10)
interface Vlan10

# Set the IP address and subnet mask
ip address 192.168.10.1 255.255.255.0

# Enable the interface
no shutdown

# Set the description for the interface
description VLAN 10

# Exit interface configuration mode
exit

#Loopback Interface

# Enter global configuration mode
configure terminal

# Access a loopback interface (e.g., Loopback0)
interface Loopback0

# Set the IP address and subnet mask
ip address 172.16.1.1 255.255.255.255

# Enable the interface
no shutdown

# Set the description for the interface
description Loopback Interface

# Exit interface configuration mode
exit


