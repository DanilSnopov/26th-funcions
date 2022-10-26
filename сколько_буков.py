def howmuch(bukvi):
    bukvi = bukvi.lower()
    povtor = []
    for i in range(len(bukvi)):
        if bukvi[i] in bukvi[:i] + bukvi[i+1:] and not bukvi[i] in povtor:
            povtor.append(bukvi[i])
    return len(povtor)
print(howmuch('abababab'))