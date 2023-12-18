import sys
import math

message_1 = input()
message_2 = input()
message_3 = input()

#

def xor_hex_strings(hex_str1, hex_str2):
  
    int_val1 = int(hex_str1, 16)
    int_val2 = int(hex_str2, 16)

    result_int = int_val1 ^ int_val2
    result_hex = format(result_int, '02x')

    return result_hex

clear_message_hex = xor_hex_strings(xor_hex_strings(message_1, message_2), message_3)

clear_message_ascii = bytes.fromhex(clear_message_hex).decode('ascii')

print(clear_message_ascii)
