genero=input("Digite m-masculino e f-feminino").upper()
idade=int(input("Digite a idade"))
if genero == "M" and idade >=18:
    print("apto a se alistar")
else:
    print("não apto a se alistar-")
