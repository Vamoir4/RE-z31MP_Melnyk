mport sys
import math

operation = input()

shift_start = int(input())

rotors = []
for i in range(3):
    rotors.append(input())

message = input()

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def caesar_shift(text, shift, reverse=False):
    shifted_text = ""
    for char in text:
        index = alphabet.find(char)
        new_index = (index + shift) % 26 if not reverse else (index - shift) % 26
        shifted_text += alphabet[new_index]
        shift += 1
    return shifted_text

def map_to_rotor(text, rotor, reverse=False):
    mapped_text = ""
    for char in text:
        index = alphabet.find(char) if not reverse else rotor.find(char)
        mapped_text += rotor[index] if not reverse else alphabet[index]
    return mapped_text

if operation == 'ENCODE':
    shifted_message = caesar_shift(message, shift_start)

    for rotor in rotors:
        shifted_message = map_to_rotor(shifted_message, rotor)

    print(shifted_message)

elif operation == 'DECODE':
    for rotor in reversed(rotors):
        message = map_to_rotor(message, rotor, reverse=True)

    decrypted_message = caesar_shift(message, shift_start, reverse=True)

    print(decrypted_message)

else:
    print("Invalid operation mode")
