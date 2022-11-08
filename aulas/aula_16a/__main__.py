from modules.test import Test

obj = Test("Felipe", "123124124", 99, "3532323134")
obj.add_id_compra(14)
obj.add_id_compra(4)
obj.add_id_compra(7)
obj.add_id_compra(12)
obj.add_id_compra(9)

print(obj.get_id_compras())
