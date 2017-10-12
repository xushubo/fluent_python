import promotions
import inspect

print(inspect.getmembers(promotions, inspect.isfunction))
promos = [func for name, func in 
                inspect.getmembers(promotions, inspect.isfunction)
                if name.endswith('_promo') and not name.startswith('best')]
print(promos)