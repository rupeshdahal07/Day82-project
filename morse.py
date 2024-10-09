letters = str(input("Give any message to convert onto morse code: ").upper())

morse_code_dict = {
    'A': '·-', 'B': '-···', 'C': '-·-·', 'D': '-··', 'E': '·', 'F': '··-·',
    'G': '--·', 'H': '····', 'I': '··', 'J': '·---', 'K': '-·-', 'L': '·-··',
    'M': '--', 'N': '-·', 'O': '---', 'P': '·--·', 'Q': '--·-', 'R': '·-·',
    'S': '···', 'T': '-', 'U': '··-', 'V': '···-', 'W': '·--', 'X': '-··-',
    'Y': '-·--', 'Z': '--··',
    '1': '·----', '2': '··---', '3': '···--', '4': '····-', '5': '·····',
    '6': '-····', '7': '--···', '8': '---··', '9': '----·', '0': '-----'
}

output = []
for letter in letters:
    for key, value in morse_code_dict.items():
        if letter == key:
            output.append(value)
        elif letter == " ":
            output.append("\t")

code = ' '.join(output)
print(code)
