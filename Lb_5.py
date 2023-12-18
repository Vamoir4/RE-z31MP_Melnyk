def encode(string):
    bits = ""
    for char in string:
        
        binary = format(ord(char), '08b')
    
        bits += ''.join([bit * 3 for bit in binary])
    return bits

def decode(bits):
    string = ""

    triples = [bits[i:i+3] for i in range(0, len(bits), 3)]

    corrected_bits = ''.join(['0' if triple.count('0') > 1 else '1' for triple in triples])
 
    ascii_values = [int(corrected_bits[i:i+8], 2) for i in range(0, len(corrected_bits), 8)]
 
    string = ''.join([chr(value) for value in ascii_values])
    return string
