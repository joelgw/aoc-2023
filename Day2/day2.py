import numpy

possible = {
        'red': 12,
        'green': 13,
        'blue': 14
        }

def challenge1(infile):
    possible_ids = []
    for line in infile:
        line = line.rstrip()
        game = line.split(': ')
        game_possible = True
        for pull in game[1].split('; '):
            for grab in pull.split(', '):
                event = grab.split(' ')
                if possible[event[1]] < int(event[0]):
                    game_possible = False
        if game_possible:
            possible_ids.append(int(game[0].split(' ')[1]))
    print('Challenge 1 Sum: {}'.format(sum(possible_ids)))

def challenge2(infile):
    powers = []
    for line in infile:
        line = line.rstrip()
        game = line.split(': ')
        mins = {
                'red': None,
                'green': None,
                'blue': None
                }
        for pull in game[1].split('; '):
            for grab in pull.split(', '):
                event = grab.split(' ')
                if mins[event[1]] == None:
                    mins[event[1]] = int(event[0])
                elif mins[event[1]] < int(event[0]):
                    mins[event[1]] = int(event[0])
        values = []
        for item in mins.values():
            values.append(item)
        powers.append(numpy.prod(values))

    print('Challenge 2 Powers sum: {}'.format(sum(powers)))

def main():
    with open("input.txt") as file:
        infile = file.readlines()

    challenge1(infile)
    challenge2(infile)

if __name__ == "__main__":
    main()
