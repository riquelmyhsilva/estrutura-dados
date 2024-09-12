letters = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]

target = "hello world"
construct = ""

for caracter in target[1 - len(target)]:
    for letter in letters:
        if caracter == target[1 - len(target)]:
            construct += letter
            print(construct)
