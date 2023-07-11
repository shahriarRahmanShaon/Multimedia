def encode(msg):
    delimiter = '|'
    count = 0
    prev_char = ''
    encoded_msg = ""
    
    for char in msg:
        if char.isspace() and char != '\n':
            msg = ' '
        if prev_char == char:
            count += 1
        else:
            if prev_char:
                encoded_msg += str(count) + delimiter + prev_char + delimiter
                count = 1
                prev_char = char
    encoded_msg += str(count) + delimiter + prev_char + delimiter
    return encoded_msg  
    
def decode(encoded_msg):
    decoded_msg = ""
    pairs = encoded_msg.split('|')
    for i in range(0, len(pairs)-1, 2):
        count = int(pairs[i])
        symbol = pairs[i+1]
        decoded_msg += count * symbol
    return decoded_msg