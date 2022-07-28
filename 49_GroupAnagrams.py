strs = ["eat","tea","tan","ate","nat","bat"] 
strs2 = [""]
strs3 = ["a"]

def fn(strs):
    hash = {}
    resultado =[]
    for str in strs:
        
        strr = sorted(str)
        strr = "".join(strr)

        if not hash.get(strr):
            hash[strr] = [str] 
        else:
            hash[strr].append(str)


    for key, value in hash.items():
        resultado.append(value)
    
    return resultado

fn(["",""])


