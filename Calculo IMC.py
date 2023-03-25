peso = float(input("Digite o peso da pessoa em kg: "))
altura = float(input("Digite a altura da pessoa em metros: "))

imc = peso / (altura ** 2)

if imc < 18.5:
    print("A pessoa esta abaixo do peso.")
elif imc >= 18.5 and imc < 25:
    print("A pessoa esta com o peso normal.")
elif imc >= 25 and imc < 30:
    print("A pessoa esta acima do peso.")
else:
    print("A pessoa esta com obesidade.")