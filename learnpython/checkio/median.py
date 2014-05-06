def checkio(data):
    data.sort()
    if len(data)%2==0:
        x=(len(data)/2)-1
        y=(len(data)/2)
        ret=(data[x]+data[y])/2
        return ret
    else:
        ind=(len(data)-1)/2
