# -Peer-to-peer-file-sharing-system
Distributed database implemeted on peer to peer system
The p2p system is a Napster-like conceptual implementation. The peers request the distrubuted databases to find the peers with the file.

Single request from a server(for example server A) is handled by a random bootstrap server which responds by giving the server with the right database fragment.

![single_requst](https://github.com/tedywond/azi_bot_project/blob/master/images/singleRequest.png)