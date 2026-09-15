def commands(binary_str):
    secret_hs = []
    if binary_str[-1] == "1":
        secret_hs.append("wink")
    if binary_str[-2] == "1":
        secret_hs.append("double blink") 
    if binary_str[-3] == "1":
        secret_hs.append("close your eyes")
    if binary_str[-4] == "1":
        secret_hs.append("jump")
    if binary_str[-5] == "1":
        secret_hs = secret_hs[::-1]
    return secret_hs
