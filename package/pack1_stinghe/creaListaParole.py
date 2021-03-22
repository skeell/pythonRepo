def creaListaParole(file):
    with open(file, "r")as f:
        s = f.read()
        sv = s.split()
