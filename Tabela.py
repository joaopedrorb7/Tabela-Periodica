tabela={
  "H": {"nome": "hidrogênio", "massa": 1.008, "numeroAtm": 1},
  "He": {"nome": "hélio", "massa": 4.0026, "numeroAtm": 2},
  "Li": {"nome": "lítio", "massa": 6.94, "numeroAtm": 3},
  "Be": {"nome": "berílio", "massa": 9.0122, "numeroAtm": 4},
  "B": {"nome": "boro", "massa": 10.81, "numeroAtm": 5},
  "C": {"nome": "carbono", "massa": 12.011, "numeroAtm": 6},
  "N": {"nome": "nitrogênio", "massa": 14.007, "numeroAtm": 7},
  "O": {"nome": "oxigênio", "massa": 15.999, "numeroAtm": 8},
  "F": {"nome": "flúor", "massa": 18.998, "numeroAtm": 9},
  "Ne": {"nome": "neônio", "massa": 20.180, "numeroAtm": 10},
  "Na": {"nome": "sódio", "massa": 22.990, "numeroAtm": 11},
  "Mg": {"nome": "magnésio", "massa": 24.305, "numeroAtm": 12},
  "Al": {"nome": "alumínio", "massa": 26.982, "numeroAtm": 13},
  "Si": {"nome": "silício", "massa": 28.085, "numeroAtm": 14},
  "P": {"nome": "fósforo", "massa": 30.974, "numeroAtm": 15},
  "S": {"nome": "enxofre", "massa": 32.06, "numeroAtm": 16},
  "Cl": {"nome": "cloro", "massa": 35.45, "numeroAtm": 17},
  "Ar": {"nome": "argônio", "massa": 39.948, "numeroAtm": 18},
  "K": {"nome": "potássio", "massa": 39.098, "numeroAtm": 19},
  "Ca": {"nome": "cálcio", "massa": 40.078, "numeroAtm": 20},
  "Sc": {"nome": "escândio", "massa": 44.955, "numeroAtm": 21},
  "Ti": {"nome": "titânio", "massa": 47.867, "numeroAtm": 22},
  "V": {"nome": "vanádio", "massa": 50.942, "numeroAtm": 23},
  "Cr": {"nome": "cromo", "massa": 51.996, "numeroAtm": 24},
  "Mn": {"nome": "manganês", "massa": 54.938, "numeroAtm": 25},
  "Fe": {"nome": "ferro", "massa": 55.845, "numeroAtm": 26},
  "Co": {"nome": "cobalto", "massa": 58.933, "numeroAtm": 27},
  "Ni": {"nome": "níquel", "massa": 58.693, "numeroAtm": 28},
  "Cu": {"nome": "cobre", "massa": 63.546, "numeroAtm": 29},
  "Zn": {"nome": "zinco", "massa": 65.38, "numeroAtm": 30},
  "Ga": {"nome": "gálio", "massa": 69.723, "numeroAtm": 31},
  "Ge": {"nome": "germânio", "massa": 72.63, "numeroAtm": 32},
  "As": {"nome": "arsênio", "massa": 74.922, "numeroAtm": 33},
  "Se": {"nome": "selênio", "massa": 78.971, "numeroAtm": 34},
  "Br": {"nome": "bromo", "massa": 79.904, "numeroAtm": 35},
  "Kr": {"nome": "criptônio", "massa": 83.798, "numeroAtm": 36},
  "Rb": {"nome": "rubídio", "massa": 85.468, "numeroAtm": 37},
  "Sr": {"nome": "estrôncio", "massa": 87.62, "numeroAtm": 38},
  }
while True:
    op=int(input("\n1.buscar elemento\n2.sair"))
    if op==1:
        filtro=int(input("digite o número atômico do elemento:\n"))
        for elemento in tabela:
            if tabela[elemento]["numeroAtm"]==filtro:
               print(f"elemento encontrado:{elemento}-{tabela[elemento]}")
            
    elif op==2:
        print("você saiu")
        break 
    else:
        print ("comando inválido")
        break           

