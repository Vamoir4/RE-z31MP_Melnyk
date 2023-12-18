def scanner(qrcode):
    
    bits = ""
    x, y, direction = 20, 20, -1
  
    while len(bits) < 76:
        for i in range(2):
            bits += str(qrcode[x][y-i] ^ ((x + y - i) % 2 == 0))
        x += direction
        if x == 8 or x > 20:
            direction *= -1
            x += direction
            y -= 2

    length = int(bits[4:12], 2)
    message = "".join(chr(int(bits[i:i+8], 2)) for i in range(12, length * 8 + 12, 8))

    return message
