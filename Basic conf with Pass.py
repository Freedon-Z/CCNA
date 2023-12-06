# Basic Router Configuration
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
banner motd $ Authorized Access Only! And Godzilla will beat Kong any day $

# Save the initial configuration
write memory

# Enter privileged exec mode for further configuration
conf t

# Set the enable secret password
enable secret class

# Configure console line for password security
line console 0
 password cisco
 login
 exit

# Configure VTY lines for password security
line vty 0 4
 password cisco
 login
 exit

# Enable password encryption service
service password-encryption

# Exit configuration mode
end

# Save the final configuration
write memory
