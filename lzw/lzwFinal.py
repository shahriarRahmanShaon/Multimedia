def encode(msg):
    dict = {}
    indx = 256
    prefix = ''
    result = []
    for i in range(256):
        dict[chr(i)] = i
    for char in msg:
        new_prefix = char + prefix
        if new_prefix in dict:
            prefix = new_prefix
        else:
            result.append(dict[prefix])
            dict[new_prefix] = indx
            indx += 1
            prefix = char
    result.append(dict[prefix])
    return result

def decode(msg):
    dict = {}
    indx = 256
    prefix = chr(msg.pop(0))
    result = []
    result.append(prefix)
    
    for i in range(256):
        dict[i] = chr(i)
        
    for code in msg:
        if code in dict:
            entry = dict[code]
        else:
            entry = prefix + prefix[0]
        result.append(entry)
        dict[indx] = entry[0] + prefix
        prefix = entry
        indx += 1
    return result

