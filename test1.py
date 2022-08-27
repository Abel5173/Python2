def main():
    plate = input()
    if is_valid(plate):
        print('Valid')
    else:
        print('Invalid')

def is_valid(s):
    # Numbers cannot be used in the middle of a plate
    for x in range(len(s)):
        if s[x].isdigit():
            if not s[x:].isdigit():
                return False

    return True

main()