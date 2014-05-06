def checkio(text):
    nopunc=""
    alph="abcdefghijklmnopqrstuvwxyz"
    for char in text:
        if char.lower() in alph:
            nopunc+=char.lower()
    
    maxcount=1
    mostfreq=""
    
    for letter in nopunc:
        if nopunc.count(letter)>maxcount:
            maxcount=nopunc.count(letter)
            mostfreq=letter
	elif nopunc.count(letter)==maxcount:
            if alph.find(letter)<alph.find(mostfreq):
                mostfreq=letter
            elif mostfreq=="":
                mostfreq=letter
                
    return mostfreq
