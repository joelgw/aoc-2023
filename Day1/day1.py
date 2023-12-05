from word2number import w2n

def read_first_num(line):
    for c in line:
        if c.isdigit():
            return c
    return None

def c2_read_first_num(line):
    letters_before_num = ""
    for c in line:
        if c.isdigit():
            return c
        else:
            letters_before_num += c
        hasword, num = check_word(letters_before_num)
        if hasword:
            return num
    return None

def read_last_num(line):
    for c in reversed(line):
        if c.isdigit():
            return c
    return None

def c2_read_last_num(line):
    letters_after_num = ""
    for c in "".join(reversed(line)):
        if c.isdigit():
            return c
        else:
            letters_after_num += c 
        hasword, num = check_word("".join(reversed(letters_after_num)))
        if hasword:
            return num
    return None

def check_word(string):
    nums = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    for num in nums:
        if num in string:
            return True, str(w2n.word_to_num(num))
    return None, None


def challenge1(infile):
    numbers = []
    for line in infile:
        first_num = read_first_num(line)
        second_num = read_last_num(line)
        numbers.append(int(first_num + second_num))

    print("Sum of numbers Challenge 1: {}".format(sum(numbers)))

def challenge2(infile):
    numbers = []
    for line in infile:
        first_num = c2_read_first_num(line)
        second_num = c2_read_last_num(line)
        numbers.append(int(first_num + second_num))

    print("Sum of numbers Challenge 2: {}".format(sum(numbers)))

def main():
    with open("day1_input.txt") as file:
        infile = file.readlines()

    challenge1(infile)
    challenge2(infile)

if __name__ == "__main__":
    main()
