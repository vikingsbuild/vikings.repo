import base64

def rc_tunel(): 
    tunel = "UmVmZXJlcj1odHRwOi8vd3d3LnJlZGVjYW5haXMuY29tLmJyLw=="
    ftunel = base64.b64decode(tunel)
    return ftunel
