# Orginalrecept och kod av Pokemonkejsaren https://github.com/pokemonkejsaren/c_recipes/blob/master/pizza.c
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
flour = round((1.0*weight), 2)
water = round((0.610*weight),2)
oil = round((0.075*weight),2)
yeast = round((0.005*weight),2)
dryyeast = round(((14/50)*yeast),2)
salt = round((0.02*weight),2)

print("Ingredienser:")
print(' - Vetemjöl: {}g \n - Vatten: {}g \n - Olja: {}g \n - Jäst: {}g / Torrjäst: {}g \n - Salt: {}g'.format(flour, water, oil, yeast, dryyeast, salt))
print("Instruktioner:")
print("Lös upp jästen, lägg till alla ingredienser, knåda...KNÅDA")
print("låt jäsa åtminstone 18h i kyl lmao")
print("forma en pizza")
print("baka så jävla varmt som möjligt på pizzasten")
