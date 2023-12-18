import sys
import math

message = input()

def decode_shift_cipher(encoded_message, shift):
    decoded_message = ""
    for char in encoded_message:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            decoded_char = chr((ord(char) - base - shift) % 26 + base)
            decoded_message += decoded_char
        else:
            decoded_message += char
    return decoded_message

def calculate_frequency_difference(decoded_message):
    frequency_list = {
        'A': 8.08, 'B': 1.67, 'C': 3.18, 'D': 3.99, 'E': 12.56,
        'F': 2.17, 'G': 1.80, 'H': 5.27, 'I': 7.24, 'J': 0.14,
        'K': 0.63, 'L': 4.04, 'M': 2.60, 'N': 7.38, 'O': 7.47,
        'P': 1.91, 'Q': 0.09, 'R': 6.42, 'S': 6.59, 'T': 9.15,
        'U': 2.79, 'V': 1.00, 'W': 1.89, 'X': 0.21, 'Y': 1.65, 'Z': 0.07
    }

    decoded_frequency = {}
    total_letters = sum(c.isalpha() for c in decoded_message)

    for char in decoded_message:
        if char.isalpha():
            char_upper = char.upper()
            decoded_frequency[char_upper] = decoded_frequency.get(char_upper, 0) + 1

    difference = 0
    for char, observed_frequency in decoded_frequency.items():
        expected_frequency = frequency_list[char] * total_letters / 100
        difference += abs(observed_frequency - expected_frequency)

    return difference

best_shift = 0
min_difference = float('inf')

for shift in range(26):
    decoded_message_attempt = decode_shift_cipher(message, shift)
    difference = calculate_frequency_difference(decoded_message_attempt)
    if difference < min_difference:
        min_difference = difference
        best_shift = shift

decoded_message = decode_shift_cipher(message, best_shift)
print(decoded_message)
