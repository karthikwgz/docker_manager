import os
import json


def docker_status():
    return(os.popen("docker ps -a").read())

def download_image(img):
    return(os.popen(f"docker pull {img}").read())

def docker_stop(cntnr):
    os.popen(f"docker stop {cntnr}")

def delete_container(cntnr):
    os.popen(f"docker rm {cntnr}")

def run_container(cntnr,img):
    os.system(f"docker run --name {cntnr} -it {img}")

def network_details():
    net_detail = os.popen("docker network inspect bridge").read()
    return json.loads(net_detail)[0]

def list_netwrok():
    return os.popen("docker network ls").read()

def disconnect_network(cntnr,ntwrk):
    print("Disconnecting............")
    os.popen(f"docker network disconnect {ntwrk} {cntnr}")
    
def connect_network(cntnr,ntwrk):
    print("Connecting...........")
    return os.popen(f"docker network connect {ntwrk} {cntnr}").read()

# print(disconnect_network("myubuntu","bridge"))
# print(connect_network("myubuntu","bridge"))
