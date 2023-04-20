import random

with open('proxy.txt', 'r') as file:
    contents = file.read()

ip = contents.split('\n')

def rand_port():
    port = int(random.randrange(10000,10099))
    return port