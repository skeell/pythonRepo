def creaListaListe(file, separatore):
    with open(file, "r")as f:
        sv = []
        for elem in f:
            elem = elem.strip() .split(separatore)
            print(elem)
            sv.append(elem)
        return sv

