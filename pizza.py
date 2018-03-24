# Orginalrecept och kod av Pokemonkejsarn https://github.com/pokemonkejsaren/c_recipes/blob/master/pizza.c
# Pythonifierad
# Basala vikten i gram för en pizza, ca 170 g normalstor
base_weight = 170

# Jaga heltal eller float
try:
    nbr_eaters = int(input("Antal pizzor? Endast siffror:  "))
except ValueError:
    try:
        nbr_eaters = float(input("Antal som ska äta pizza? "))
    except ValueError:
        print("Det var ju för fan ingen siffra")
        quit()
        
weight = base_weight * nbr_eaters

# Proportionerna * totala degmassan för antalet pizzor
flour = 1.0*weight
water = 0.610*weight
oil = 0.075*weight
yeast = 0.005*weight
salt = 0.02*weight

print("Ingredienser:")
print(' - Vetemjöl: {0}g \n - Vatten: {1}g \n - Olja: {2}g \n - Jäst: {3}g \n - Salt: {4}g'.format(flour, water, oil, yeast, salt))
print("Instruktioner:")
print("Lös upp jästen, lägg till alla ingredienser, knåda...KNÅDA")
print("låt jäsa åtminstone 18h i kyl lmao")
print("forma en pizza")
print("baka så jävla varmt som möjligt på pizzasten")
