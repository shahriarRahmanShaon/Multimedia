import os
def lzw_compress(data):
    dictionary = {}
    result = []
    indx = 256
    
    for i in range(256):
        dictionary[chr(i)] = i
    prefix = ''
    for char in data:
        new_prefix =  prefix + char
        if new_prefix in dictionary:
            prefix = new_prefix
        else:
            result.append(dictionary[prefix])
            dictionary[new_prefix] = indx
            indx += 1
            prefix = char
    result.append(dictionary[prefix])
        
    return result

def lzw_decompress(data):
    dictionary = {}
    result = []
    indx = 256
    
    for i in range(256):
        dictionary[i] = chr(i)
    prefix = chr(data.pop(0))
    result.append(prefix)
    
    for code in data:
        if code in dictionary:
            entry = dictionary[code]
        else:
            entry = prefix + prefix[0]
            
        result.append(entry)
        dictionary[indx] = prefix + entry[0]
        indx += 1
        prefix = entry
        
    return result
        

def encodefile(input_file,output_file):
    with open(input_file, 'r') as f:
        data = f.read()
        compressed = lzw_compress(data)
    with open(output_file,'w') as f:
        f.write(' '.join(map(str,compressed)))
        
    
def decodefile(input_file,output_file):
    with open(input_file, 'r') as f:
        data = f.read()
        data = list(map(int,data.split()))
        decompressed = lzw_decompress(data)
    with open(output_file,'w') as f:
        f.write(''.join(map(str,decompressed)))
        
        
encodefile('inp.txt','enc.txt')
decodefile('enc.txt','dec.txt')
orgfile_size = os.path.getsize("inp.txt")
encfile_size = os.path.getsize("enc.txt")
print(f'Compression ratio: {orgfile_size/encfile_size:.2f}')