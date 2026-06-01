for i in range(0,5):
    x=int(input("Digite um valor "))
    v = x % 2
    if v == 1:
        print(f"o valor {x} é impar")
    else:
        print(f"o valor {x} é par")
print("esta fora do laço")