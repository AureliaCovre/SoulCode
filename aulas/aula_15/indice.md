-- --------------------------------------------------
-- CONECTANDO E POPULANDO O BANCO DE DADOS MONGO
-- --------------------------------------------------
# 1.Criar Conector;
# 2.Classe Item com metodo Many (para inserções diversas) com nome e cpf;
# 3.Criar lista para inserção;
# 4.Criar objetos para converter em dicionário;
# 5.Retornar o dicionário e salvar ele na lista - return {"nome": self.get_nome(), "cpf": self.get_cpf()}


-- --------------------------------------------------

-- --------------------------------------------------
# 1 .Lista vazia
# 2. Iterar nos dados que veio do banco
# 3. Criar um objeto com os dados que foram iterados
# 4. Adicionar na lista vazia os objetos

-- --------------------------------------------------
-- UPTADATE PARA CORRIGIR OS CPF'S DA KELY
-- --------------------------------------------------
# 1. Utilizar a lista2 tipo dicionário vem do banco MongoDB;
# 2. Realizar a consulta da quantidade de informações que tem no banco;
# 3. Criar uma lista dos cpf corretos;
# 4. Utilizar o metodo set;

-- --------------------------------------------------
-- APRENDENDO SOBRE DELETE
-- --------------------------------------------------
# 1. Descobrir o que quer deletar (fazer a lista das informações);
# 2. Deletar usando  deleteOne;
# 3. Deletar vários com delete Many;
