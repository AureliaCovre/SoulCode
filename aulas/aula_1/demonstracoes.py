try:
    # 0 = falso, desligado, inativo / 1 = verdadeiro, ligado, ativo
    alarme_incendio_piso1 = True
    alarme_incendio_piso2 = True
    alarme_incendio_piso3 = False
    if alarme_incendio_piso1 == 1 or alarme_incendio_piso2 == 1 or alarme_incendio_piso3 == 1:
        print("ALARME! CORREEEEEEE")

except Exception as e:
    print(str(e))


