import PySimpleGUI as sg

#Creating the Node class with its attributes

class GraphNode():
    def __init__(self, recipe, ingredients, cuisine, difficulty, link):
        self.recipe = recipe
        self.ingredients = ingredients
        self.cuisine = cuisine
        self.difficulty = difficulty
        self.link = link
        self.adjacencylist = []
        self.visited = False
        self.rating = None
        self.saved = False

    def __str__(self):
        return 'Recipe: {} \nIngredients: {} \nCuisine: {} \nDifficulty level: {} \nLink to full recipe: {}'.format(
            self.recipe, self.ingredients, self.cuisine, self.difficulty, self.link)

    # Method to input a rating after user has done the recipe
    def inputrating(self):
        if self.rating == None:
            rating = eval(input("What rating would you give this recipe after making it?"))
            self.rating = rating
            return
        else:
            x = input(
                'Do you want to leave your previous rating or input a new one? Type -leave- or -input-')  # should be just a button in the GUI (leave or change)
            if x.lower() == 'leave':
                return
            else:
                rating = eval(input("What rating would you give this recipe after making it?"))
                self.rating = rating

    # Depth-first search algorithm to show recommendations to user considering ingredients, cuisine preference and showing from easiest to hardest in
    # each cuisine:
    def dfs(self):  # the algorithm will always be ran starting at the startNode, no other nodes
        self.visited = True
        for n in self.adjacencylist:
            if not n.visited:
                x = 0
                for key in n.ingredients:
                    for i in availableIngredients:  # list of ingredients inputed by user
                        if key == i:
                            x = x + n.ingredients[key]
                if x >= 0.7:  # Add it to the recommendated recipes if the user has 70% or + of the needed ingredients (in terms of importance)
                    print(n)
                    print()
                n.dfs()

    # DFS algorithm to show the user all the recipes belonging to a specific cuisine, ignoring user's available ingredients:
    def showCuisine(self, chosenCuisine):  # always beginning at startNode
        self.visited = True
        for n in self.adjacencylist:
            if not n.visited:
                if n.cuisine == chosenCuisine:
                    print(n)
                    print()
                n.showCuisine(chosenCuisine)

    # Breadth first search algorithm to show the user all the recipes from a specific difficulty level:
    def showDifficulty(self, difficulty):
        queue = []
        queue.append(self)
        self.visited = True
        while queue:
            currentNode = queue.pop(0)
            if currentNode.difficulty == difficulty:
                print(currentNode)
                print()
            for n in currentNode.adjacencylist:
                if not n.visited:
                    n.visited = True
                    queue.append(n)

    def setVisitedFalse(
            self):  # if one of the algorithms is ran but the user wants to see recipes according to another condition
        # (for example they're shown recipes considering their ingredients but now they only want to see italian recipes), now all the
        # nodes have the visited attribute set to True because of the first algorithm so we need to set the visited attribute to false
        # again if we want to run another algorithm. This function is to address that issue
        for n in self.adjacencylist:
            n.visited = False
            n.setVisitedFalse()

    # Function for user to be able to save the recipe to access in the future whenever he/she wants:
    def saveRecipe(self):
        x = input('Save recipe? Type -yes- or -no-')  # in the GUI this would just be a button, like a saving icon
        if self.saved == False:
            if x == 'yes':
                self.saved = True
        if self.saved == True:
            if x == 'no':
                self.saved = False
        # This more or less represents touching the saving button, if it is not saved and we want to save it it will be saved. If it is saved and we say we don't want it saved, we will 'unsave' it

    # Method to display saved recipes. Would be ran when user clicks on the 'saved' section of the app.
    def savedRecipes(
            self):  # Starting at the startNode, we check all the nodes in the graph and display them if saved is set =True
        for node in self.adjacencylist:
            if not node.visited:
                if node.saved == True:
                    print(node)
                node.savedRecipes()


#Creating the functions that will be used to process the users' input regarding their ordered cuisine preferences:

def cuisineRecipe(cuisine, recipe):
  if recipe.cuisine == cuisine:
    return recipe
  else:
    None

def finalAdjList(cuisineList, recipeList):
  x = []
  for i in cuisineList:
    for n in recipeList:
      if cuisineRecipe(i, n) != None:
        x.append(n)
  return x


#Create the nodes

startNode = GraphNode('start node', {}, 'none', None, None) #this node is used as the starting point to run the traversal algorithms

pestoPasta = GraphNode('Pesto pasta', {'pasta':0.5, 'pesto':0.4, 'cheese':0.1}, 'italian', 1, 'https://www.bbcgoodfood.com/recipes/easy-pesto-pasta')
focaccia = GraphNode('Focaccia', {'bread flour':0.4, 'yeast':0.4, 'salt':0, 'olive oil':0.2}, 'italian', 1, 'https://cookpad.com/uk/recipes/13129011-grandmas-focaccia')
margheritaPizza = GraphNode('Margherita pizza', {'pizza dough':0.5, 'tomato sauce':0.2, 'cheese':0.2, 'basil':0.1}, 'italian', 1, 'https://cookieandkate.com/margherita-pizza-recipe/')
bellini = GraphNode('Bellini', {'pasta':0.3, 'butter':0.1, 'flour':0.1, 'milk':0.1, 'eggs':0.1, 'parmesan':0.1, 'salt':0, 'mozzarella':0.1, 'peppers':0.1}, 'italian', 1, 'https://dinnerthendessert.com/cheesy-florentine-pasta/')
parmesanMushroomsRisotto = GraphNode('Parmesan mushrooms risotto', {'butter':0.1, 'shallot':0.1, 'rice':0.4, 'mushrooms':0.2, 'parmesan':0.2}, 'italian', 2,'https://www.allrecipes.com/recipe/85389/gourmet-mushroom-risotto/')
spicyKaleLasagna = GraphNode('Spicy kale lasagna', {'olive oil':0.1, 'tomatoes':0.1, 'cheese':0.1, 'lasagna noodles':0.4, 'kale':0.3}, 'italian', 2, 'https://www.acouplecooks.com/spicy-kale-lasagna/')
eggplantRolls = GraphNode('Egg plant rolls with spinach and ricotta', {'eggplants':0.3, 'olive oil':0.05, 'spinach':0.2, 'ricotta':0.2, 'tomato sauce':0.1, 'breadcrumb':0.1, 'parmesan':0.05}, 'italian', 2, 'https://hungryhappens.net/eggplant-rolls-with-mozzarella-and-prosciutto/')
chickenParmesan = GraphNode('Chicken Parmesan ', {'chicken':0.3, 'parmesan':0.2, 'parsley':0.05, 'garlic':0.05, 'eggs':0.1, 'marinara sauce':0.1, 'olive oil':0.05, 'breadcrumb':0.1,'flour':0.05}, 'italian', 2, 'https://www.pinterest.es/pin/234961305547935769/')
shrimpMarinara = GraphNode('Shrimp pasta with marinara sauce', {'butter':0.1, 'parmesan':0.1, 'shrimps':0.3, 'spaghetti':0.4, 'basil':0.1}, 'italian', 3, 'https://www.acouplecooks.com/shrimp-marinara/')
italianMeatballs = GraphNode('Italian meatballs', {'ground beef':0.3, 'italian sausages':0.3, 'onion':0.05, 'garlic':0.05, 'eggs':0.1, 'parmesan':0.05, 'olive oil':0.05, 'tomatoes':0.1}, 'italian', 3, 'https://www.recipetineats.com/classic-italian-meatballs-extra-soft-and-juicy/')


chickenTacos = GraphNode('Chicken tacos', {'salt':0,'chicken':0.3, 'tortillas':0.3, 'avocado':0.2, 'cheese':0.2}, 'mexican', 1,'https://www.delish.com/cooking/recipe-ideas/recipes/a58716/easy-chicken-tacos-recipe/')
cheeseBlackBeansQuesadilla = GraphNode('Cheese black bean quesadilla', {'black beans':0.3,'tortillas':0.4, 'cheese':0.3}, 'mexican', 1, 'https://www.budgetbytes.com/hearty-black-bean-quesadillas/')
guacamoleSalsa = GraphNode('Guacamole salsa',{'salt':0,'avocado':0.3,'onion':0.3,'tomatoes':0.2,'lime':0.2}, 'mexican', 1, 'https://www.bbcgoodfood.com/recipes/guacamole-salsa')
chickenFlautas = GraphNode('Chicken flautas', {'salt':0,'chicken':0.3,'tortillas':0.3, 'avocado':0.3,'lime':0.1}, 'mexican',2, 'https://www.delish.com/cooking/recipe-ideas/a39176258/chicken-flautas-recipe/')
fishTacos = GraphNode('Fish tacos',{'salt':0,'fish':0.3,'tortillas':0.3,'onion':0.1,'tomatoes':0.1,'avocado':0.2}, 'mexican',2,'https://www.simplyrecipes.com/recipes/fish_tacos/')
mexicanFiestaRice = GraphNode('Mexican fiesta rice', {'salt':0.0, 'onion':0.2, 'peppers':0.2, 'tomatoes':0.2, 'rice':0.4}, 'mexican', 2, 'https://www.bbcgoodfood.com/recipes/mexican-fiesta-rice')
cornSoup = GraphNode('Corn soup', {'corn':0.3, 'tomatoes':0.3, 'onion':0.3, 'lime':0.1}, 'mexican', 3,'https://www.averiecooks.com/easy-30-minute-homemade-chicken-tortilla-soup/')
chilliConCarne = GraphNode('Chilli con carne', {'salt':0,'onion':0.1, 'beef':0.3,'tomatoes':0.1,'kidney beans':0.3,'rice':0.2}, 'mexican', 3,'https://www.bbcgoodfood.com/recipes/chilli-con-carne-recipe')
burrito = GraphNode('Burrito',{'salt':0,'tortillas':0.2,'black beans':0.2,'beef':0.2,'tomatoes':0.1,'onion':0.1,'avocado':0.2}, 'mexican',3,'https://www.theseasonedmom.com/easiest-burrito-recipe/')
beefBirra = GraphNode('Beef Birra',{'salt':0,'beef':0.2,'peppers':0.2,'cumin':0.1,'garlic':0.1,'onion':0.1,'vinegar':0.2, 'cilantro':0.1}, 'mexican',3, 'https://www.mexicoinmykitchen.com/beef-birria-recipe/')

patatasBravas = GraphNode('Patatas bravas',{'potatoes':0.3, 'garlic':0.1,'onion':0.2,'tomatoes':0.1,'hot sauce':0.1,'lemon':0.1,'mayonnaise':0.1},'spanish',1,'https://spanishsabores.com/patatas-bravas-recipe-spanish-fried-potatoes-with-spicy-sauce/')
garlicMushroom = GraphNode('Garlic mushrooms',{'salt':0,'mushrooms':0.4,'garlic':0.3,'lemon':0.1,'paprika':0.2},'spanish',1,'https://cafedelites.com/garlic-mushrooms/')
spanishTortilla = GraphNode('Spanish tortilla', {'salt':0,'eggs':0.4, 'potatoes':0.3,'onion':0.3}, 'spanish', 2, 'https://cooking.nytimes.com/recipes/8849-spanish-tortilla')
spanishRice = GraphNode('Spanish rice',{'salt':0,'rice':0.3,'onion':0.2,'bell pepper':0.2,'garlic':0.05,'tomatoes':0.2,'lime':0.05}, 'spanish', 2,'https://lilluna.com/food-tutorial-spanish-rice/')
chickpeaStew = GraphNode('Chickpea stew',{'chickpeas':0.3,'chilli':0.2,'garlic':0.1,'onion':0.2,'spinach':0.2}, 'spanish',2,'https://spainonafork.com/spanish-chickpea-spinach-stew-recipe/')
squid = GraphNode('Squid',{'lemon':0.2,'eggs':0.2,'squid':0.3,'flour':0.3}, 'spanish', 2,'https://leitesculinaria.com/17647/recipes-calamari-a-la-plancha.html')
salmorejo = GraphNode('Salmorejo',{'tomatoes':0.3,'garlic':0.1,'vinegar':0.3,'olive oil':0.1,'eggs':0.2},'spanish',2,'https://eatingeuropean.com/salmorejo-spanish-cold-tomato-soup-recipe/')
lentilSoup = GraphNode('Lentil soup',{'salt':0,'lentil':0.3,'potatoes':0.3,'carrots':0.1,'garlic':0.1,'pork':0.2}, 'spanish', 2,'https://www.delish.com/cooking/recipe-ideas/recipes/a44787/easy-spinach-lentil-soup-recipe/')
paella = GraphNode('Paella', {'salt':0,'rice':0.3,'lobster':0.3,'onion':0.1,'garlic':0.1,'tomatoes':0.1,'green beans':0.1}, 'spanish',3,'https://tastesbetterfromscratch.com/paella/')
churros = GraphNode('Churros', {'butter':0.2,'vanilla extract':0.1,'flour':0.2,'milk':0.2,'chocolate':0.1,'baking powder':0.1}, 'spanish',3, 'https://www.bbcgoodfood.com/recipes/churros-chocolate-dipping-sauce')


sushi = GraphNode('Sushi', {'japanese rice':0.33, 'salmon':0.33, 'seaweed':0.34}, 'japanese', 1, 'https://www.fifteenspatulas.com/homemade-sushi/')
cauliflowerTempura = GraphNode('Cauliflower', {'cauliflower':0.7, 'flour':0.1, 'eggs':0.1, 'olive oil':0.1}, 'japanese', 1,'https://food52.com/recipes/38531-cauliflower-tempura-with-sweet-chili-sauce')
yakitoriChicken = GraphNode('Yakitori chicken', {'skewers':0.2, 'soy sauce':0.1, 'chicken':0.4, 'sake':0.1, 'onion':0.1, 'sugar':0.1}, 'japanese', 1,'https://therecipecritic.com/yakitori-chicken/')
californiaMaki = GraphNode('California maki', {'japanese rice':0.2, 'nori sheets':0.2, 'salmon':0.2, 'avocado':0.2, 'cucumber':0.2}, 'japanese', 2,'https://www.yummy.ph/recipe/california-maki-recipe')
chickenTeriyaki = GraphNode('Chicken teriyaki', {'chicken':0.4, 'olive oil':0.1, 'soy sauce':0.1, 'sugar':0.1, 'vinegar':0.1, 'ginger':0.1, 'garlic':0.1}, 'japanese', 2, 'https://www.cookingclassy.com/teriyaki-chicken/')
sushiBurrito = GraphNode('Sushi burrito', {'salmon':0.1, 'tuna':0.1, 'japanese rice':0.2, 'cucumber':0.05, 'avocado':0.05, 'carrots':0.05, 'soy sauce':0.05, 'nori sheets':0.1, 'ginger':0.05}, 'japanese', 2,'https://www.feastingathome.com/sushi-burrito-recipe/')
japaneseKatsudon = GraphNode('Japenese katsudon', {'olive oil':0.05, 'onion':0.05, 'breaded pork fillet':0.3, 'soy sauce':0.05, 'sugar':0.05, 'eggs':0.2, 'japanese rice':0.3}, 'japanese', 2,'https://thewoksoflife.com/katsudon/')
poachedBeafandNoodles = GraphNode('Poached beef and noodles', {'soy sauce':0.05, 'sake':0.05, 'carrots':0.2, 'sugar':0.05, 'onion':0.05, 'beef':0.3, 'noodles':0.3}, 'japanese', 3,'https://www.bbcgoodfood.com/recipes/poached-beef-noodles-gyudon')
tonkatsuPork = GraphNode('Tonkatsu pork', {'pork':0.4, 'flour':0.1, 'eggs':0.2, 'olive oil':0.05, 'breadcrumb':0.1, 'ketchup':0.05, 'soy sauce':0.05, 'sugar':0.05}, 'japanese', 3,'https://www.justonecookbook.com/tonkatsu/')
ramen = GraphNode('Ramen', {'eggs':0.1, 'chicken':0.1, 'pork':0.1, 'carrots':0.1, 'ramen noodles':0.2, 'carrots':0.1, 'onion':0.1, 'chilli':0.05, 'ginger':0.05, 'mushrooms':0.1}, 'japanese', 3,'https://www.forkknifeswoon.com/simple-homemade-chicken-ramen/')


spicyChilly = GraphNode('Spicy chilly',{'garlic':0.2,'onion':0.2,'rice':0.3,'lime':0.1,'soy sauce':0.2}, 'thai', 1,'https://www.delicious.com.au/recipes/thai-spicy-chilli-basil-fried-rice/rd23hktd')
padThai = GraphNode('Pad thai',{'noodles':0.2,'chicken':0.2,'eggs':0.2,'garlic':0.1,'soy sauce':0.2,'peanuts':0.1}, 'thai', 1,'https://hot-thai-kitchen.com/best-pad-thai/')
beefFillet = GraphNode('Beef fillet',{'salt':0,'peanuts':0.1,'chilli':0.2,'garlic':0.1,'beef':0.3,'ginger':0.1,'soy sauce':0.2}, 'thai',2,'https://www.allrecipes.com/recipe/234642/thai-beef/')
thaiChickenMeatballs = GraphNode('Thai chicken meatballs',{'chicken':0.2,'chilli':0.2,'lime':0.1,'curry':0.2,'eggs':0.2,'peanuts':0.1}, 'thai',2,'https://www.taste.com.au/recipes/thai-chicken-meatballs/rz9bjozu')
thaiChickenRisotto = GraphNode('Thai chicken risotto', {'salt':0,'chicken':0.2,'rice':0.2,'onion':0.1,'curry':0.2,'lime':0.1,'green beans':0.2}, 'thai', 2,'https://www.taste.com.au/recipes/thai-chicken-risotto/82741d33-8f0e-4112-916b-2b9c8a5c001d')
beefSalad = GraphNode('Beed salad', {'salt':0,'beef':0.2,'noodles':0.2,'carrots':0.1,'zucchini':0.1,'lime':0.1,'garlic':0.1,'sugar':0.1,'olive oil':0.1}, 'thai', 2,'https://www.recipetineats.com/thai-beef-salad-2/')
coconutCrab = GraphNode('Coconut crab',{'coconut':0.3,'crab':0.3,'lime':0.1,'sugar':0.1,'chilli':0.2}, 'thai',3,'https://www.thespruceeats.com/thai-crab-curry-recipe-1300541')
srirachaSalmon = GraphNode('Sriracha salmon',{'soy sauce':0.1,'chilli':0.1,'sriracha':0.2,'salmon':0.3,'ginger':0.1,'peas':0.1,'butter':0.1},'thai', 3,'https://chefsavvy.com/honey-sriracha-salmon/')
curryNoodleSoup = GraphNode('Curry noodle soup', {'curry':0.2,'noodles':0.2,'potatoes':0.05,'onion':0.5,'coconut':0.1,'rice':0.1,'fish':0.15,'lime':0.05}, 'thai', 3,'https://www.littlebroken.com/thai-noodle-soup/')
suki = GraphNode('Suki', {'rice noodles':0.2 ,'onion':0.1 ,'celery':0.1 , 'carrots':0.1 ,'salt':0, 'garlic':0.1 ,'pork':0.2, 'eggs':0.1 ,'peppers':0.1}, 'thai', 3, 'https://www.bbcgoodfood.com/recipes/suki')


boiledEgg = GraphNode('Boiled eggs', {'eggs':1, 'salt':0, 'water':0}, 'general/not specified', 1,'https://thestayathomechef.com/how-to-boil-eggs/')
tomatoSoup = GraphNode('Tomato Soup', {'tomatoes':0.3,'salt':0,'butter':0.2,'onion':0.2, 'salt':0.1, 'peppers':0.1, 'parsley':0.1}, 'general/not specified',1,'https://www.inspiredtaste.net/27956/easy-tomato-soup-recipe/')
arepas = GraphNode('Arepas', {'salt':0, 'milk':0.4, 'corn flour':0.6}, 'general/not specified', 1,'https://minimalistbaker.com/how-to-make-arepas/')
galloPinto = GraphNode('Gallo pinto', {'onion':0.1, 'avocado':0.2, 'tomatoes':0.1, 'rice':0.3, 'peppers':0.1, 'black beans':0.3}, 'general/not specified', 2,'https://stripedspatula.com/gallo-pinto/')
salmonInParchment = GraphNode('Salmon in parchement', {'salmon':0.6, 'sour cream':0.1, 'olive oil':0.1, 'lemon':0.1, 'salt':0.1}, 'general/not specified', 2,'https://www.allrecipes.com/recipe/229032/parchment-baked-salmon/')
lentilCurry = GraphNode('Lentil curry', {'oil':0.05, 'onion':0.05, 'curry':0.2, 'lentil':0.4, 'rice':0.2, 'carrots':0.1}, 'general/not specified', 2,'https://www.recipetineats.com/lentil-curry-mega-flavour-lentil-recipe/')
quicheLorraine = GraphNode('Quiche Lorraine', {'dough':0.4, 'smoked steaky bacon':0.1, 'cheddar':0.2, 'eggs':0.2, 'sour cream':0.1}, 'general/not specified', 2,'https://www.bbcgoodfood.com/recipes/ultimate-quiche-lorraine')
donerKebab = GraphNode('Doner kebab', {'ground beef':0.4, 'yoghurt':0.1, 'milk':0.1, 'wrap':0.3, 'onion':0.05, 'garlic':0.05, 'salt':0}, 'general/not specified', 3,'https://www.bbcgoodfood.com/recipes/doner-kebab')
filetMignon = GraphNode('Filet Mignon', {'pork':0.5, 'vegetable broth':0.2, 'sour cream':0.1, 'mushrooms':0.1, 'olive oil':0.05, 'butter':0.05}, 'general/not specified', 3, 'https://www.delish.com/cooking/recipe-ideas/a23515113/how-to-cook-filet-mignon/')
fishandchips = GraphNode('Fish and chips', {'fish':0.5, 'salt':0, 'breadcrumb':0.1, 'flour':0.1, 'potatoes':0.3}, 'general/not specified', 3,'https://www.thespruceeats.com/best-fish-and-chips-recipe-434856')


#Connecting the nodes to create the graph:

#After this point, each cuisine is a graph itself, they're not connected yet to the startNode because the order in which they go into the
#startNode's adjacency list depends on the user's input of their prefered cuisines

# Italian cuisine:
pestoPasta.adjacencylist = [focaccia, parmesanMushroomsRisotto, shrimpMarinara]
focaccia.adjacencylist = [margheritaPizza, bellini]
parmesanMushroomsRisotto.adjacencylist = [spicyKaleLasagna, eggplantRolls, chickenParmesan]
shrimpMarinara.adjacencylist = [italianMeatballs]


# Mexican cuisine
chickenTacos.adjacencylist = [cheeseBlackBeansQuesadilla, chickenFlautas, cornSoup]
cheeseBlackBeansQuesadilla.adjacencylist = [guacamoleSalsa]
chickenFlautas.adjacencylist = [fishTacos, mexicanFiestaRice]
cornSoup.adjacencylist = [chilliConCarne, burrito, beefBirra]


# Spanish cuisine
patatasBravas.adjacencylist = [garlicMushroom, spanishTortilla, paella]
garlicMushroom.adjacencylist = []
spanishTortilla.adjacencylist = [spanishRice, chickpeaStew, squid, salmorejo, lentilSoup]
paella.adjacencylist = [churros]


# Japanese cuisine
sushi.adjacencylist = [cauliflowerTempura, californiaMaki, poachedBeafandNoodles]
cauliflowerTempura.adjacencylist = [yakitoriChicken]
californiaMaki.adjacencylist = [chickenTeriyaki, sushiBurrito, japaneseKatsudon]
poachedBeafandNoodles.adjacencylist = [tonkatsuPork, ramen]


# Thai cuisine
spicyChilly.adjacencylist = [padThai, beefFillet, coconutCrab]
padThai.adjacencylist = []
beefFillet.adjacencylist = [thaiChickenMeatballs, thaiChickenRisotto, beefSalad]
coconutCrab = [srirachaSalmon, curryNoodleSoup, suki]


# General
boiledEgg.adjacencylist = [tomatoSoup, galloPinto, donerKebab]
tomatoSoup.adjacencylist = [arepas]
galloPinto.adjacencylist = [salmonInParchment, lentilCurry, quicheLorraine]
donerKebab.adjacencylist = [filetMignon, fishandchips]


#Joining the whole graph together:

#After getting the user's list of cuisines through the GUI (in preference order, from favorite to least favorite), the list is saved in
#a variable called 'cuisines'
firstDegree = [pestoPasta, chickenTacos, patatasBravas, sushi, spicyChilly, boiledEgg] #List with the nodes that are in the first degree connections with the startNode

#Run the functions to compare the cuisines list (user input) and the cuisine of each of the first degree connection nodes, to define the order in
#which they will go in the adjacency list of the startNode, and then with this we will specify the adjacency list:
cuisines = []




availableIngredients = []


ingredient_selector_column = [
    [sg.Text("Select your ingredients:",auto_size_text=True, background_color = 'orange', font = 'bold')],
    [sg.Checkbox('Chicken', default = False, key = 'chicken', enable_events=True, text_color = 'white', background_color = 'orange')],
    [sg.Checkbox('Pasta', default = False, key = 'pasta', enable_events=True, text_color = 'white', background_color = 'orange')],
    [sg.Checkbox('Pesto', default = False,  key = 'pesto', enable_events=True, text_color = 'white', background_color = 'orange')],
    [sg.Checkbox('Cheese', default = False,  key = 'cheese', enable_events=True, text_color = 'white', background_color = 'orange')],
    [sg.Checkbox('Bread', default = False,  key = 'bread', enable_events=True, text_color = 'white', background_color = 'orange')],
    [sg.Checkbox('Flour', default = False,  key = 'flour', enable_events=True, text_color = 'white', background_color = 'orange')],
    [sg.Checkbox('Yeast', default = False,  key = 'yeast', enable_events=True, text_color = 'white', background_color = 'orange')],
    [sg.Checkbox('Olive Oil', default = False,  key = 'olive oil', enable_events=True, text_color = 'white', background_color = 'orange')],
    [sg.Checkbox('Tomato Sauce', default=False, key='tomato sauce', enable_events=True, text_color = 'white', background_color = 'orange')],
    [sg.Checkbox('Butter', default=False, key='butter', enable_events=True, text_color = 'white', background_color = 'orange')],
    [sg.Checkbox('Basil', default=False, key='basil', enable_events=True, text_color = 'white', background_color = 'orange')],
    [sg.Checkbox('Rice', default=False, key='rice', enable_events=True, text_color = 'white', background_color = 'orange')],
    [sg.Checkbox('Pizza Dough', default=False, key='pizza dough', enable_events=True, text_color = 'white', background_color = 'orange')],
    [sg.Checkbox('Milk', default=False, key='milk', enable_events=True, text_color = 'white', background_color = 'orange')],
    [sg.Checkbox('Eggs', default=False, key='eggs', enable_events=True, text_color = 'white', background_color = 'orange')],
    [sg.Checkbox('Parmesan', default=False, key='parmesan', enable_events=True, text_color = 'white', background_color = 'orange')],
    [sg.Checkbox('Mozzarella', default=False, key='mozzarella', enable_events=True, text_color = 'white', background_color = 'orange')],
    [sg.Checkbox('Peppers', default=False, key='peppers', enable_events=True, text_color = 'white', background_color = 'orange')],
    [sg.Checkbox('Shallot', default=False, key='shallot', enable_events=True, text_color = 'white', background_color = 'orange')],
    [sg.Checkbox('Mushrooms', default=False, key='mushrooms', enable_events=True, text_color = 'white', background_color = 'orange')],
    [sg.Checkbox('Tomatoes', default=False, key='tomatoes', enable_events=True, text_color = 'white', background_color = 'orange')],
    [sg.Checkbox('Lasagna Noodles', default=False, key='lasagna noodles', enable_events=True, text_color = 'white', background_color = 'orange')],
    [sg.Checkbox('Kale', default=False, key='kale', enable_events=True, text_color = 'white', background_color = 'orange')],
    [sg.Checkbox('Eggplants', default=False, key='eggplants', enable_events=True, text_color = 'white', background_color = 'orange')],
    [sg.Checkbox('Spinach', default=False, key='spinach', enable_events=True, text_color = 'white', background_color = 'orange')],
    [sg.Checkbox('Ricotta', default=False, key='ricotta', enable_events=True, text_color = 'white', background_color = 'orange')],
    [sg.Checkbox('Bread Crumbs', default=False, key='breadcrumb', enable_events=True, text_color = 'white', background_color = 'orange')],
    [sg.Checkbox('Parsley', default=False, key='parsley', enable_events=True, text_color = 'white', background_color = 'orange')],
    [sg.Checkbox('Garlic', default=False, key='garlic', enable_events=True, text_color = 'white', background_color = 'orange')],
    [sg.Checkbox('Marinara Sauce', default=False, key='marinara sauce', enable_events=True, text_color = 'white', background_color = 'orange')],
    [sg.Checkbox('Shrimp', default=False, key='shrimps', enable_events=True, text_color = 'white', background_color = 'orange')],
    [sg.Checkbox('Spaghetti', default=False, key='spaghetti', enable_events=True, text_color = 'white', background_color = 'orange')],
    [sg.Checkbox('Ground Beef', default=False, key='ground beef', enable_events=True, text_color = 'white', background_color = 'orange')],
    [sg.Checkbox('Italian Sausages', default=False, key='italian sausages', enable_events=True, text_color = 'white', background_color = 'orange')],
    [sg.Checkbox('Onion', default=False, key='onion', enable_events=True, text_color = 'white', background_color = 'orange')],
    [sg.Checkbox('Tortillas', default=False, key='tortillas', enable_events=True, text_color = 'white', background_color = 'orange')],
    [sg.Checkbox('Avocado', default=False, key='avocado', enable_events=True, text_color = 'white', background_color = 'orange')],
    [sg.Checkbox('Black Beans', default=False, key='black beans', enable_events=True, text_color = 'white', background_color = 'orange')],
    [sg.Checkbox('Lime', default=False, key='lime', enable_events=True, text_color = 'white', background_color = 'orange')],
    [sg.Checkbox('Fish', default=False, key='fish', enable_events=True, text_color = 'white', background_color = 'orange')],
    [sg.Checkbox('Corn', default=False, key='corn', enable_events=True, text_color = 'white', background_color = 'orange')],
    [sg.Checkbox('Beef', default=False, key='beef', enable_events=True, text_color = 'white', background_color = 'orange')],
    [sg.Checkbox('Kidney Beans', default=False, key='kidney bans', enable_events=True, text_color = 'white', background_color = 'orange')],
    [sg.Checkbox('Cumin', default=False, key='cumin', enable_events=True, text_color = 'white', background_color = 'orange')],
    [sg.Checkbox('Vinegar', default=False, key='vinegar', enable_events=True, text_color = 'white', background_color = 'orange')],
    [sg.Checkbox('Cilantro', default=False, key='cilantro', enable_events=True, text_color = 'white', background_color = 'orange')],
    [sg.Checkbox('Hot Sauce', default=False, key='hot sauce', enable_events=True, text_color = 'white', background_color = 'orange')],
    [sg.Checkbox('Lemon', default=False, key='lemon', enable_events=True, text_color = 'white', background_color = 'orange')],
    [sg.Checkbox('Mayo', default=False, key='mayonnaise', enable_events=True, text_color = 'white', background_color = 'orange')],
    [sg.Checkbox('Paprika', default=False, key='paprika', enable_events=True, text_color = 'white', background_color = 'orange')],
    [sg.Checkbox('Bell Pepper', default=False, key='bell pepper', enable_events=True, text_color = 'white', background_color = 'orange')],
    [sg.Checkbox('Chickpeas', default=False, key='chickpeas', enable_events=True, text_color = 'white', background_color = 'orange')],
    [sg.Checkbox('Chilli', default=False, key='chilli', enable_events=True, text_color = 'white', background_color = 'orange')],
    [sg.Checkbox('Squid', default=False, key='squid', enable_events=True, text_color = 'white', background_color = 'orange')],
    [sg.Checkbox('Lentils', default=False, key='lentil', enable_events=True, text_color = 'white', background_color = 'orange')],
    [sg.Checkbox('Potatoes', default=False, key='potatoes', enable_events=True, text_color = 'white', background_color = 'orange')],
    [sg.Checkbox('Pork', default=False, key='pork', enable_events=True, text_color = 'white', background_color = 'orange')],
    [sg.Checkbox('Lobster', default=False, key='lobster', enable_events=True, text_color = 'white', background_color = 'orange')],
    [sg.Checkbox('Green Beans', default=False, key='green beans', enable_events=True, text_color = 'white', background_color = 'orange')],
    [sg.Checkbox('Vanilla Extract', default=False, key='vanilla extract', enable_events=True, text_color = 'white', background_color = 'orange')],
    [sg.Checkbox('Chocolate', default=False, key='chocolate', enable_events=True, text_color = 'white', background_color = 'orange')],
    [sg.Checkbox('Baking Powder', default=False, key='baking powder', enable_events=True, text_color = 'white', background_color = 'orange')],
    [sg.Checkbox('Japanese Rice', default=False, key='japanese rice', enable_events=True, text_color = 'white', background_color = 'orange')],
    [sg.Checkbox('Salmon', default=False, key='salmon', enable_events=True, text_color = 'white', background_color = 'orange')],
    [sg.Checkbox('Seaweed', default=False, key='seaweed', enable_events=True, text_color = 'white', background_color = 'orange')],
    [sg.Checkbox('Cauliflower', default=False, key='cauliflower', enable_events=True, text_color = 'white', background_color = 'orange')],
    [sg.Checkbox('Skewers', default=False, key='skewers', enable_events=True, text_color = 'white', background_color = 'orange')],
    [sg.Checkbox('Soy Sauce', default=False, key='soy sauce', enable_events=True, text_color = 'white', background_color = 'orange')],
    [sg.Checkbox('Sake', default=False, key='sake', enable_events=True, text_color = 'white', background_color = 'orange')],
    [sg.Checkbox('Cucumber', default=False, key='cucumber', enable_events=True, text_color = 'white', background_color = 'orange')],
    [sg.Checkbox('Sugar', default=False, key='sugar', enable_events=True, text_color = 'white', background_color = 'orange')],
    [sg.Checkbox('Nori Sheets', default=False, key='nori sheets', enable_events=True, text_color = 'white', background_color = 'orange')],
    [sg.Checkbox('Ginger', default=False, key='ginger', enable_events=True, text_color = 'white', background_color = 'orange')],
    [sg.Checkbox('Tuna', default=False, key='tuna', enable_events=True, text_color = 'white', background_color = 'orange')],
    [sg.Checkbox('Carrots', default=False, key='carrots', enable_events=True, text_color = 'white', background_color = 'orange')],
    [sg.Checkbox('Breaded Pork Fillet', default=False, key='breaded pork fillet', enable_events=True, text_color = 'white', background_color = 'orange')],
    [sg.Checkbox('Noodles', default=False, key='noodles', enable_events=True, text_color = 'white', background_color = 'orange')],
    [sg.Checkbox('Ketchup', default=False, key='ketchup', enable_events=True, text_color = 'white', background_color = 'orange')],
    [sg.Checkbox('Ramen Noodles', default=False, key='ramen noodles', enable_events=True, text_color = 'white', background_color = 'orange')],
    [sg.Checkbox('Peanuts', default=False, key='peanuts', enable_events=True, text_color = 'white', background_color = 'orange')],
    [sg.Checkbox('Curry', default=False, key='curry', enable_events=True, text_color = 'white', background_color = 'orange')],
    [sg.Checkbox('Zucchini', default=False, key='zucchini', enable_events=True, text_color = 'white', background_color = 'orange')],
    [sg.Checkbox('Crab', default=False, key='crab', enable_events=True, text_color = 'white', background_color = 'orange')],
    [sg.Checkbox('Sriracha', default=False, key='sriracha', enable_events=True, text_color = 'white', background_color = 'orange')],
    [sg.Checkbox('Peas', default=False, key='peas', enable_events=True, text_color = 'white', background_color = 'orange')],
    [sg.Checkbox('Celery', default=False, key='celery', enable_events=True, text_color = 'white', background_color = 'orange')],
    [sg.Checkbox('Corn Flour', default=False, key='corn flour', enable_events=True, text_color = 'white', background_color = 'orange')],
    [sg.Checkbox('Sour Cream', default=False, key='sour cream', enable_events=True, text_color = 'white', background_color = 'orange')],
    [sg.Checkbox('Dough', default=False, key='dough', enable_events=True, text_color = 'white', background_color = 'orange')],
    [sg.Checkbox('Bacon', default=False, key='smoked steaky bacon', enable_events=True, text_color = 'white', background_color = 'orange')],
    [sg.Checkbox('Cheddar', default=False, key='cheddar', enable_events=True, text_color = 'white', background_color = 'orange')],
    [sg.Checkbox('Yoghurt', default=False, key='yoghurt', enable_events=True, text_color = 'white', background_color = 'orange')],
    [sg.Checkbox('Veggie Broth', default=False, key='vegetable broth', enable_events=True, text_color = 'white', background_color = 'orange')],
    [sg.Button('Find me easy recipes!', size = (20,1), button_color = 'orange on white', border_width = 3)]
]

cusine_selector = [
    [sg.Text('Choose your cuisines in your preffered order:', background_color = 'orange', font = 'bold')],
    [sg.Checkbox('Mexican', default=False, key='mexican', enable_events=True, text_color = 'white', background_color = 'orange')],
    [sg.Checkbox('Spanish', default=False, key='spanish', enable_events=True, text_color = 'white', background_color = 'orange')],
    [sg.Checkbox('Italian', default=False, key='italian', enable_events=True, text_color = 'white', background_color = 'orange')],
    [sg.Checkbox('Japanese', default=False, key='japanese', enable_events=True, text_color = 'white', background_color = 'orange')],
    [sg.Checkbox('Thai', default=False, key='thai', enable_events=True, text_color = 'white', background_color = 'orange')],
    [sg.Checkbox('General/Not Specified', default=False, key='general/not specified', enable_events=True, text_color = 'white', background_color = 'orange')],
]

layout = [
    [
        sg.Column(cusine_selector, background_color='orange'),
        sg.Column(ingredient_selector_column, size = (300,500),background_color='orange', scrollable = True,vertical_scroll_only = True)
    ]
]

# Create the window
window = sg.Window("INSTARECIPE", layout, background_color='orange')


while True:
    event, values = window.read()
    # Break code when window closes
    if event == sg.WINDOW_CLOSED:
        break

    # Chicken
    if event == 'chicken':
        if values['chicken'] == True:
            availableIngredients.append("chicken")
        elif values['chicken'] == False:
            if "chicken" in availableIngredients:
                availableIngredients.remove('chicken')

    if event == 'pasta':
        if values['pasta'] == True:
            availableIngredients.append("pasta")
        elif values['pasta'] == False:
            if "pasta" in availableIngredients:
                availableIngredients.remove('pasta')


    if event == 'pesto':
        if values['pesto'] == True:
            availableIngredients.append("pesto")
        elif values['pesto'] == False:
            if "pesto" in availableIngredients:
                availableIngredients.remove('pesto')


    if event == 'cheese':
        if values['cheese'] == True:
            availableIngredients.append("cheese")
        elif values['cheese'] == False:
            if "cheese" in availableIngredients:
                availableIngredients.remove('cheese')


    if event == 'bread':
        if values['bread'] == True:
            availableIngredients.append("bread")
        elif values['bread'] == False:
            if "bread" in availableIngredients:
                availableIngredients.remove('bread')

    if event == 'flour':
        if values['flour'] == True:
            availableIngredients.append("flour")
        elif values['flour'] == False:
            if "flour" in availableIngredients:
                availableIngredients.remove('flour')

    if event == 'yeast':
        if values['yeast'] == True:
            availableIngredients.append("yeast")
        elif values['yeast'] == False:
            if "yeast" in availableIngredients:
                availableIngredients.remove('yeast')

    if event == 'olive oil':
        if values['olive oil'] == True:
            availableIngredients.append("olive oil")
        elif values['olive oil'] == False:
            if "olive oil" in availableIngredients:
                availableIngredients.remove('olive oil')

    if event == 'tomato sauce':
        if values['tomato sauce'] == True:
            availableIngredients.append("tomato sauce")
        elif values['tomato sauce'] == False:
            if "tomato sauce" in availableIngredients:
                availableIngredients.remove('tomato sauce')


    if event == 'butter':
        if values['butter'] == True:
            availableIngredients.append("butter")
        elif values['butter'] == False:
            if "butter" in availableIngredients:
                availableIngredients.remove('butter')


    if event == 'basil':
        if values['basil'] == True:
            availableIngredients.append("basil")
        elif values['basil'] == False:
            if "basil" in availableIngredients:
                availableIngredients.remove('basil')

    if event == 'rice':
        if values['rice'] == True:
            availableIngredients.append("rice")
        elif values['rice'] == False:
            if "rice" in availableIngredients:
                availableIngredients.remove('rice')

    if event == 'pizza dough':
        if values['pizza dough'] == True:
            availableIngredients.append("pizza dough")
        elif values['pizza dough'] == False:
            if "pizza dough" in availableIngredients:
                availableIngredients.remove('pizza dough')

    if event == 'milk':
        if values['milk'] == True:
            availableIngredients.append("milk")
        elif values['milk'] == False:
            if "milk" in availableIngredients:
                availableIngredients.remove('milk')

    if event == 'eggs':
        if values['eggs'] == True:
            availableIngredients.append("eggs")
        elif values['eggs'] == False:
            if "eggs" in availableIngredients:
                availableIngredients.remove('eggs')

    if event == 'parmesan':
        if values['parmesan'] == True:
            availableIngredients.append("parmesan")
        elif values['parmesan'] == False:
            if "parmesan" in availableIngredients:
                availableIngredients.remove('parmesan')

    if event == 'mozzarella':
        if values['mozzarella'] == True:
            availableIngredients.append("mozzarella")
        elif values['mozzarella'] == False:
            if "mozzarella" in availableIngredients:
                availableIngredients.remove('mozzarella')

    if event == 'peppers':
        if values['peppers'] == True:
            availableIngredients.append("peppers")
        elif values['peppers'] == False:
            if "peppers" in availableIngredients:
                availableIngredients.remove('peppers')

    if event == 'shallot':
        if values['shallot'] == True:
            availableIngredients.append("shallot")
        elif values['shallot'] == False:
            if "shallot" in availableIngredients:
                availableIngredients.remove('shallot')

    if event == 'mushrooms':
        if values['mushrooms'] == True:
            availableIngredients.append("mushrooms")
        elif values['mushrooms'] == False:
            if "mushrooms" in availableIngredients:
                availableIngredients.remove('mushrooms')

    if event == 'tomatoes':
        if values['tomatoes'] == True:
            availableIngredients.append("tomatoes")
        elif values['tomatoes'] == False:
            if "tomatoes" in availableIngredients:
                availableIngredients.remove('tomatoes')

    if event == 'lasagna noodles':
        if values['lasagna noodles'] == True:
            availableIngredients.append("lasagna noodles")
        elif values['lasagna noodles'] == False:
            if "lasagna noodles" in availableIngredients:
                availableIngredients.remove('lasagna noodles')

    if event == 'kale':
        if values['kale'] == True:
            availableIngredients.append("kale")
        elif values['kale'] == False:
            if "kale" in availableIngredients:
                availableIngredients.remove('kale')

    if event == 'eggplants':
        if values['eggplants'] == True:
            availableIngredients.append("eggplants")
        elif values['eggplants'] == False:
            if "eggplants" in availableIngredients:
                availableIngredients.remove('eggplants')

    if event == 'spinach':
        if values['spinach'] == True:
            availableIngredients.append("spinach")
        elif values['spinach'] == False:
            if "spinach" in availableIngredients:
                availableIngredients.remove('spinach')

    if event == 'ricotta':
        if values['ricotta'] == True:
            availableIngredients.append("ricotta")
        elif values['ricotta'] == False:
            if "ricotta" in availableIngredients:
                availableIngredients.remove('ricotta')

    if event == 'breadcrumb':
        if values['breadcrumb'] == True:
            availableIngredients.append("breadcrumb")
        elif values['breadcrumb'] == False:
            if "breadcrumb" in availableIngredients:
                availableIngredients.remove('breadcrumb')

    if event == 'parsley':
        if values['parsley'] == True:
            availableIngredients.append("parsley")
        elif values['parsley'] == False:
            if "parsley" in availableIngredients:
                availableIngredients.remove('parsley')

    if event == 'garlic':
        if values['garlic'] == True:
            availableIngredients.append("garlic")
        elif values['garlic'] == False:
            if "garlic" in availableIngredients:
                availableIngredients.remove('garlic')

    if event == 'marinara sauce':
        if values['marinara sauce'] == True:
            availableIngredients.append("marinara sauce")
        elif values['marinara sauce'] == False:
            if "marinara sauce" in availableIngredients:
                availableIngredients.remove('marinara sauce')

    if event == 'shrimps':
        if values['shrimps'] == True:
            availableIngredients.append("shrimps")
        elif values['shrimps'] == False:
            if "shrimps" in availableIngredients:
                availableIngredients.remove('shrimps')

    if event == 'spaghetti':
        if values['spaghetti'] == True:
            availableIngredients.append("spaghetti")
        elif values['spaghetti'] == False:
            if "spaghetti" in availableIngredients:
                availableIngredients.remove('spaghetti')

    if event == 'ground beef':
        if values['ground beef'] == True:
            availableIngredients.append("ground beef")
        elif values['ground beef'] == False:
            if "ground beef" in availableIngredients:
                availableIngredients.remove('ground beef')

    if event == 'italian sausages':
        if values['italian sausages'] == True:
            availableIngredients.append("italian sausages")
        elif values['italian sausages'] == False:
            if "italian sausages" in availableIngredients:
                availableIngredients.remove('italian sausages')

    if event == 'onion':
        if values['onion'] == True:
            availableIngredients.append("onion")
        elif values['onion'] == False:
            if "onion" in availableIngredients:
                availableIngredients.remove('onion')

    if event == 'tortillas':
        if values['tortillas'] == True:
            availableIngredients.append("tortillas")
        elif values['tortillas'] == False:
            if "tortillas" in availableIngredients:
                availableIngredients.remove('tortillas')

    if event == 'avocado':
        if values['avocado'] == True:
            availableIngredients.append("avocado")
        elif values['avocado'] == False:
            if "avocado" in availableIngredients:
                availableIngredients.remove('avocado')

    if event == 'black beans':
        if values['black beans'] == True:
            availableIngredients.append("black beans")
        elif values['black beans'] == False:
            if "black beans" in availableIngredients:
                availableIngredients.remove('black beans')

    if event == 'lime':
        if values['lime'] == True:
            availableIngredients.append("lime")
        elif values['lime'] == False:
            if "lime" in availableIngredients:
                availableIngredients.remove('lime')

    if event == 'fish':
        if values['fish'] == True:
            availableIngredients.append("fish")
        elif values['fish'] == False:
            if "fish" in availableIngredients:
                availableIngredients.remove('fish')

    if event == 'corn':
        if values['corn'] == True:
            availableIngredients.append("corn")
        elif values['corn'] == False:
            if "corn" in availableIngredients:
                availableIngredients.remove('corn')

    if event == 'beef':
        if values['beef'] == True:
            availableIngredients.append("beef")
        elif values['beef'] == False:
            if "beef" in availableIngredients:
                availableIngredients.remove('beef')

    if event == 'kidney bans':
        if values['kidney bans'] == True:
            availableIngredients.append("kidney bans")
        elif values['kidney bans'] == False:
            if "kidney bans" in availableIngredients:
                availableIngredients.remove('kidney bans')

    if event == 'cumin':
        if values['cumin'] == True:
            availableIngredients.append("cumin")
        elif values['cumin'] == False:
            if "cumin" in availableIngredients:
                availableIngredients.remove('cumin')

    if event == 'vinegar':
        if values['vinegar'] == True:
            availableIngredients.append("vinegar")
        elif values['vinegar'] == False:
            if "vinegar" in availableIngredients:
                availableIngredients.remove('vinegar')

    if event == 'cilantro':
        if values['cilantro'] == True:
            availableIngredients.append("cilantro")
        elif values['cilantro'] == False:
            if "cilantro" in availableIngredients:
                availableIngredients.remove('cilantro')

    if event == 'hot sauce':
        if values['hot sauce'] == True:
            availableIngredients.append("hot sauce")
        elif values['hot sauce'] == False:
            if "hot sauce" in availableIngredients:
                availableIngredients.remove('hot sauce')

    if event == 'lemon':
        if values['lemon'] == True:
            availableIngredients.append("lemon")
        elif values['lemon'] == False:
            if "lemon" in availableIngredients:
                availableIngredients.remove('lemon')

    if event == 'mayonnaise':
        if values['mayonnaise'] == True:
            availableIngredients.append("mayonnaise")
        elif values['mayonnaise'] == False:
            if "mayonnaise" in availableIngredients:
                availableIngredients.remove('mayonnaise')

    if event == 'paprika':
        if values['paprika'] == True:
            availableIngredients.append("paprika")
        elif values['paprika'] == False:
            if "paprika" in availableIngredients:
                availableIngredients.remove('paprika')

    if event == 'bell pepper':
        if values['bell pepper'] == True:
            availableIngredients.append("bell pepper")
        elif values['bell pepper'] == False:
            if "bell pepper" in availableIngredients:
                availableIngredients.remove('bell pepper')

    if event == 'chickpeas':
        if values['chickpeas'] == True:
            availableIngredients.append("chickpeas")
        elif values['chickpeas'] == False:
            if "chickpeas" in availableIngredients:
                availableIngredients.remove('chickpeas')

    if event == 'chilli':
        if values['chilli'] == True:
            availableIngredients.append("chilli")
        elif values['chilli'] == False:
            if "chilli" in availableIngredients:
                availableIngredients.remove('chilli')

    if event == 'squid':
        if values['squid'] == True:
            availableIngredients.append("squid")
        elif values['squid'] == False:
            if "squid" in availableIngredients:
                availableIngredients.remove('squid')

    if event == 'lentil':
        if values['lentil'] == True:
            availableIngredients.append("lentil")
        elif values['lentil'] == False:
            if "lentil" in availableIngredients:
                availableIngredients.remove('lentil')

    if event == 'potatoes':
        if values['potatoes'] == True:
            availableIngredients.append("potatoes")
        elif values['potatoes'] == False:
            if "potatoes" in availableIngredients:
                availableIngredients.remove('potatoes')

    if event == 'pork':
        if values['pork'] == True:
            availableIngredients.append("pork")
        elif values['pork'] == False:
            if "pork" in availableIngredients:
                availableIngredients.remove('pork')

    if event == 'lobster':
        if values['lobster'] == True:
            availableIngredients.append("lobster")
        elif values['lobster'] == False:
            if "lobster" in availableIngredients:
                availableIngredients.remove('lobster')

    if event == 'green beans':
        if values['green beans'] == True:
            availableIngredients.append("green beans")
        elif values['green beans'] == False:
            if "green beans" in availableIngredients:
                availableIngredients.remove('green beans')

    if event == 'vanilla extract':
        if values['vanilla extract'] == True:
            availableIngredients.append("vanilla extract")
        elif values['vanilla extract'] == False:
            if "vanilla extract" in availableIngredients:
                availableIngredients.remove('vanilla extract')

    if event == 'chocolate':
        if values['chocolate'] == True:
            availableIngredients.append("chocolate")
        elif values['chocolate'] == False:
            if "chocolate" in availableIngredients:
                availableIngredients.remove('chocolate')

    if event == 'baking powder':
        if values['baking powder'] == True:
            availableIngredients.append("baking powder")
        elif values['baking powder'] == False:
            if "baking powder" in availableIngredients:
                availableIngredients.remove('baking powder')

    if event == 'japanese rice':
        if values['japanese rice'] == True:
            availableIngredients.append("japanese rice")
        elif values['japanese rice'] == False:
            if "japanese rice" in availableIngredients:
                availableIngredients.remove('japanese rice')

    if event == 'salmon':
        if values['salmon'] == True:
            availableIngredients.append("salmon")
        elif values['salmon'] == False:
            if "salmon" in availableIngredients:
                availableIngredients.remove('salmon')

    if event == 'seaweed':
        if values['seaweed'] == True:
            availableIngredients.append("seaweed")
        elif values['seaweed'] == False:
            if "seaweed" in availableIngredients:
                availableIngredients.remove('seaweed')

    if event == 'cauliflower':
        if values['cauliflower'] == True:
            availableIngredients.append("cauliflower")
        elif values['cauliflower'] == False:
            if "cauliflower" in availableIngredients:
                availableIngredients.remove('cauliflower')

    if event == 'skewers':
        if values['skewers'] == True:
            availableIngredients.append("skewers")
        elif values['skewers'] == False:
            if "skewers" in availableIngredients:
                availableIngredients.remove('skewers')

    if event == 'soy sauce':
        if values['soy sauce'] == True:
            availableIngredients.append("soy sauce")
        elif values['soy sauce'] == False:
            if "soy sauce" in availableIngredients:
                availableIngredients.remove('soy sauce')

    if event == 'sake':
        if values['sake'] == True:
            availableIngredients.append("sake")
        elif values['sake'] == False:
            if "sake" in availableIngredients:
                availableIngredients.remove('sake')

    if event == 'cucumber':
        if values['cucumber'] == True:
            availableIngredients.append("cucumber")
        elif values['cucumber'] == False:
            if "cucumber" in availableIngredients:
                availableIngredients.remove('cucumber')

    if event == 'sugar':
        if values['sugar'] == True:
            availableIngredients.append("sugar")
        elif values['sugar'] == False:
            if "sugar" in availableIngredients:
                availableIngredients.remove('sugar')

    if event == 'nori sheets':
        if values['nori sheets'] == True:
            availableIngredients.append("nori sheets")
        elif values['nori sheets'] == False:
            if "nori sheets" in availableIngredients:
                availableIngredients.remove('nori sheets')

    if event == 'ginger':
        if values['ginger'] == True:
            availableIngredients.append("ginger")
        elif values['ginger'] == False:
            if "ginger" in availableIngredients:
                availableIngredients.remove('ginger')

    if event == 'tuna':
        if values['tuna'] == True:
            availableIngredients.append("tuna")
        elif values['tuna'] == False:
            if "tuna" in availableIngredients:
                availableIngredients.remove('tuna')

    if event == 'carrots':
        if values['carrots'] == True:
            availableIngredients.append("carrots")
        elif values['carrots'] == False:
            if "carrots" in availableIngredients:
                availableIngredients.remove('carrots')

    if event == 'breaded pork':
        if values['breaded pork'] == True:
            availableIngredients.append("breaded pork")
        elif values['breaded pork'] == False:
            if "breaded pork" in availableIngredients:
                availableIngredients.remove('breaded pork')

    if event == 'noodles':
        if values['noodles'] == True:
            availableIngredients.append("noodles")
        elif values['noodles'] == False:
            if "noodles" in availableIngredients:
                availableIngredients.remove('noodles')

    if event == 'ketchup':
        if values['ketchup'] == True:
            availableIngredients.append("ketchup")
        elif values['ketchup'] == False:
            if "ketchup" in availableIngredients:
                availableIngredients.remove('ketchup')

    if event == 'ramen noodles':
        if values['ramen noodles'] == True:
            availableIngredients.append("ramen noodles")
        elif values['ramen noodles'] == False:
            if "ramen noodles" in availableIngredients:
                availableIngredients.remove('ramen noodles')

    if event == 'peanuts':
        if values['peanuts'] == True:
            availableIngredients.append("peanuts")
        elif values['peanuts'] == False:
            if "peanuts" in availableIngredients:
                availableIngredients.remove('peanuts')

    if event == 'curry':
        if values['curry'] == True:
            availableIngredients.append("curry")
        elif values['curry'] == False:
            if "curry" in availableIngredients:
                availableIngredients.remove('curry')

    if event == 'zucchini':
        if values['zucchini'] == True:
            availableIngredients.append("zucchini")
        elif values['zucchini'] == False:
            if "zucchini" in availableIngredients:
                availableIngredients.remove('zucchini')

    if event == 'crab':
        if values['crab'] == True:
            availableIngredients.append("crab")
        elif values['crab'] == False:
            if "crab" in availableIngredients:
                availableIngredients.remove('crab')

    if event == 'sriracha':
        if values['sriracha'] == True:
            availableIngredients.append("sriracha")
        elif values['sriracha'] == False:
            if "sriracha" in availableIngredients:
                availableIngredients.remove('sriracha')

    if event == 'peas':
        if values['peas'] == True:
            availableIngredients.append("peas")
        elif values['peas'] == False:
            if "peas" in availableIngredients:
                availableIngredients.remove('peas')

    if event == 'celery':
        if values['celery'] == True:
            availableIngredients.append("celery")
        elif values['celery'] == False:
            if "celery" in availableIngredients:
                availableIngredients.remove('celery')

    if event == 'corn flour':
        if values['corn flour'] == True:
            availableIngredients.append("corn flour")
        elif values['corn flour'] == False:
            if "corn flour" in availableIngredients:
                availableIngredients.remove('corn flour')

    if event == 'sour cream':
        if values['sour cream'] == True:
            availableIngredients.append("sour cream")
        elif values['sour cream'] == False:
            if "sour cream" in availableIngredients:
                availableIngredients.remove('sour cream')

    if event == 'dough':
        if values['dough'] == True:
            availableIngredients.append("dough")
        elif values['dough'] == False:
            if "dough" in availableIngredients:
                availableIngredients.remove('dough')

    if event == 'smoked steaky bacon':
        if values['smoked steaky bacon'] == True:
            availableIngredients.append("smoked steaky bacon")
        elif values['smoked steaky bacon'] == False:
            if "smoked steaky bacon" in availableIngredients:
                availableIngredients.remove('smoked steaky bacon')

    if event == 'cheddar':
        if values['cheddar'] == True:
            availableIngredients.append("cheddar")
        elif values['cheddar'] == False:
            if "cheddar" in availableIngredients:
                availableIngredients.remove('cheddar')

    if event == 'yoghurt':
        if values['yoghurt'] == True:
            availableIngredients.append("yoghurt")
        elif values['yoghurt'] == False:
            if "yoghurt" in availableIngredients:
                availableIngredients.remove('yoghurt')

    if event == 'vegetable broth':
        if values['vegetable broth'] == True:
            availableIngredients.append("vegetable broth")
        elif values['vegetable broth'] == False:
            if "vegetable broth" in availableIngredients:
                availableIngredients.remove('vegetable broth')

    if event == 'mexican':
        if values['mexican'] == True:
            cuisines.append("mexican")
        elif values['mexican'] == False:
            if "mexican" in cuisines:
                cuisines.remove('mexican')

    if event == 'spanish':
        if values['spanish'] == True:
            cuisines.append("spanish")
        elif values['spanish'] == False:
            if "spanish" in cuisines:
                cuisines.remove('spanish')

    if event == 'italian':
        if values['italian'] == True:
            cuisines.append("italian")
        elif values['italian'] == False:
            if "italian" in cuisines:
                cuisines.remove('italian')

    if event == 'japanese':
        if values['japanese'] == True:
            cuisines.append("japanese")
        elif values['japanese'] == False:
            if "japanese" in cuisines:
                cuisines.remove('japanese')

    if event == 'thai':
        if values['thai'] == True:
            cuisines.append("thai")
        elif values['thai'] == False:
            if "thai" in cuisines:
                cuisines.remove('thai')

    if event == 'general/not specified':
        if values['general/not specified'] == True:
            cuisines.append("general/not specified")
        elif values['general/not specified'] == False:
            if "general/not specified" in cuisines:
                cuisines.remove('general/not specified')

    if event == 'Find me easy recipes!':
        x = finalAdjList(cuisines, firstDegree)
        startNode.adjacencylist = x
        startNode.dfs()
        break







