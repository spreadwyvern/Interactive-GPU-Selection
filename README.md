# Interactive GPU Selection
A small script for assisting in running machine learning programs that require GPUs, especially on a shared GPU server.
Based on pynvml. 

Lists current GPU usage on the server and lets user select desired number of GPUs.
```
===== status of GPUs =====
b'GeForce GTX 1080 Ti': 11172.4 MB free, 0.0 MB used, 11172.4 MB total
b'GeForce GTX 1080 Ti': 11172.4 MB free, 0.0 MB used, 11172.4 MB total
b'GeForce GTX 1080 Ti': 11172.4 MB free, 0.0 MB used, 11172.4 MB total
b'GeForce GTX 1080 Ti': 11172.4 MB free, 0.0 MB used, 11172.4 MB total
b'GeForce GTX 1080 Ti': 11172.4 MB free, 0.0 MB used, 11172.4 MB total
b'GeForce GTX 1080 Ti': 11172.4 MB free, 0.0 MB used, 11172.4 MB total
b'GeForce GTX 1080 Ti': 11172.4 MB free, 0.0 MB used, 11172.4 MB total
b'GeForce GTX 1080 Ti': 11172.4 MB free, 0.0 MB used, 11172.4 MB total
===== available GPUs ===== 
 GPU [0, 1, 2, 3, 4, 5, 6, 7]
```
```
Desired number of GPUs: 
2
===== acquire GPUs =====
Training on GPU [0, 1]
```