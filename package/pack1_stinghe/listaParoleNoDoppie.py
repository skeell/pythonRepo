def listaNoDoppie(file):
    with open(file, "r")as f:
        s = f.read()
        sv = s.split()
        ris = []
        for elem in sv:
            if elem not in ris:
                ris.append(elem)
            ris.sort()
            return ris
