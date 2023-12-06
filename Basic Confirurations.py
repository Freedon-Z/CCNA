# Basic Configurations

#Access Router  Suggest improvements to optimize this

Router>enable
Password: [Enter your enable password]
Router#configure terminal

# Configuring Hostname

Router(config)#hostname YourRouterName
YourRouterName(config)#


#Configuring Interfaces

YourRouterName(config)#interface gigabitethernet0/0
YourRouterName(config-if)#ip address 192.168.1.1 255.255.255.0
YourRouterName(config-if)#no shutdown
YourRouterName(config-if)#exit

#Setting the Enable Secret Password

YourRouterName(config)#enable secret YourEnablePassword

#Configuring Interfaces

YourRouterName(config)#interface gigabitethernet0/0
YourRouterName(config-if)#description LAN Interface

#Setting a Banner
YourRouterName(config)#banner motd # Unauthorized access is prohibited! #

#Configuring Static Routes
YourRouterName(config)#ip route 0.0.0.0 0.0.0.0 192.168.1.254


#Configuring Dynamic Routing (OSPF)
YourRouterName(config)#router ospf 1
YourRouterName(config-router)#network 192.168.1.0 0.0.0.255 area 0

#Configuring NAT

YourRouterName(config)#ip nat inside
YourRouterName(config)#interface gigabitethernet0/0
YourRouterName(config-if)#ip nat outside


#Saving Configurations
YourRouterName#write memory



# Basic Router Configurations

# Enter global configuration mode
configure terminal

# Disable DNS domain lookup
no ip domain-lookup

# Set the hostname to R1
hostname R1

# Configure console line settings
line console 0
 logging synchronous
 exit

# Set a message of the day (MOTD) banner
banner motd $ Authorized Access Only! $

# Exit global configuration mode
end

# Save the configuration
write memory


#Set Router Hostname:

configure terminal
hostname MyRouter


#Configure Banner Message:

configure terminal
banner motd $
**********************************************
*  Authorized Access Only! Unauthorized access *
*   is prohibited. Disconnect IMMEDIATELY if   *
*           you are not an authorized user.    *
**********************************************
$


#Configure DNS Settings:

configure terminal
ip domain-name mydomain.com
ip name-server 8.8.8.8

# Set Clock and Timezone:
configure terminal
clock set 14:30:00 May 15 2023
clock timezone EST -5


#Configure NTP

configure terminal
ntp server pool.ntp.org


#Secure Console Access:

configure terminal
line console 0
password console-password
login
exit


# Secure Telnet and SSH Access:

configure terminal
line vty 0 4
password telnet-password
login
transport input telnet
exit

crypto key generate rsa
ip ssh version 2
line vty 0 4
password ssh-password
login
transport input ssh
exit



Switch Configurations
# Enter global configuration mode
configure terminal

# Disable DNS domain lookup
no ip domain-lookup

# Set the hostname to S1
hostname S1

# Configure console line settings
line console 0
 logging synchronous
 exit

# Set a message of the day (MOTD) banner
banner motd $ Authorized Access Only! $

# Save the configuration
write memory
