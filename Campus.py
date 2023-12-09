
three departments  each one has its own separte ip address
configure devises to end to end for  access internal and external server  
devices get dynamic ip address from router based dhcp server
swtiches configured to provide vlan and security settings

RIPv2 provide routing for router in internal network and static routing for external servers 

plan, design and prototype campus  => what cables and devices and hardens you gonna use
     hierarchical model: 
     core layer : Router 
     distribution layer :  multi layer  switch 3650
     access layer :access layer switch


topology
main campus
 building A : Admin staff , share network equipments , vlans
 building B : tech staff and pcs 
 Building C : 
          2 swtiches
          student swtich, IT switch
 lab and , host servers 
              Students’ labs and 
              IT department => web server for mail hosted externally on  cloud servr 
              
 smaller camous : septarate place
..
Router name campus
   hierarchical need layer 3 switch : distribution hierarchical
    4 departments = 4 swtiches

    Building b
     2 swtiches


    Building c 
    2 swtiches
    student lab , it lab
   every Building has pcs and printing
 Router(cloud) for email server , conneceted to main Router main campus
    web server, ftp server  ?? why


connect devises >"which devices and why" serial connection serial dce 


Q: router cloud email server connectet to ?


Branch campus:
 2 departments

   Router 2911,
   multilayer switch ()
   access layer switch 2960

 configure :
     core devises: router core layer

    and end devices . to access enternal servers and external server


 Note: each department should have own septarate ip network   

 Note: network between Routers
 Note: config Router via cli
        EN
        CONF T 
        int gig0/0 # serial cable
        no sh 
        int se0/1/0
        no sh

        int se0/1/1
        no sh
        do wr


Note: config switch - cli : en , conf t , interface vlan 10
                           switch(config)# range fa0/1-24
                           switch(config-if-range)#switchport access vlan 10
                                                  do wr
int range fa0/1-24
switchport mode access
switchport access vlan 10
do wr
en , conf t, int gig0/1/2 , switchport mode access, switchport access vlan 10, do wr, ex
en , con t, int gig1/0/1, switchport mode trunk
                                   switchport trunk encapsulation dotq //# if not available(by default ) then don't need it

Note: config interfaces ->assaign ip address
                          main router - en,conf t , int se0/1/1
                          distribution , en, conf t. int gig0/1/1
                          access layer, en, conf t, int gig0/1/0 , ex, do wr 

       config distribution layer & access layer                               


 Note; the Branch and cloud interfaces get ip address
                 main campus:: create  sub interfaces for each department>> 8 vlan
                               (interface >< sub-interface)
                  inter-vlan routing: so devices in different vlan  can comunicate togather
                                     config ip address for interfaces

                  en,conf t, int se0/1/1, ip address 10.10.10.1 255.255.255.252
                                         do wr
                   assaign static ip address to server
                                  ping 20.0.0.1                      
            con dhcp server:Switch(config)#ip dhcp pool staf-pool
                            Switch(dhcp-config)#network 192.168.9.0 255.255.255.0
                            Switch(dhcp-config)#default-router 192.168.9.1
                            Switch(dhcp-config)#dns-server 192.168.9.1




