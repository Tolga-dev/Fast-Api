from SyncGame.Server import Client

# Basic Tcp Ping Pong Game
* Main idea
  * 2 Client 
    * Host
      * Sends Ball Position 
      * Sends Its Position
      * Receives Client Position
    * Client
      * Receives Host Position
      * Receives Ball Position
      * Sends Its Position
  * Server
    * Sends information to all clients, including host, that is a client technically
    * Gets information from all clients

* how to run?

Run Server
```python
python.exe Server.py
```
Open A terminal and Run Client.py
```python
python.exe Client.py
```
Open Another terminal and Run Client.py
```python
python.exe Client.py
```
