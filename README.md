# MongoDB-client-simple-demo
A MongoDB client simple demonstration inspired by w3schools's examples

This script demonstrates the most use functions of [pymongo](https://pymongo.readthedocs.io/en/stable/), which are explained in [w3schools's website](https://www.w3schools.com/python/python_mongodb_getstarted.asp) includings:
database creation, collection creation, data insertion, finding, querying, sorting, deletion, dropping collection, etc.

# Getting started
1. You must have your own **mongodb** service running to serve this demo, or you can easily run it by follow [this repo](https://github.com/geeksloth/mongodb-simple-docker-compose) with few steps
2. Clone and get into this repo
```bash
git clone https://github.com/geeksloth/MongoDB-client-simple-demo.git && cd MongoDB-client-simple-demo
```
3. Install some requirements:
```bash
python3 -m pip install --upgrade pip && python3 -m pip install pymongo
```
4. [Recommend] Modify ```server```, ```username```, and ```password``` to your *MongoDB* server. Or you cal leave it default if you use [this guide](https://github.com/geeksloth/mongodb-simple-docker-compose).
5. Run the demo:
```bash
python3 demo.py
```
