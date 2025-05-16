import threading
import requests
import socket

### ------------------ ###
### Simple C2 Template ###
### ------------------ ###

server = "http://yourserver.com/" # You HAVE to replace this with your server or it wont work.

headers = { # put your headers here if it needs headers.
    "Content-Type": "application/json"
}

def check(): # this checks if the server is valid.
    res = requests.post(server, headers=headers)
    if res.status_code in [200,201,202,203,204]: # replace with your codes, for success, and error.
        print("Server is working.")
    elif res.status_code in [400,401,402,403,404]: # same here.
        print("Server is not working.")
    else:
        print(f"Error: {res.status_code}")
    
def connect():
    check()

    req = requests.post(f"{server}connect") # put your route to connect to the client.

    ### now make it support your client. ###
    

connect()
