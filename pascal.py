def pascal(n):
    if n == 1:
        return [1]
    else:
        thisLine = [1]
        previousLine = pascal(n-1)
        for i in range(len(previousLine)-1):
            thisLine.append(previousLine[i] + previousLine[i+1])
        thisLine += [1]
    return thisLine

for i in range (1,7) :
    print(pascal(i))