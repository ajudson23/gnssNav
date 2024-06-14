import pynmea2

file = open(r'/Users/ashleyjudson/Documents/testing/summerGames/testingFile.txt', encoding='utf-8')

for line in file.readlines():
    try:
        msg = pynmea2.parse(line)
        print(repr(msg))
    except pynmea2.ParseError as e:
        print('Parse error: {}'.format(e))
        continue

# organize this code and take the important stuff 