import os
def encode(text):
    encoded = ''
    prev_char = ''
    count = 0
    delimiter = '|'
    for char in text:
        if char.isspace() and char != '\n':
            char = ' '
        if char == prev_char:
            count += 1
        else:
            if prev_char:
                encoded += str(count) + delimiter + prev_char + delimiter
            prev_char = char
            count = 1
    encoded += str(count) + delimiter + prev_char + delimiter
    return encoded



def decode(text):
    decoded = ''
    pairs = text.split('|')
    for i in range(0, len(pairs)-1, 2):
        count = int(pairs[i])
        char = pairs[i+1]
        decoded += char * count
    return decoded


def compress(input_file, output_file):
    with open(input_file, 'r') as f:
        text = f.read()
    encoded_text = encode(text)
    with open(output_file, 'w') as f:
        f.write(encoded_text)


def decompress(input_file, output_file):
    with open(input_file, 'r') as f:
        encoded_text = f.read()
    decoded_text = decode(encoded_text)
    with open(output_file, 'w') as f:
        f.write(decoded_text)

compress('inp.txt', "enc.txt")
decompress('enc.txt','dec.txt')

orgfile_size = os.path.getsize("inp.txt")
encfile_size = os.path.getsize("enc.txt")
print(f'Compression ratio: {orgfile_size/encfile_size:.2f}')