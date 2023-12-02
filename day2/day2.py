import re

def a():
    numRed = 12
    numGreen = 13
    numBlue = 14

    ret = 0
    with open("input.txt", "r") as fp:
        for line in fp.readlines():
            # ^Game\W+(?P<id>\d):(\W+([^;]+;))+(\W+([^;]+))?
            possible = True
            for group in line.split(';'):
                for m in re.finditer(r'((?P<red>\d+) red)|((?P<green>\d+) green)|((?P<blue>\d+) blue)', group):
                    colors = m.groupdict(default="0")
                    if int(colors["red"]) > numRed or int(colors["green"]) > numGreen or int(colors["blue"]) > numBlue:
                        possible = False
                        break
                if not possible:
                    break
            if possible:
                ret += int(re.match(r'^Game\W+(?P<id>\d+):', line)["id"])
    return ret


def b():
    ret = 0
    with open("input.txt", "r") as fp:
        for line in fp.readlines():
            maxRed = 0
            maxGreen = 0
            maxBlue = 0

            for group in line.split(';'):
                for m in re.finditer(r'((?P<red>\d+) red)|((?P<green>\d+) green)|((?P<blue>\d+) blue)', group):
                    colors = m.groupdict(default="0")
                    if int(colors["red"]) > maxRed:
                        maxRed = int(colors["red"])
                    if int(colors["green"]) > maxGreen:
                        maxGreen = int(colors["green"])
                    if int(colors["blue"]) > maxBlue:
                        maxBlue = int(colors["blue"])
            
            ret += maxRed * maxGreen * maxBlue
    return int(ret)


print(a())
print(b())