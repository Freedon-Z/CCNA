#Show current SSH configuration
show ip ssh

#Enter global configuration mode
conf t

#Configure domain name for SSH
ipdomain-name cisco.com

#Generate RSA crypto key for SSH
crypto key generate rsa

#Configure a username and secret for SSH login
username admin secret ccna

#Configure VTY lines for SSH
line vty 0 15
 transport input ssh
 login local
 exit

#Configure SSH version 2
ip ssh version 2

#Exit configuration mode
end
