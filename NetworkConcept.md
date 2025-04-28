# Network Concept
* a computer network
  * interconnected group of devices(laptop, computer, printer, mobile, camera) to exchange data
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
    * all computers connect to that channel and receiving data from the sources on any computer will be simultaneous
  * Star Topology
    * a central point connected to computers like rays of a star
    * laptop, tablet, phone to modem
  * Point to point 
    * simple one
    * two devices together like chain 
    * telephony
  * tree
    * root node high top 
  
# OSI/TCP
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
  * Transport
  * Internet
  * Link

# Protocols, The Rules
* a network protocol
  * established set or rules that determine how data is transmitted between different devices in the same network
  * allows connected devices to communicate with each other
    * regardless of any differences in their internal processes
  * rule establishment
    * identified sender and receiver
    * common language and grammar
    * speed and timing of delivery 
    * confirmation or acknowledgment requirements
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
    