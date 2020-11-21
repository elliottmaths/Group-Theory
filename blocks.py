def Omega(n):
    return list(range(1, n+1))

def powerset(s):
    x = len(s)
    masks = [1 << i for i in range(x)]
    for i in range(1 << x):
        yield [ss for mask, ss in zip(masks, s) if i & mask]

def alpha(x, order):
    value = (x + 1) % order
    if value == 0:
        return order
    return value

def beta(x, order):
    FunctionDict = dict()
    FunctionDict[1] = 1
    for i in range(2, order + 1):
        entry = order - i + 2
        FunctionDict[i] = entry
    return FunctionDict[x]

order = 4

blocks = []
for subset in powerset(Omega(order)):
    IsABlock = True
    for reflection in range(2):
        if reflection == 0:
            for NumOfRotations in range(order):
                ImageList = []
                for element in subset:
                    NewElement = element
                    for rotation in range(NumOfRotations):
                        NewElement = alpha(NewElement, order)
                    ImageList.append(NewElement)
                if set(ImageList) != set(subset) and not set(subset).isdisjoint(set(ImageList)):
                    IsABlock = False
        else:
            for NumOfRotations in range(order):
                ImageList = []
                for element in subset:
                    NewElement = element
                    for rotation in range(NumOfRotations):
                        NewElement = alpha(NewElement, order)
                    NewElement = beta(NewElement, order)
                    ImageList.append(NewElement)
                if set(ImageList) != set(subset) and not set(subset).isdisjoint(set(ImageList)):
                    IsABlock = False
    if IsABlock:
        blocks.append(subset)

print(blocks)
