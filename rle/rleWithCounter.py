from collections import Counter

with open("inp.txt", "r") as file:
    contents = file.read()

def encode(contents):
    counter_result = Counter(contents)
    return dict(counter_result)
    
def decode(encoded_msg):
    result_string = ''.join([key * value for key, value in encoded_msg.items()])
    return result_string


res = encode(contents)
with open("enc.txt", "w") as file:
    file.write(str(res))
    
with open("enc.txt", "r") as file:
    dict_string = file.read()

enc_dict = eval(dict_string)

decoded_res = decode(enc_dict)

with open("dec.txt", "w") as file:
    file.write(str(decoded_res))
    
print(res)
print(decoded_res)
