import custom_cyphers

# Coin Head
# ELIZABETH II - AUSTRALIA 2022 #
#      3 26      1 5     4      #
# Numbers are decoded from Braille
head = "ATBASH"

# Cypher on the outside track of the back
outer_string = "DVZIVZFWZXRLFHRMXLMXVKGZMWNVGRXFOLFHRMVCVXFGRLM.URMWXOZIRGBRM7DRWGSC5WVKGS."

# Cypher on the inside track of the back
inner_string = "BGOAMVOEIATSIRLNGTTNEOGRERGXNTEAIFCECAIEOALEKFNR5LWEFCHDEEAEEE7NMDRXX5"

# Hexadecimal in lower right third of back
hexadecimal  = "E3B8287D4290F7233814D7A47A291DC0F71B2806D1A53B311CC4B97A0E1CC2B93B31068593332F10C6A3352F14D1B27A3514D6F7382F1AD0B0322955D1B83D3801CDB2287D05C0B82A311085A033291D85A3323855D6BC333119D6FB7A3C11C4A72E3C17CCBB33290C85B6343955CCBA3B3A1CCBB62E341ACBF72E3255CAA73F2F14D1B27A341B85A3323855D6BB333055C4A53F3C55C7B22E2A10C0B97A291DC0F73E3413C3BE392819D1F73B331185A3323855CCBA2A3206D6BE3831108B"


# This is where the fun begins
print('---- Cyper 1')
print(head)
print('')

print('---- Cyper 2')
for cypher in outer_string.split('.'):
    if cypher != '':
        print(custom_cyphers.atbash(cypher))
print('')

print('---- Cyper 3')
print(custom_cyphers.clarity_matrix(inner_string, 7, 5))
print('')

print('---- Cyper 4')
hexadecimal_xor = "A5 D7 5A 5D 75" # A5D75 repeated twice to make 5 complete bytes

bytes_a = bytes.fromhex(hexadecimal.replace(" ", ""))
bytes_b = bytes.fromhex(hexadecimal_xor.replace(" ", ""))
print(custom_cyphers.byte_xor(bytes_a, bytes_b).decode("ascii"))
print('')

print('---- Bonus Cyper')
# Bonus Level
# Outer Ring
# Shaded are spaces since they're least common, dark is a dot, and light is a dash.
bonus_outer = ".---- ----. ....- --... -.. ... -... .- .-.. -... . .-. - .--. .- .-. -.-"
print(custom_cyphers.morse_decrypt(bonus_outer))

# Shadded are zero, Light is 1
# The original is 7 bit by 10 characters, i have padded this to 8 bit by 10 chacters
bonus_inner = "01000001 01010011 01000100 01000011 01100010 01110010 00110010 00110000 00110010 00110010"
n = int(bonus_inner.replace(' ', ''), 2)
print(n.to_bytes((n.bit_length() + 7) // 8, 'big').decode())
