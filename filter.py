def prob(count1, total1, count2, total2):
    firstRatio = (1.0*count1)/total1
    secondRation = (1.0*count2)/total2
    combined = firstRatio / (firstRatio + secondRatio)
    split = 1.0
    unknown = .5
    notSplit = 1.0*count1 + 1.0*count2
    return ((split * unknown) + (notSplit * combined)) / (split + notSplit)
