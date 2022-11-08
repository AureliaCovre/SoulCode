from modules.connector import interface_db
#from modules.class_vendas import Vendas

if __name__ == "__main__":
           
    try:
      while True:
        selecao = input("Para gerar o relatorio tecle enter")
        
        #o total de vendas
        interface = interface_db("root", "aurelia1", "127.0.0.1", "mydb")
        dados = interface.selecionar("SELECT sum(valor_total) as total_vendas from vendas")
        print("O faturamento total foi de R$:  ",dados[0][0])
        print("-----------------------------------------------------------------------------------")
            
        #o funcionário que realizou a maior venda e qual o total desta
        interface = interface_db("root", "aurelia1", "127.0.0.1", "mydb")
        dados = interface.selecionar("SELECT a.nome_vend, b.valor_total from vendedor a, vendas b where a.idvendedor = b.idvendedor order by valor_total desc limit 1")
        print("O funcionario que realizou maior venda foi: ",dados[0][0])
        print("No valor de R$: ",dados[0][1])
        print("-----------------------------------------------------------------------------------")
                        
        #o funcionário que realizou a maior quantidade de vendas e quantas foram
        interface = interface_db("root", "aurelia1", "127.0.0.1", "mydb")
        dados = interface.selecionar("SELECT a.nome_vend, count(b.idvendedor) as qtdvendas from vendedor a, vendas b where b.idvendedor = a.idvendedor group by a.nome_vend order by qtdvendas desc limit 1") 
        print("O funcionario que realizou maior quantidade de vendas foi: ",dados[0][0])
        print("No no total de:  ",dados[0][1])
        print("-----------------------------------------------------------------------------------")
        
        #o fornecedor mais utilizado
        interface = interface_db("root", "aurelia1", "127.0.0.1", "mydb")
        dados = interface.selecionar("SELECT p.idfornecedor, f.nome_forn, count(p.idfornecedor) as contagem FROM fornecedor f, produto p where f.idfornecedor = p.idfornecedor GROUP BY idfornecedor ORDER BY contagem desc limit 1")
        print("Codigo do fornecedor: ",dados[0][0])
        print("Fornecedor mais utilizado: ",dados[0][1])
        print("Total de atendimento: ", dados[0][2])
        print("-----------------------------------------------------------------------------------")
            
        #o total de comissão devido a cada funcionário considerando-se 8% de comissão    
        interface = interface_db("root", "aurelia1", "127.0.0.1", "mydb")
        dados = interface.selecionar("SELECT a.nome_vend, SUM(b.valor_total)*0.08 as comissao FROM vendedor a, vendas b where a.idvendedor = b.idvendedor GROUP BY nome_vend ORDER BY comissao DESC")
        lista = []
        for item in range(len(dados)):
            print("Vendedor/comissão:", dados[item])
        break
            
    except Exception as e:
        print(str(e))
