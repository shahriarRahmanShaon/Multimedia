from collections import Counter
from heapq import heappop, heappush

class Node:
    def __init__(self, symbol=None, freq=0, left=None, right=None):
        self.symbol = symbol
        self.freq = freq
        self.left = left 
        self.right = right 
        
    def __lt__(self, other):
        return self.freq < other.freq 
    
def gen_frq_table(symbol):
    freq_table = []
    symbol_count = Counter(symbol)
    total_count = len(symbol)
    for symbol, count in symbol_count.items():
        probability = count/total_count
        node = Node(symbol, probability)
        freq_table.append(node)
        
    for node in freq_table:
        print(node.symbol, node.freq)
        
    return freq_table
def gen_tree(freq_table):
    heap = freq_table[:]
    while len(heap)>1:
        left = heappop(heap)
        right = heappop(heap)
        parent = Node(freq=left.frq+right.freq, left=left, right=right)
        heappush(heap, parent)
    return heap[0]

def gen_codewards(root):
    dict = {}
    stack = [(root, "")]
    while stack:
        node, code = stack.pop()
        if node.symbol:
            dict[node.symbol] = code
        if node.left:
            stack.append((node.left, code + "0"))
        if node.right:
            stack.append((node.right, code + "1"))
    return dict

def encode(symbols, codewards):
    encoded_msg = ""
    for symbol in symbols:
        encoded_msg += codewards[symbol]
    return encoded_msg

def decode(encode_msg, root):
    node = root 
    decoded_msg = ""
    for bit in encode_msg:
        if bit == "0":
            node = node.left 
        if bit == "1": 
            node = node.right 
        if node.symbol:
            decoded_msg += node.symbol 
            node = root 
    return decoded_msg