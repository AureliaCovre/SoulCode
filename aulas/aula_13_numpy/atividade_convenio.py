from modules.connector import interface_db
import numpy as np

if __name__ == "__atividade_convenio__":
    try:
      interface = interface_db("root", "aurelia1", "127.0.0.1", "clinica_boa_saude") 
    #   query = "SELECT * FROM convenio"
    #   bd_convenio = interface.selecionar(query)
      
    #  lista_convenio = []
    #   media = np.median(media)
    #  print(lista_convenio) 
                   
      
      paciente = interface.selecionar("SELECT codpac, tipo as possui from tipo = "S"")
      print("Pacientes com convenio: ", paciente)
      print("-----------------------------------------------------------------------------------")
                   
    except Exception as e:
        print(str(e))    