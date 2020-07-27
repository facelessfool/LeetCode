def longestCommonPrefix(self, strs: List[str]) -> str:
    if(len(strs) == 0):
        return("")
    minStr = min(strs, key=lambda x: len(x))
    j = 0
    counter = -1
    index = 0
    for i in range(0, len(minStr)):
        counter = 0
        for j in range(0, len(strs)):
            if(minStr[i] == strs[j][i]):
                counter += 1
            else:
                break
        if(counter == len(strs)):
            index += 1

    if(index == 0):
        return ("")
    res = minStr[slice(index)]

    return (res)
