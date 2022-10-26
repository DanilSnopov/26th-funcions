def letter(bukvi):
    return len([ch for ch in (set(bukvi.lower())) if bukvi.lower().count(ch) > 1])
print(letter('abababab'))