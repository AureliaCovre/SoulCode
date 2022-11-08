try:
    peso_do_individuo: 89     #Altura deve ser em metros (m)
    altura_do_individuo: 1.70 #Peso deve ser em kilogramas (kg)
    imc = peso_do_individuo / (altura_do_individuo*altura_do_individuo)
    if 0 < imc < 18.5:
        print("Desnutrido")
    elif 18.5 <= imc > 24.9:
        print("Peso normal")
    elif 24.9 <= imc < 30:
        print("Sobrepeso")
    elif imc >= 30:
        print("Obesidade")
    else:
        print("ERRO: peso: ", imc, "altura: ", altura_do_individuo)

except Exception as e:
    print("ERRO: ", str(e))
