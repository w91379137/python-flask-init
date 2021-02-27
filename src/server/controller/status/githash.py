
import os

def githash():
    stream = os.popen('git rev-parse --short HEAD')
    output = stream.read()
    return output
