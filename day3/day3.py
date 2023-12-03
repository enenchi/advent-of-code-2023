
def a(filepath):
    engine = 0
    with open(filepath, "r") as fp:
        parts = dict()
        partLocs = dict()
        symbols = list()

        parts[0] = 0

        partId = 1
        for row, line in enumerate(fp.readlines()):
            part = ""
            for col, c in enumerate(line):
                if c.isdigit():
                    part += c
                    partLocs[(row, col)] = partId
                else:
                    if c != "." and c != "\n":
                        symbols.append((row, col))
                    if part:
                        parts[partId] = int(part)
                        partId += 1
                        part = ""
        
        usedParts = set()
        for row, col in symbols:
            usedParts.add(partLocs.get((row - 1, col - 1), 0))
            usedParts.add(partLocs.get((row - 1, col), 0))
            usedParts.add(partLocs.get((row - 1, col + 1), 0))

            usedParts.add(partLocs.get((row, col - 1), 0))
            usedParts.add(partLocs.get((row, col + 1), 0))

            usedParts.add(partLocs.get((row + 1, col - 1), 0))
            usedParts.add(partLocs.get((row + 1, col), 0))
            usedParts.add(partLocs.get((row + 1, col + 1), 0))

        for usedPart in usedParts:
            engine += parts[usedPart]
    
    return engine
        


def b(filepath):
    gearRatios = 0
    with open(filepath, "r") as fp:
        parts = dict()
        partLocs = dict()
        symbols = list()

        parts[0] = 0

        partId = 1
        for row, line in enumerate(fp.readlines()):
            part = ""
            for col, c in enumerate(line):
                if c.isdigit():
                    part += c
                    partLocs[(row, col)] = partId
                else:
                    if c == "*":
                        symbols.append((row, col))
                    if part:
                        parts[partId] = int(part)
                        partId += 1
                        part = ""
        
        for row, col in symbols:
            usedParts = set()

            usedParts.add(partLocs.get((row - 1, col - 1), 0))
            usedParts.add(partLocs.get((row - 1, col), 0))
            usedParts.add(partLocs.get((row - 1, col + 1), 0))

            usedParts.add(partLocs.get((row, col - 1), 0))
            usedParts.add(partLocs.get((row, col + 1), 0))

            usedParts.add(partLocs.get((row + 1, col - 1), 0))
            usedParts.add(partLocs.get((row + 1, col), 0))
            usedParts.add(partLocs.get((row + 1, col + 1), 0))

            usedParts.remove(0)

            if len(usedParts) == 2:
                a, b = usedParts
                gearRatios += parts[a] * parts[b]
    
    return gearRatios


print(a("test.txt"))
print(a("input.txt"))
print(b("test.txt"))
print(b("input.txt"))