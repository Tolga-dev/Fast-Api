# Network Fundamentals
## Network Concept
* a computer network
  * interconnected group of devices(laptop, computer, printer, mobile, camera) to exchange data
* converged network
  * telehone, video, data coms with single network
  * traditional separate networks
    * each network with its own rules
  * Converging  network
    * capable of delivering data void and video
  * 
* Devices
  * Wireless
    * joint device - wifi router
      * connects camera phone to router
  * Wired
    * physically connected using cable or wire
* Reliable network
  * ensures reliable and consistent delivery of data between devices or systems
* Four Basic Network Architecture
  * Fault Tolerance
  * Scalability
  * Qos
  * Security
* Topology
  * network hub : broadcast data packs to al ldevices
  * switch: selectively forwards data
  * Geometric representation as topology
  * Right Topology
    * increase performance 
    * reduce risks
    * increase energy and data efficiency
    * reduce operational and maintenance costs
  * Physical Topology
    * interconnected with wires and cables
  * Logical Topology
    * How devices appear connected to the user
* in shared ethernet
  * uses hubs rather than switches 
* physical is start
* logical is node to node
* Hub
  * broadcasts data packets to all devices connected to it regardless of intended recipient
* Switch 
  * more advenced device that selectively forwards data packets only to the device that it is intended for 
    * more efficient data transmission compared to a hub
* Most Popular Topologies
  * Bus
    * single channel
    * all computers connect to that channel and receiving data from the sources on any computer will 
    * be simultaneous
  * Star Topology
    * a central point connected to computers like rays of a star
    * laptop, tablet, phone to modem
  * Point to point 
    * simple one
    * two devices together like chain 
    * telephony
  * tree
    * root node high top 
  * hybrid
    * several topology used
      * bus and star for interconnection f.e
  
### OSI/TCP
* Osi 
  * open systems interconnection
  * Tcp/IP transmission control protocol / internet protocol
  * models used to understand and standardize network communication
  * layered
    * helps in isolating issues 
    * understanding the roles of different networking components
* Osi Model
  * application layer - Data - Host layer
    * interaction layer where applications can access the network services
  * presentation layer - Data - Host layer
    * encoding process and data storage formats
  * session layer - Data - Host layer
    * connections and responsible for controlling ports and sessions
  * transport layer - Data - Host layer
    * transfer data and make sure that it is delivered safe and sounds
  * network layer - Packets - Media layer
    * physical path the data will take
  * data link layer - Frame - Media layer
    * isolate some frames and correct errors that could occur on the physical layer
  * Physical layer - Bit - Media layer
    * transmit data over a cable or radio signal
* Transmission Control Protocol / Internet Protocol
  * Tcp Ip
  * Application 
    * app
    * presne
    * session
  * Transport
    * transport
  * Internet
    * network
  * Link
    * data link

### Protocols, The Rules
* a network protocol
  * established set or rules that determine how data is transmitted between different devices 
    * in the same network
  * allows connected devices to communicate with each other
    * regardless of any differences in their internal processes
  * rule establishment
    * identified sender and receiver
    * common language and grammar
    * speed and timing of delivery 
    * confirmation or acknowledgment requirements
  * protocols
    * Communications basics
    * encoding
    * formatting and encapsulation
    * size
    * timing
    * delivery options
      * unicast
        * from one source to one destination
      * broadcast
        * from one source to all possible destinations 
      * multicast
        * from one source to multiple stating

### Data Encapsulation
* Communication between layers on the same device 
  * encapsulation
  * decapsulation

## Ethernet
### Mac address
  * unique identifier
  * ethernet hardware address
  * hardware address
  * physical address
  * mac 48 bit, 6 byte
  * 12 hex ieee requirements
* First three 
  * vendor specific identifier
  * OUI
  * last 2 bit
    * first 
      * 0 globall unique
      * 1 locally administered
    * second
      * 0 unicast
      * 1 multicast
* last three
  * unique value within manufacturer's allocation
  * NIC
* mac acress types
  * unicast
    * unique 
    * a frame is sent from single to single
  * broadcast
    * all nodes
  * multicasts
    * group of nodes
* unique bit
  * reset
    * globallny unique
  * set
    * locally administrated
* 00-60-2F-3A-07-BC
* 00:60:2F:3A:07:BC
* 0060.2F3A.07BC
* 00-60-2f-3a-07-bc

### Ethernet Frame
* data link later
  * osi
* link layer 
  * tcp
* chuck of data, frame
* exact layer mac uses
* 6 byte destination
  * mac destionative interface
* 6 source
  * intercae
* 2 type
  * ethernet frame
* 46 - 1500 byte
  * user data
* 4 byte facs, frame check sequence
* 1 layer
  * preable, synchronize receiver clock and identify start of new frame
* no match
  * device discard the frame
* match
  * frame passed up 

### Mac vs IP
* mac, move the frame within local 
* ip, facilitate the communication
* same network
  * mac
* remote
  * ip

### Arp
* allows to display and modify, ip to physical address translation tables
* address resolution protocol

## Network

### Internet Protocol
* ip, internet protocol, communication protocol for routing addressing ip packs
* deliver packets from source to host destination
* Connectionless
* media independence
* best effort delivery
* routing
* addressing
* fragmentation and reassembly
* versioning
### IP v4
* version 4 
* internet header length 4 bit
* total length 16
* identification 16
* flags 3
  * reserver, future use must be 0
  * dont fragment 1 df 
  * more fragments mf 
* time to live ttl 8
* protocol 8 bit
* source ip 32, destination ip 32
* ipv4 is 32 bit
* ipv4 subnet mask
  * 32 bit 
  * network and host 
* address types
  * static
    * manually assigned to a host 
  * dynamic
    * dynamic ip address dhcp 
    * automatically provides ip addresses and other network configs
  * puclic  private
    * public
      * assigned to a device
    * private
      * directly accessible from internet
      * internal communication
      * 10.0.0.0/8  , 172.16.0.0/12  , 192.168.0.0/16.
* unicast
  * single sender 
  * single receiver
  * data is dispatched from one to specific destination by ip
  * mostly point to point communications
* broadcast
  * unique type of address used to send data packets to all devices
  * all devices
* multi cast address
  * sender to dispatch packets to group of recipients concurrently

* 224.0.0.0 - 224.0.0.255 (224.0.0.0/24)	
  * Reserved for local network control messages and protocols. Used by routing protocols (e.g., OSPF (Open Shortest Path First), RIP (Routing Information Protocol) and other network protocols like ICMP (Internet Control Message Protocol) for multicast pings.
* 224.0.1.0 - 238.255.255.255	
  * Available for global multicast addresses. Used for multicast communication across different networks and not restricted to local network use.
* 239.0.0.0 - 239.255.255.255	
  * Reserved for administratively scoped multicast addresses. Intended for use within specific domains or administrative boundaries and not forwarded beyond those boundaries.

* Loopback address
  * 127.0.0.1 ipv4 or ::! in ipv6
  * lo 
  * virtual representation of the device itself
* challenges
  * ipv4
    * demand
  * exhaustion
  * weak protocol extensibility
  * security problems

### IPv6
* larger address space
  * 128 bit
  * hex
* simplified header
  * reduct complexity
  * relocating optional 
* end to end connectivity
  * unique ip address
  * eleminating nat
  * ipv6 fully implemented
  * firewalls
* auto configs
* faster forwarding 
* no broadcast
* sec
* anycast supoort
* extensibility
* packet
  * version 4 bit, set to 6
  * trasffic class 8 bit
  * flow label 20 bit, to label packs , router and switch
  * payload, extesnion headers 
  * next header, protocol fields in ipv4, 
  * hop limit, number of hops, router
    * packet, can traverse before being discacrded, serves similar purpose time ot live
  * source and destionaion
* ip v6 address
  * 128 bit
  * hex format
  * ipv4 dotted decimal
  * by colon and 4 digit
  * 2001:0db8:0000:0000:0000:7a6e:0680:9668 can be written as 2001:db8::7a6e:680:9668 
  * 64 bits network, 64 bits node
  * network 64
    * routing, infos, traffic acress networks, 
  * node
    * lower 64, 
* ipv6 address type, scope
  * global unicast address
    * routable
    * 2001
  * site prefix
    * IANA to RIRs, allocate address to internver service providers, isps organiozation
      * /48 /56 / 64
  * subnet
    * divide allocated address space into smaller subnets for efficient address allocation and management
  * interface id
    * last 64, global unicast address
    * identifies the individual network interface, host within network 
    * randomly assigned
    * network interface, a hardware comp that connects a comp host to a network
  * unique local addresses ula
    * ula in ipv6, internal, lan
    * ula not from outside
      * address allocation
        * ula's divided into two /8 
          * fd00::/8 for globally assigned addresses.
          * fc00::/8 for locally assigned addresses.
      * ipv6 loopback address
        * representation of the same interface within a copmuter 
        * ipv4 and ipv6
        * tcp ip protocol stack directs packets back through the same interface
      * ipv4 
        * loopback adds are reserved, with 127.o.o.o/8 
        * ::1/128 
* using ipv6 in url
  * ipv4 users can access network resources like web pages using url
  * in ipv6, formar requires a tweak
  * ipv6, must be closed by square brackets 
  * https://[2001:db8:4531:674::100e]/webpage
* ipv6 prefix length
  * not usbnet mask 
  * prefix length yes
    * number of leading bits in ipv6
    * remaining bits represent interface identifier, host portions address 
    * cidr notation
    * / 
    * 2001:0db8:85a3::/48, the prefix length is 48
    * 48 BITS NETWORK PORTION, 128 - 48 = 80, INTERFACE IDENTIFIER
    * size of network, or subnet associated with ipv6
    * larger prefix, smaller size, allowing more subent, less address per subnt
    * /64 common
    * /48 site allocation, large scale
    * /128 no subnet
* challges
  * header manipulation
  * dual stacking
  * flooding
  * cost
  * dns challenges

### ICMP
* internet control message protocol, encapsulate within ip packs
  * network devices to comm with each other
* type 8 bit
  * 0 echo reply
  * 3 destionation unreach
  * 8 echo request
  * 11 time exceeded
* code 8 bit 
  * provides addtional infos about condition 
* icmp 16 bit
  * checksum
  * packet header data 
* additional data variable
* echo contain data payload, RTT round trip time between devices
* tools
  * ping packet internet groper
    * testing 
    * measure rtt
    * usage
      * verify
      * test
      * troubleshoot
  * tracte traceroute linux, tracert windows
    * to trace path that packets take from source to destionation
    * identify path check delays
    * troubleshoot
    * traffic infficient checking

### Routing
* process of forwaring ip packets from one to anohter
* table
  * destionaltion 
    * subnet or network
  * next hop router or interface
    * packet should be forwarded to reach the destination network
  * metric or cost
    * a value representing the cost or desirability of route used for seelction the best path amont multiple options
* dynamic cs static routing
  * static config
    * administrators manually define routing entries  in table
  * dynamic
    * routing protocols, router exchange info and automatically update routing tables based on network conditions and change
    * routers exchange updates to inform each other 
    * adapt to network changes, reroute traffic along alternative paths
* protocols
  * info and maintain routing tables
  * distance vector 
    * RIP routing information pro
    * hop count as metric and exchange table with neighboring
  * link state protocols
    * ospf, open shortest path first 
    * is is, intermediate system to intermediate system
    * a detailed view of network topology and calculate shortest paths using algo like dijktra algo
  * path vector 
    * bgp, border gateway protocol
    * used for routing between autonomous systems on internet and consider plocies and attributes 
* routing decision process
  * ip packets
  * packet forwarding
    * outgoing interface ok, forward pack to appropriate interface
* default gateway
  * A ROUTER, SERVES AS THE entry, exit point for traffic between local network and external network 
* main responsibility of the default gateway
  * network conenctivity
  * routing decision
  * configs
  * internet access
* ruoting tools
  * view 
  * add delete modify
  * manipulte metrics

### Subnetting
* process of diving a large internet protocol ip, into smaller, subnetwork known subnets
* efficiently allocate ip , optimize network, sec
  * efficient ip
  * network performance
  * sec
* techniques
  * divide network into equal sized nets
  * create nets based on geo
  * implement add to simplify and addres 
* number of required subnet
* host
* routing efficeny
* scalability
* /24
  * default local 
* /32
  * localback
* /31 
  * point to point
* 2001:db8::/32 
  * Documentation prefix used for examples
* ::1 
  * Localhost 
* fc00::/7 
  * Unique Local Addresses (ULA) - also known as “Private” IPv6 addresses. 
* fe80::/10 
  * Link Local addresses, only valid inside a single broadcast domain. 
* ff00::0/8 
  * Multicast addresses

### Tools
* ping
  * measure RTT
  * time it takes fro a packet to go from source to destionation and back
  * latency, performance
  * TTL value
* traceroute, tracert
  * network diagnostic tools
  * used to track path packet take from source to destionation
  * identifying each hop along the way
  * each hop, a router, gateway
  * pack passes through, allowing users to diagnose network issues and delays
* route
  * command line tool used in op to view and manipulate ip
  * allows users to display, add, modify, or delete entries in ip 
  * how pack forwarded on network

## Transport
### Overview
* end to end
  * key
    * segnentation reassebmly
    * end to end communication
    * reliable data delivery
    * connection managemetn
  * tcp
    * web, email, file transfer
  * udp
    * connectionless
    * voice, video streaming
  * port
  * socket
    * two processes communicate with each other over network
      * ip
      * port 
    * stream socket, tcp
    * datagram sockets, udp
### Tcp
* RELIABLE DATA, FLOW CONTROL, congestion control, full duplex communication, ordered data, connection oriented protocol, byte oriented protocol
* header
  * source port 16
  * destination 16
  * sequence 32
  * acknowledgment 32
  * data 4
  * reserver 6
  * flags 6
    * ack
    * rest
    * syn
    * fin
  * windows size 16
  * checksum 16
  * urgent 16
  * options
* three way handshake
  * syn
  * syn ack
  * ack
  * established
* flow control in tcp
  * manage rate of data transmission between sender receiver to ensure that sender does not overwhelm the reciever

### Udp
* connectionless, unreliable transport layer protocol 
* does not establish a connection before sending data
* lightweight
* source, destionation 16 16
* length checksum 16 16
* data
* client process overview

### Nat
* network address translation nat
* modify network address information in ip packet
* multiple devices within private network to share single public ip address for communication with devices outside
* static nat
  * simplest form of nat
  * one to one mapping tech
    * private ip address is permanently mapped to corresponding public ip
    * with static nat, incoming packets destined for public ip address 
    * a mail server on the inside of private network, static pubilc ip address for consistent 
* dnyamic pooled
  * multiple private ip, mapped to pool of public ip 
* masquerade nat pat
  * masquerade nat, nat overload pat, port address translation
  
### Tools
* netstat
  * display network connection
  * routing tables 
  * network interface statics
* display active tcp
* listening port
* processes
* process id: unique numeric identifier, assigned by operating system to each running process
  * used to manage and tack information
*  running netstat -tulnp shows TCP and UDP connections along with the associated PIDs
* netcat
  * nc, reading from and wiring to network connection using tcp or udp
* nmap
  * network mapper
  * open source tool 
  * used for network discovery
* tcpdump
  * analyzer that allows users to capture, display network packets transmitted and receiver over a network interface
    * network traffic sniffer

## Application
### DHCP
* dynamic host configuration protocol dhcp
  * automatically assign ip addresses and other network configs to devices on a network
* main
  * dynamic ip assignment
    * from pool
    * device connect to network and request an ip address, it send dhcp request to network
    * server, recieve and repons
  * ip address leases
    * dhcp client accepts an ip address offer, it leases the address for a specific period knows as lease time
    * time configurable, how long cluent can use assigned ip
  * reservatoin
    * particular devices based on their mac
* dora
  * discover
  * offer
  * request
  * acknowledge

### DNS
* domain name system, dns, distributed naming system used to translate domain names into ip addresses
* local check
* host
  * map
  * between ip and domain name
* host file commonly used for
  * local testing
  * pre resolution of domain names
  * specifying server names without configured dns
* tools
  * ns look up
  * querying dns to optain domain name or ip 
  * Mirrors refer to duplicate servers or websites that provide the same content as the original source

### Http
* hypertext transfer protocol
* client and server on www
* request response protocol
* client server communication
* stateless
* http versions
* http request
  * request method, url, hearder, message body
  * request
    * get
    * post
    * put
    * delete
    * patch
    * head
  * header
    * user agent
    * content type
    * authorization
    * cookie
* http response 
  * status line 
  * header
  * message body

### Https 
* hypertext transfer protocol secure
* same but secure
* security threats, including eavesdropping, data tampering, and man-in-the-middle attacks

### Protocol inspection
* to analyze and monitor network traffic at a granuler level
* tcpdump wireshark
* wireshark
  * network protocol sniffer
  * captures, display data packs acress a network