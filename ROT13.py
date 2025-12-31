import argparse

def rot13(cipher_text):
    plain_text = ""
    for c in cipher_text:
        if 'A' <= c <= 'Z':
            plain_text += chr((ord(c) - ord('A') + 13) % 26 + ord('A'))
        elif 'a' <= c <= 'z':
            plain_text += chr((ord(c) - ord('a') + 13) % 26 + ord('a'))
        else:
            plain_text += c
    return plain_text

def main():
    try :
        parser = argparse.ArgumentParser()
        parser.add_argument("--input", "-i",required=True, help="the input to apply rot13 on")
        args = parser.parse_args()
        cipher_text = str(args.input)
        plain_text = rot13(cipher_text)
        print(f'this is the flag : {plain_text}')
    except Exception :
        print("!!")

if __name__ == "__main__":
    main()