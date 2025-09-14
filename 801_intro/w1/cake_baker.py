import time
bakery = False
required_ingredients = ['a', 'b', 'c']
what_i_got = ['a', 'b', 'c']

def purchase():
    pass

def collect_ingredients(what_i_got):
    if what_i_got == required_ingredients:
        return True
    else:
        return False
    
def baking(required_ingredients):
    is_it_done = False
    processed_ingredients = []

    def pre_processing(required_ingredients):
        return processed_ingredients
    
    def start_baking(processed_ingredients):
        done = False
        if done:
             return True
         

    while not is_it_done:
        if pre_processing(required_ingredients):
              if start_baking(processed_ingredients):
                   is_it_done = True
        return True
              

if bakery:
    purchase()
else:
    if collect_ingredients(what_i_got):
            baking(required_ingredients)
    else:
         pass
        
