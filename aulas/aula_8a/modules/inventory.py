
class inventory:
    inventory_id = ""
    film_id = ""
    store_id = ""
    last_update = ""
    
    def __init__(self, i_id, f_id, s_id, ls):
        try:
            self.inventory_id = i_id
            self.film_id = f_id
            self.store_id = s_id
            self.last_update = ls
        except Exception as e:
            print(str(e))
            
    def get_inventory_id(self):
        return self.inventory_id
