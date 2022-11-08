from modules.pessoa import Pessoa
from modules.aluno import Aluno
from modules.funcionario import Funcionario
from modules.aluno_portugues import Aluno_p
from modules.aluno_mat import Aluno_m


if __name__ == "__main__":
    
    #Instanciando aurelia na classe pessoa
    aurelia = Pessoa("Aurélia", "12345687", "rua d", "99999999")
    maria = Pessoa("Maria", "147852", "rua a", "8888888")
    pedro = Pessoa("Pedro", "963258741", "rua b", "7777777")
    joao = Pessoa("Joao", "4561238", "rua f", "666666")
    luzia = Pessoa("luzia", "123687", "rua g", "555555")
    
    print("Relação Pessoa: ")
    aurelia.print_nome()
    aurelia.print_rg()
    aurelia.print_endereco()
    aurelia.print_contato() 
    
    maria.print_nome()
    maria.print_rg()
    maria.print_endereco()
    maria.print_contato()    
    
    pedro.print_nome()
    pedro.print_rg()
    pedro.print_endereco()
    pedro.print_contato()    
    
    joao.print_nome()
    joao.print_rg()
    joao.print_endereco()
    joao.print_contato()    
    
    luzia.print_nome()
    luzia.print_rg()
    luzia.print_endereco()
    luzia.print_contato()    
     
       
    
    maria = Funcionario("Maria", "12345687", "rua d", "99999999", "001", "Assistente")
    pedro = Funcionario("pedro", "147852", "rua a", "8888888", "002", "Analista")
    julia = Funcionario("julia", "963258741", "rua b", "7777777", "003", "Faxineira")
    clara = Funcionario("clara", "4561238", "rua f", "666666", "004", "Secretaria")
    jose = Funcionario("jose", "123687", "rua g", "555555", "005", "Arquivo")

    print("Relação de Funcionario: ")
    maria.print_nome()
    maria.print_rg()
    maria.print_endereco()
    maria.print_contato() 
    maria.print_id()
    maria.print_cargo()
    
    pedro.print_nome()
    pedro.print_rg()
    pedro.print_endereco()
    pedro.print_contato()  
    pedro.print_id()
    pedro.print_cargo()  
    
    julia.print_nome()
    julia.print_rg()
    julia.print_endereco()
    julia.print_contato() 
    julia.print_id()
    julia.print_cargo()   
    
    clara.print_nome()
    clara.print_rg()
    clara.print_endereco()
    clara.print_contato()  
    clara.print_id()
    clara.print_cargo()  
    
    jose.print_nome()
    jose.print_rg()
    jose.print_endereco()
    jose.print_contato() 
    jose.print_id()
    jose.print_cargo()
    
    adriana = Aluno("Adriana", "12345687", "rua d", "99999999", "229771")
    bruna = Aluno("Bruna", "147852", "rua a", "8888888", "229772")
    antonio = Aluno("Antonio", "963258741", "rua b", "7777777", "229773")
    mateus = Aluno("Mateus", "4561238", "rua f", "666666", "229774")
    isabela = Aluno("Isabela", "123687", "rua g", "555555", "229775")

    print("Relação de Aluno: ")
    adriana.print_nome()
    adriana.print_rg()
    adriana.print_endereco()
    adriana.print_contato() 
    adriana.print_matricula()
    
    bruna.print_nome()
    bruna.print_rg()
    bruna.print_endereco()
    bruna.print_contato()  
    bruna.print_matricula()
     
    antonio.print_nome()
    antonio.print_rg()
    antonio.print_endereco()
    antonio.print_contato() 
    antonio.print_matricula()
         
    mateus.print_nome()
    mateus.print_rg()
    mateus.print_endereco()
    mateus.print_contato()  
    mateus.print_matricula()
  
    isabela.print_nome()
    isabela.print_rg()
    isabela.print_endereco()
    isabela.print_contato() 
    isabela.print_matricula()
       
    cleberson = Aluno_p("cleberson", "12345687", "rua d", "99999999", "229771", "7")
    carol = Aluno_p("carol", "147852", "rua a", "8888888", "229772", "8")
    amelia = Aluno_p("amelia", "963258741", "rua b", "7777777", "229773","6")
    roberta = Aluno_p("roberta", "4561238", "rua f", "666666", "229774","5")
    lucas = Aluno_p("lucas", "123687", "rua g", "555555", "229775","4")

    print("Relação de Alunos de Portugues: ")
    cleberson.print_nome()
    cleberson.print_rg()
    cleberson.print_endereco()
    cleberson.print_contato() 
    cleberson.print_matricula()
    cleberson.print_nota()
    
    carol.print_nome()
    carol.print_rg()
    carol.print_endereco()
    carol.print_contato()  
    carol.print_matricula()
    carol.print_nota()
     
    amelia.print_nome()
    amelia.print_rg()
    amelia.print_endereco()
    amelia.print_contato() 
    amelia.print_matricula()
    amelia.print_nota()
         
    roberta.print_nome()
    roberta.print_rg()
    roberta.print_endereco()
    roberta.print_contato()  
    roberta.print_matricula()
    roberta.print_nota()
  
    lucas.print_nome()
    lucas.print_rg()
    lucas.print_endereco()
    lucas.print_contato() 
    lucas.print_matricula()  
    lucas.print_nota() 
    
    cleberson = Aluno_m("cleberson", "12345687", "rua d", "99999999", "229771", "5")
    carol = Aluno_m("carol", "147852", "rua a", "8888888", "229772", "4")
    amelia = Aluno_m("amelia", "963258741", "rua b", "7777777", "229773","6")
    roberta = Aluno_m("roberta", "4561238", "rua f", "666666", "229774","7")
    lucas = Aluno_m("lucas", "123687", "rua g", "555555", "229775","8")

    print("Relação de Alunos de Matematica: ")
    cleberson.print_nome()
    cleberson.print_rg()
    cleberson.print_endereco()
    cleberson.print_contato() 
    cleberson.print_matricula()
    cleberson.print_nota()
    
    carol.print_nome()
    carol.print_rg()
    carol.print_endereco()
    carol.print_contato()  
    carol.print_matricula()
    carol.print_nota()
     
    amelia.print_nome()
    amelia.print_rg()
    amelia.print_endereco()
    amelia.print_contato() 
    amelia.print_matricula()
    amelia.print_nota()
         
    roberta.print_nome()
    roberta.print_rg()
    roberta.print_endereco()
    roberta.print_contato()  
    roberta.print_matricula()
    roberta.print_nota()
  
    lucas.print_nome()
    lucas.print_rg()
    lucas.print_endereco()
    lucas.print_contato() 
    lucas.print_matricula()  
    lucas.print_nota()   
