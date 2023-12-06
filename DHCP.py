# Enter global configuration mode
configure terminal

# Enable DHCP service on the router
service dhcp

# Create a DHCP pool named "LAN-Pool"
ip dhcp pool LAN-Pool

# Specify the network and subnet mask for the DHCP pool
network 192.168.1.0 255.255.255.0

# Set the default gateway for DHCP clients
default-router 192.168.1.1

# Set the DNS server for DHCP clients
dns-server 8.8.8.8

# Specify the lease duration (optional, default is 1 day)
lease 7

# Exclude IP addresses from the DHCP pool (optional)
ip dhcp excluded-address 192.168.1.1 192.168.1.10

# Enable the DHCP pool
exit

# Exit global configuration mode
end



#DHCP Pool

# Enter global configuration mode
configure terminal

# Enable DHCP service on the router
service dhcp

# Create a DHCP pool named "LAN-Pool"
ip dhcp pool LAN-Pool

# Specify the network and subnet mask for the DHCP pool
network 192.168.1.0 255.255.255.0

# Set the default gateway for DHCP clients
default-router 192.168.1.1

# Set the DNS server for DHCP clients
dns-server 8.8.8.8

# Specify the lease duration (optional, default is 1 day)
lease 7

# Exclude IP addresses from the DHCP pool (optional)
ip dhcp excluded-address 192.168.1.1 192.168.1.10

# Enable the DHCP pool
exit

# Exit global configuration mode
end

# dhcp verify

show ip dhcp pool && show ip dhcp binding && show ip dhcp statistics && show ip interface brief


# dhcp pool for vlans

# Enter global configuration mode
configure terminal

# Enable DHCP service
service dhcp

# Create a DHCP pool for VLAN 10
ip dhcp pool VLAN10-Pool
 network 192.168.10.0 255.255.255.0
 default-router 192.168.10.1
 dns-server 8.8.8.8
 lease 7

# Create a DHCP pool for VLAN 20
ip dhcp pool VLAN20-Pool
 network 192.168.20.0 255.255.255.0
 default-router 192.168.20.1
 dns-server 8.8.8.8
 lease 7

# Create a DHCP pool for VLAN 30
ip dhcp pool VLAN30-Pool
 network 192.168.30.0 255.255.255.0
 default-router 192.168.30.1
 dns-server 8.8.8.8
 lease 7

# Repeat the above for additional VLANs

# Exit global configuration mode
end
