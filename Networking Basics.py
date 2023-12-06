#Networking Basics:



Router Configuration:

#Configure basic router settings.

configure terminal
hostname RouterA


#Enable routing.

ip routing

#Save the configuration.

end
write memory

##Repeat the steps on RouterB.

#Switch Configuration:

#Configure basic switch settings.

configure terminal
hostname Switch1


#Save the configuration.

end
write memory
#Repeat the steps on Switch2.

#Host Configuration:

#Assign IP addresses to hosts.

configure terminal
interface GigabitEthernet0/0
ip address 192.168.1.2 255.255.255.0

#Set the default gateway.

ip default-gateway 192.168.1.1


#Save the configuration.

end
write memory

#Repeat the steps for Host2.


#Step 2: IP Addressing (IPv4 and IPv6)
#IPv4 Configuration:

#Configure IPv4 addressing on RouterA.

configure terminal
interface GigabitEthernet0/1
ip address 10.0.0.1 255.255.255.0


#Save the configuration.

end
write memory

#Repeat the steps on RouterB.

#IPv6 Configuration:

Configure IPv6 addressing on RouterA.

configure terminal
interface GigabitEthernet0/1
ipv6 address 2001:db8::1/64


#Save the configuration.

end
write memory

#Repeat the steps on RouterB.

#Step 3: Subnetting and VLSM
#Subnetting:

#Subnet the network into two subnets.

configure terminal
interface GigabitEthernet0/1.1
encapsulation dot1Q 10
ip address 10.0.0.1 255.255.255.

#Save the configuration.

end
write memory


#Repeat the steps for RouterB.

VLSM:


configure terminal
interface GigabitEthernet0/1.1.1
encapsulation dot1Q 11
ip address 10.0.0.2 255.255.255.252

#Save the configuration.

write memory

#Repeat the steps for RouterB.

#Step 4: MAC Addresses and ARP
#View MAC Addresses:


show mac address-table



#Clear ARP cache on RouterA.

clear arp


#Save the configuration.

end
write memory

#Repeat the steps on RouterB.

