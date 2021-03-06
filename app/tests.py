#!/usr/bin/env python3

# -------
# imports
# -------

from config import app
from unittest import main, \
                     TestCase
from models import Cocktail, \
                   Ingredient, \
                   Amount
import requests
import idb
import json

#HOST = 'http://104.130.22.54'
HOST = 'http://localhost:5000'

# -----------
# TestIDB
#  Total of 125 tests written
# -----------

class TestIdb(TestCase):
    """Unit tests for methods in models.py and idb.py"""

    # ----------
    # cocktail__init__
    # ----------

    def test_cocktail_init_1(self):
        """Test __init__ method for the class Cocktail"""
        name = "Vodka Sprite"
        glass = "Glass"
        recipe = "Vodka Sprite Recipe"
        cocktail = Cocktail(name, glass, recipe)
        self.assertEqual(name, cocktail.name)
        self.assertEqual(glass, cocktail.glass)
        self.assertEqual(recipe, cocktail.recipe)
        self.assertEqual(None, cocktail.image)

    def test_cocktail_init_2(self):
        """Test __init__ method for the class Cocktail"""
        cocktail = Cocktail(None, None, None)
        self.assertEqual(None, cocktail.name)
        self.assertEqual(None, cocktail.glass)
        self.assertEqual(None, cocktail.recipe)
        self.assertEqual(None, cocktail.image)

    def test_cocktail_init_3(self):
        """Test __init__ method for the class Cocktail"""
        name = ""
        glass = ""
        recipe = ""
        cocktail = Cocktail(name, glass, recipe)
        self.assertEqual(name, cocktail.name)
        self.assertEqual(glass, cocktail.glass)
        self.assertEqual(recipe, cocktail.recipe)
        self.assertEqual(None, cocktail.image)

    def test_cocktail_init_4(self):
        """Test __init__ method for the class Cocktail"""
        name = "Aqua"
        glass = "Bottle"
        recipe = "Aqua Recipe"
        image = "static/images/cocktails/Aqua.jpg"
        cocktail = Cocktail(name, glass, recipe, image)
        self.assertEqual(name, cocktail.name)
        self.assertEqual(glass, cocktail.glass)
        self.assertEqual(recipe, cocktail.recipe)
        self.assertEqual(image, cocktail.image)

    def test_cocktail_init_5(self):
        """Test __init__ method for the class Cocktail"""
        name = "Aqua"
        glass = "Bottle"
        recipe = "Aqua Recipe"
        image = "static/images/cocktails/Aqua.jpg"
        cocktail = Cocktail(name, glass, recipe, image)
        self.assertEqual(name, cocktail.name)
        self.assertEqual(glass, cocktail.glass)
        self.assertEqual(recipe, cocktail.recipe)
        self.assertIsNotNone(cocktail.image)

    def test_cocktail_init_6(self):
        """Test __init__ method for the class Cocktail"""
        name = None
        glass = None
        recipe = None
        image = "static/images/cocktails/Aqua.jpg"
        cocktail = Cocktail(name, glass, recipe, image)
        self.assertIsNone(cocktail.name)
        self.assertIsNone(cocktail.glass)
        self.assertIsNone(cocktail.recipe)
        self.assertIsNotNone(cocktail.image)

    def test_cocktail_init_7(self):
        """Test __init__ method for the class Cocktail"""
        name = "None"
        glass = "None"
        recipe = "None"
        cocktail = Cocktail(name, glass, recipe)
        self.assertEqual(name, cocktail.name)
        self.assertEqual(glass, cocktail.glass)
        self.assertEqual(recipe, cocktail.recipe)
        self.assertEqual(None, cocktail.image)

    # ----------
    # cocktail__repr__
    # ----------

    def test_cocktail_repr_1(self):
        """Test __repr__ method for the class Cocktail"""
        cocktail = Cocktail("Vodka Sprite", "Glass", "Vodka Sprite Recipe")
        drink = cocktail.__repr__()
        self.assertEqual("<Cocktail '%s'>" % cocktail.name, drink)

    def test_cocktail_repr_2(self):
        """Test __repr__ method for the class Cocktail"""
        cocktail = Cocktail(None, None, None, None)
        drink = cocktail.__repr__()
        self.assertEqual("<Cocktail None>", drink)

    def test_cocktail_repr_3(self):
        """Test __repr__ method for the class Cocktail"""
        cocktail = Cocktail("", "", "")
        drink = cocktail.__repr__()
        self.assertEqual("<Cocktail ''>", drink)

    def test_cocktail_repr_4(self):
        """Test __repr__ method for the class Cocktail"""
        cocktail = Cocktail("Aqua", "Bottle", "Aqua Recipe", "static/images/cocktails/Aqua.jpg")
        drink = cocktail.__repr__()
        self.assertEqual("<Cocktail '%s'>" % cocktail.name, drink)

    # ----------
    # ingredient__init__
    # ----------

    def test_ingredient_init_1(self):
        """Test __init__ method for the class Ingredient"""
        name = "Rum"
        ingredient = Ingredient(name)
        self.assertEqual(name, ingredient.name)
        self.assertEqual(None, ingredient.image)

    def test_ingredient_init_2(self):
        """Test __init__ method for the class Ingredient"""
        name = None
        ingredient = Ingredient(name)
        self.assertEqual(name, ingredient.name)
        self.assertEqual(None, ingredient.image)

    def test_ingredient_init_3(self):
        """Test __init__ method for the class Ingredient"""
        name = ""
        ingredient = Ingredient(name)
        self.assertEqual(name, ingredient.name)
        self.assertEqual(None, ingredient.image)

    def test_ingredient_init_4(self):
        """Test __init__ method for the class Ingredient"""
        name = "Berries"
        image = "static/images/ingredients/Berries.jpg"
        ingredient = Ingredient(name, image)
        self.assertEqual(name, ingredient.name)
        self.assertEqual(image, ingredient.image)

    def test_ingredient_init_5(self):
        """Test __init__ method for the class Ingredient"""
        name = "Berries"
        image = "static/images/ingredients/Berries.jpg"
        ingredient = Ingredient(name, image)
        self.assertEqual(name, ingredient.name)
        self.assertIsNotNone(ingredient.image)

    def test_ingredient_init_6(self):
        """Test __init__ method for the class Ingredient"""
        name = None
        image = "static/images/ingredients/Aqua.jpg"
        ingredient = Ingredient(name, image)
        self.assertIsNone(ingredient.name)
        self.assertIsNotNone(ingredient.image)

    def test_ingredient_init_7(self):
        """Test __init__ method for the class Ingredient"""
        name = "None"
        ingredient = Ingredient(name)
        self.assertEqual(name, ingredient.name)
        self.assertEqual(None, ingredient.image)

    # ----------
    # ingredient__repr__
    # ----------

    def test_ingredient_repr_1(self):
        """Test __repr__ method for the class Ingredient"""
        name = "Rum"
        ingredient = Ingredient(name)
        ingredient_name = ingredient.__repr__()
        self.assertEqual("<Ingredient '%s'>" % ingredient.name, ingredient_name)

    def test_ingredient_repr_2(self):
        """Test __repr__ method for the class Ingredient"""
        name = None
        ingredient = Ingredient(name)
        ingredient_name = ingredient.__repr__()
        self.assertEqual("<Ingredient None>", ingredient_name)

    def test_ingredient_repr_3(self):
        """Test __repr__ method for the class Ingredient"""
        name = ""
        ingredient = Ingredient(name)
        ingredient_name = ingredient.__repr__()
        self.assertEqual("<Ingredient ''>", ingredient_name)

    def test_ingredient_repr_4(self):
        """Test __repr__ method for the class Ingredient"""
        name = "Berries"
        image = "static/images/ingredients/Berries.jpg"
        ingredient = Ingredient(name, image)
        ingredient_name = ingredient.__repr__()
        self.assertEqual("<Ingredient '%s'>" % ingredient.name, ingredient_name)

# ----------
# amount__init__
# ----------

    def test_amount_init_1(self):
        """Test __init__ method for the class Amount"""
        cocktail = Cocktail("Moscow Mule", "Cup", "Moscow Mule Recipe")
        ingredient = Ingredient("Rum")
        amount = "2 oz."
        value = Amount(cocktail, ingredient, amount)
        self.assertEqual(cocktail, value.c_data)
        self.assertEqual(ingredient, value.i_data)
        self.assertEqual(amount, value.amount)

    def test_amount_init_2(self):
        """Test __init__ method for the class Amount"""
        cocktail = Cocktail(None, None, None, None)
        ingredient = Ingredient(None, None)
        amount = "1"
        value = Amount(cocktail, ingredient, amount)
        self.assertEqual(cocktail, value.c_data)
        self.assertEqual(ingredient, value.i_data)
        self.assertEqual(amount, value.amount)

    def test_amount_init_3(self):
        """Test __init__ method for the class Amount"""
        cocktail = Cocktail("", "", "")
        ingredient = Ingredient("")
        amount = "3 oz."
        value = Amount(cocktail, ingredient, amount)
        self.assertEqual(cocktail, value.c_data)
        self.assertEqual(ingredient, value.i_data)
        self.assertEqual(amount, value.amount)

    def test_amount_init_4(self):
        """Test __init__ method for the class Amount"""
        cocktail = Cocktail("Aqua", "Bottle", "Aqua Recipe", "static/images/cocktails/Aqua.jpg")
        ingredient = Ingredient("Berries", "static/images/ingredients/Berries.jpg")
        amount = "3 oz."
        value = Amount(cocktail, ingredient, amount)
        self.assertEqual(cocktail, value.c_data)
        self.assertEqual(ingredient, value.i_data)
        self.assertEqual(amount, value.amount)

    def test_amount_init_5(self):
        """Test __init__ method for the class Amount"""
        cocktail = Cocktail("Aqua", "Bottle", "Aqua Recipe", "static/images/cocktails/Aqua.jpg")
        ingredient = Ingredient("Berries", "static/images/ingredients/Berries.jpg")
        amount = "3 oz."
        value = Amount(cocktail, ingredient, amount)
        self.assertIsNotNone(cocktail, value.c_data)
        self.assertIsNotNone(ingredient, value.i_data)
        self.assertIsNotNone(amount, value.amount)

    def test_amount_init_6(self):
        """Test __init__ method for the class Amount"""
        cocktail = Cocktail(None, None, None, "static/images/cocktails/Aqua.jpg")
        ingredient = Ingredient(None, "static/images/ingredients/Berries.jpg")
        amount = "3 oz."
        value = Amount(cocktail, ingredient, amount)
        self.assertIsNotNone(value.c_data)
        self.assertIsNotNone(value.i_data)
        self.assertIsNotNone(value.amount)

    def test_amount_init_7(self):
        """Test __init__ method for the class Amount"""
        cocktail = Cocktail(None, None, None, None)
        ingredient = Ingredient(None, "static/images/ingredients/Berries.jpg")
        amount = "3 oz."
        value = Amount(cocktail, ingredient, amount)
        self.assertIsNotNone(value.c_data)
        self.assertIsNotNone(value.i_data)
        self.assertIsNotNone(value.amount)

    def test_amount_init_8(self):
        """Test __init__ method for the class Amount"""
        cocktail = Cocktail(None, None, None, "static/images/cocktails/Aqua.jpg")
        ingredient = Ingredient(None, None)
        amount = "3 oz."
        value = Amount(cocktail, ingredient, amount)
        self.assertIsNotNone(value.c_data)
        self.assertIsNotNone(value.i_data)
        self.assertIsNotNone(value.amount)

    # ----------
    # amount__repr__
    # ----------

    def test_amount_repr_1(self):
        """Test __repr__ method for the class Amount"""
        cocktail = Cocktail("Moscow Mule", "Cup", "Moscow Mule Recipe")
        ingredient = Ingredient("Rum")
        amount = Amount(cocktail, ingredient, "2 oz.")
        amount_name = amount.__repr__()
        self.assertEqual(
            "<Amount [%r-|---|-%r]>" % (amount.c_data, amount.i_data),
            amount_name
        )

    def test_amount_repr_2(self):
        """Test __repr__ method for the class Amount"""
        cocktail = Cocktail(None, None, None, None)
        ingredient = Ingredient(None, None)
        amount = Amount(cocktail, ingredient, "1")
        amount_name = amount.__repr__()
        self.assertEqual(
            "<Amount [%r-|---|-%r]>" % (amount.c_data, amount.i_data),
            amount_name
        )

    def test_amount_repr_3(self):
        """Test __repr__ method for the class Amount"""
        cocktail = Cocktail("", "", "")
        ingredient = Ingredient("")
        amount = Amount(cocktail, ingredient, "3 oz.")
        amount_name = amount.__repr__()
        self.assertEqual(
            "<Amount [%r-|---|-%r]>" % (amount.c_data, amount.i_data),
            amount_name
        )

    def test_amount_repr_4(self):
        """Test __repr__ method for the class Amount"""
        cocktail = Cocktail("Aqua", "Bottle", "Aqua Recipe", "static/images/cocktails/Aqua.jpg")
        ingredient = Ingredient("Berries", "static/images/ingredients/Berries.jpg")
        amount = Amount(cocktail, ingredient, "3 oz.")
        amount_name = amount.__repr__()
        self.assertEqual(
            "<Amount [%r-|---|-%r]>" % (amount.c_data, amount.i_data),
            amount_name
        )

    # ---
    # API
    # ---

    # ---
    # api_cocktail_list
    # ---

    def test_api_cocktail_list_1(self):
        result = json.loads(idb.api_cocktail_list())
        self.assertEqual(result[0], {'name': "'57 Chevy with a White License Plate",
            'id': 1})

    def test_api_cocktail_list_2(self):
        result = json.loads(idb.api_cocktail_list())
        self.assertEqual(result[1], {'name': '155 Belmont', 'id': 2})

    def test_api_cocktail_list_3(self):
        result = json.loads(idb.api_cocktail_list())
        self.assertIsNotNone(result[1])

    # ---
    # api_cocktail_list_route
    # ---

    def test_api_cocktail_list_route_1(self):
        result = json.loads(app.test_client().get('/api/cocktail').data.decode())
        self.assertEqual(result[57], {'id': 58, 'name': 'Bullshot'})

    def test_api_cocktail_list_route_2(self):
        result = json.loads(app.test_client().get('/api/cocktail').data.decode())
        self.assertEqual(result[100]['id'], 101)

    def test_api_cocktail_list_route_3(self):
        result = json.loads(app.test_client().get('/api/cocktail').data.decode())
        self.assertEqual(result[2]['name'], '9 1/2 Weeks')

    # ---
    # api_cocktail
    # ---

    def test_api_cocktail_1(self):
        result = json.loads(idb.api_cocktail(1))
        self.assertEqual(result[0]['ingredients'][0]['quantity'], '1 oz white ')

    def test_api_cocktail_2(self):
        result = json.loads(idb.api_cocktail(2))
        self.assertEqual(result[0]['ingredients'][2]['name'], 'Vodka')

    def test_api_cocktail_3(self):
        result = json.loads(idb.api_cocktail(55))
        self.assertEqual(result[0]['name'], 'Brandy Alexandra')

    # ---
    # api_cocktail_route
    # ---

    def test_api_cocktail_route_1(self):
        result = json.loads(app.test_client().get('/api/cocktail/189').data.decode())
        self.assertEqual(result[0]['ingredients'][1], {"name": "Cognac", "id":
            123, "quantity": "2 oz "})

    def test_api_cocktail_route_2(self):
        result = json.loads(app.test_client().get('/api/cocktail/39').data.decode())
        self.assertEqual(result[0]['name'], 'Black and White')

    def test_api_cocktail_route_3(self):
        result = json.loads(app.test_client().get('/api/cocktail/3').data.decode())
        self.assertEqual(result[0]['ingredients'][2]['name'], 'Strawberry liqueur')

    # ---
    # api_cocktail_name
    # ---

    def test_api_cocktail_name_1(self):
        result = json.loads(idb.api_cocktail_name(1))
        self.assertEqual(result['name'], "'57 Chevy with a White License Plate")

    def test_api_cocktail_name_2(self):
        result = json.loads(idb.api_cocktail_name(2))
        self.assertEqual(result['name'], '155 Belmont')

    def test_api_cocktail_name_3(self):
        result = json.loads(idb.api_cocktail_name(3))
        self.assertEqual(result['name'], '9 1/2 Weeks')

    # ---
    # api_cocktail_name_route
    # ---

    def test_api_cocktail_name_route_1(self):
        result = json.loads(app.test_client().get('/api/cocktail/88/name').data.decode())
        self.assertEqual(result['name'], 'Cool Kid')

    def test_api_cocktail_name_route_2(self):
        result = json.loads(app.test_client().get('/api/cocktail/5/name').data.decode())
        self.assertEqual(result['name'], 'A True Amaretto Sour')

    def test_api_cocktail_name_route_3(self):
        result = json.loads(app.test_client().get('/api/cocktail/200/name').data.decode())
        self.assertEqual(result['name'], 'Jihad')

    # ---
    # api_cocktail_ingredients
    # ---

    def test_api_cocktail_ingredients_1(self):
        result = json.loads(idb.api_cocktail_ingredients(1))
        self.assertEqual(result[0], {'quantity': '1 oz white ', 'name':
            'Creme de Cacao', 'id': 1})

    def test_api_cocktail_ingredients_2(self):
        result = json.loads(idb.api_cocktail_ingredients(1))
        self.assertEqual(result[1], {'quantity': '1 oz ', 'name': 'Vodka', 'id': 2})

    def test_api_cocktail_ingredients_3(self):
        result = json.loads(idb.api_cocktail_ingredients(None))
        self.assertEqual(result, [])

    # ---
    # api_cocktail_ingredients_route
    # ---

    def test_api_ct_ingred_route_1(self):
        result = json.loads(app.test_client().get('/api/cocktail/45/ingredients').data.decode())
        self.assertEqual(result[4]['name'], 'Lemon juice')

    def test_api_ct_ingred_route_2(self):
        result = json.loads(app.test_client().get('/api/cocktail/10/ingredients').data.decode())
        self.assertEqual(result[0]['quantity'], '1 part ')

    def test_api_ct_ingred_route_3(self):
        result = json.loads(app.test_client().get('/api/cocktail/0/ingredients').data.decode())
        self.assertEqual(result, [])

    # ---
    # api_cocktail_glass
    # ---

    def test_api_cocktail_glass_1(self):
        result = json.loads(idb.api_cocktail_glass(1))
        self.assertEqual(result['glass'], 'Highball glass')

    def test_api_cocktail_glass_2(self):
        result = json.loads(idb.api_cocktail_glass(2))
        self.assertEqual(result['glass'], 'White wine glass')

    def test_api_cocktail_glass_3(self):
        result = json.loads(idb.api_cocktail_glass(3))
        self.assertEqual(result['glass'], 'Cocktail glass')

    # ---
    # api_cocktail_glass_route
    # ---

    def test_api_cocktail_glass_route_1(self):
        result = json.loads(app.test_client().get('/api/cocktail/16/glass').data.decode())
        self.assertEqual(result['glass'], 'Parfait glass')

    def test_api_cocktail_glass_route_2(self):
        result = json.loads(app.test_client().get('/api/cocktail/143/glass').data.decode())
        self.assertEqual(result['glass'], 'vote')

    def test_api_cocktail_glass_route_3(self):
        result = json.loads(app.test_client().get('/api/cocktail/2/glass').data.decode())
        self.assertEqual(result['glass'], 'White wine glass')

    # ---
    # api_cocktail_recipe
    # ---

    def test_api_cocktail_recipe_1(self):
        result = json.loads(idb.api_cocktail_recipe(1))
        self.assertEqual(result['recipe'], '1. Fill a rocks glass with ice ' +
            '2.add white creme de cacao and vodka 3.stir')

    def test_api_cocktail_recipe_2(self):
        result = json.loads(idb.api_cocktail_recipe(2))
        self.assertEqual(result['recipe'], 'Blend with ice. Serve in a wine ' +
            'glass. Garnish with carrot.')

    def test_api_cocktail_recipe_3(self):
        result = json.loads(idb.api_cocktail_recipe(3))
        self.assertEqual(result['recipe'], 'Combine all ingredients in glass ' +
            'mixer. Chill and strain into Cocktail glass. Garnish with sliced strawberry.')

    # ---
    # api_cocktail_recipe_route
    # ---

    def test_api_ct_recipe_route_1(self):
        result = json.loads(app.test_client().get('/api/cocktail/2/recipe').data.decode())
        self.assertEqual(result['recipe'], 'Blend with ice. Serve in a wine ' +
            'glass. Garnish with carrot.')

    def test_api_ct_recipe_route_2(self):
        result = json.loads(app.test_client().get('/api/cocktail/79/recipe').data.decode())
        self.assertEqual(result['recipe'], 'Place one part dry gin in ' +
            'Cocktail Glass. Do NOT bruise the Gin! Carefully add two parts ' +
            'Sprite. Do NOT bruise the Sprite. Optionally, add a dash of ' +
            'cayenne pepper for added flavor. Add 3 tablespoons of dry ice ' +
            'for that mystical, yet strangely, psycho effect.')

    def test_api_ct_recipe_route_3(self):
        result = json.loads(app.test_client().get('/api/cocktail/128/recipe').data.decode())
        self.assertEqual(result['recipe'], 'Stir Vodka and Grenadine with ' +
            'ice. Fill in Champagne-flute without the ice. Fill up with ' +
            'champagne.')

    # ---
    # api_cocktail_image
    # ---

    def test_api_cocktail_image_1(self):
        result = json.loads(idb.api_cocktail_image(1))
        self.assertIsNotNone(result)

    def test_api_cocktail_image_2(self):
        result = json.loads(idb.api_cocktail_image(2))
        self.assertIsNotNone(result)

    def test_api_cocktail_image_3(self):
        result = json.loads(idb.api_cocktail_image(4))
        self.assertIsNotNone(result)

    # ---
    # api_cocktail_image_route
    # ---

    def test_api_cocktail_image_route_1(self):
        result = json.loads(app.test_client().get('/api/cocktail/66/image').data.decode())
        self.assertIsNotNone(result)

    def test_api_cocktail_image_route_2(self):
        result = json.loads(app.test_client().get('/api/cocktail/81/image').data.decode())
        self.assertIsNotNone(result)

    def test_api_cocktail_image_route_3(self):
        result = json.loads(app.test_client().get('/api/cocktail/220/image').data.decode())
        self.assertIsNotNone(result['imageURL'])

    # ---
    # api_ingredient_list
    # ---

    def test_api_ingredient_list_1(self):
        result = json.loads(idb.api_ingredient_list())
        self.assertEqual(result[0], {'name': 'Creme de Cacao', 'id': 1})

    def test_api_ingredient_list_2(self):
        result = json.loads(idb.api_ingredient_list())
        self.assertEqual(result[1], {'name': 'Vodka', 'id': 2})

    def test_api_ingredient_list_3(self):
        result = json.loads(idb.api_ingredient_list())
        self.assertIsNotNone(result[1])

    # ---
    # api_ingredient_list_route
    # ---

    def test_api_ingred_list_route_1(self):
        result = json.loads(app.test_client().get('/api/ingredient').data.decode())
        self.assertEqual(result[69]['id'], 70)

    def test_api_ingred_list_route_2(self):
        result = json.loads(app.test_client().get('/api/ingredient').data.decode())
        self.assertEqual(result[92]['name'], 'Tang')

    def test_api_ingred_list_route_3(self):
        result = json.loads(app.test_client().get('/api/ingredient').data.decode())
        self.assertEqual(result[41]['name'], 'Sour mix')

    # ---
    # api_ingredient
    # ---

    def test_api_ingredient_1(self):
        result = json.loads(idb.api_ingredient(1))
        self.assertEqual(result[0]['cocktails'][0]['id'], 1)

    def test_api_ingredient_2(self):
        result = json.loads(idb.api_ingredient(2))
        self.assertEqual(result[0]['numberOfCocktails'], 77)

    def test_api_ingredient_3(self):
        result = json.loads(idb.api_ingredient(3))
        self.assertEqual(result[0]['cocktails'][2]['name'], 'Caribbean Smoked Torch')

    # ---
    # api_ingredient_route
    # ---

    def test_api_ingredient_route_1(self):
        result = json.loads(app.test_client().get('/api/ingredient/212').data.decode())
        self.assertEqual(result[0]['name'], 'Daiquiri mix')

    def test_api_ingredient_route_2(self):
        result = json.loads(app.test_client().get('/api/ingredient/1').data.decode())
        self.assertEqual(result[0]['cocktails'][6],  {"name": "Golden Miller", "id": 158})

    def test_api_ingredient_route_3(self):
        result = json.loads(app.test_client().get('/api/ingredient/29').data.decode())
        self.assertEqual(result[0]['numberOfCocktails'], 13)

    # ---
    # api_ingredient_name
    # ---

    def test_api_ingredient_name_1(self):
        result = json.loads(idb.api_ingredient_name(1))
        self.assertEqual(result['name'], 'Creme de Cacao')

    def test_api_ingredient_name_2(self):
        result = json.loads(idb.api_ingredient_name(2))
        self.assertEqual(result['name'], 'Vodka')

    def test_api_ingredient_name_3(self):
        result = json.loads(idb.api_ingredient_name(3))
        self.assertEqual(result['name'], 'Dark rum')

    # ---
    # api_ingredient_name_route
    # ---

    def test_api_ingred_name_route_1(self):
        result = json.loads(app.test_client().get('/api/ingredient/17/name').data.decode())
        self.assertEqual(result['name'], 'Hot chocolate')

    def test_api_ingred_name_route_2(self):
        result = json.loads(app.test_client().get('/api/ingredient/172/name').data.decode())
        self.assertEqual(result['name'], 'Egg yolk')

    def test_api_ingred_name_route_3(self):
        result = json.loads(app.test_client().get('/api/ingredient/144/name').data.decode())
        self.assertEqual(result['name'], 'Thunderbird')

    # ---
    # api_ingredient_cocktails
    # ---

    def test_api_ingredient_cocktails_1(self):
        result = json.loads(idb.api_ingredient_cocktails(1))
        self.assertEqual(result[0], {'name': "'57 Chevy with a White License Plate", 'id': 1})

    def test_api_ingredient_cocktails_2(self):
        result = json.loads(idb.api_ingredient_cocktails(1))
        self.assertEqual(result[1], {'name': 'Alexander (Original)', 'id': 12})

    def test_api_ingredient_cocktails_3(self):
        result = json.loads(idb.api_ingredient_cocktails(None))
        self.assertEqual(result, [])

    # ---
    # api_ingredient_cocktails_route
    # ---

    def test_api_ingred_cts_route_1(self):
        result = json.loads(app.test_client().get('/api/ingredient/108/cocktails').data.decode())
        self.assertEqual(result[1]['name'], 'Don\'s Bloody Mary')

    def test_api_ingred_cts_route_2(self):
        result = json.loads(app.test_client().get('/api/ingredient/199/cocktails').data.decode())
        self.assertEqual(result[0]['name'], 'Lava Flow')

    def test_api_ingred_cts_route_3(self):
        result = json.loads(app.test_client().get('/api/ingredient/33/cocktails').data.decode())
        self.assertEqual(result[0]['name'], 'Apertif d\'Absinthe')

    # ---
    # api_ingredient_image
    # ---

    def test_api_ingredient_image_1(self):
        result = json.loads(idb.api_ingredient_image(1))
        self.assertEqual(result['imageURL'], '/static/images/ingredients/Creme+de+Cacao.jpg')

    def test_api_ingredient_image_2(self):
        result = json.loads(idb.api_ingredient_image(2))
        self.assertEqual(result['imageURL'], '/static/images/ingredients/Vodka.jpg')

    def test_api_ingredient_image_3(self):
        result = json.loads(idb.api_ingredient_image(3))
        self.assertEqual(result['imageURL'], '/static/images/ingredients/Dark+rum.jpg')

    # ---
    # api_ingredient_image_route
    # ---

    def test_api_ingred_image_route_1(self):
        result = json.loads(app.test_client().get('/api/ingredient/205/image').data.decode())
        self.assertEqual(result['imageURL'], '/static/images/ingredients/Orange' +
            '+peel.jpg')

    def test_api_ingred_image_route_2(self):
        result = json.loads(app.test_client().get('/api/ingredient/56/image').data.decode())
        self.assertEqual(result['imageURL'], '/static/images/ingredients/Grand' +
            '+Marnier.jpg')

    def test_api_ingred_image_route_3(self):
        result = json.loads(app.test_client().get('/api/ingredient/20/image').data.decode())
        self.assertEqual(result['imageURL'], '/static/images/ingredients/Soda+water.jpg')

    # ---
    # api_ingredient_numcocktails
    # ---

    def test_api_ingred_numcocktails_1(self):
        result = json.loads(idb.api_ingredient_numcocktails(1))
        self.assertEqual(result, {'numCocktails': 7})

    def test_api_ingred_numcocktails_2(self):
        result = json.loads(idb.api_ingredient_numcocktails(1))
        self.assertEqual(result['numCocktails'], 7)

    def test_api_ingred_numcocktails_3(self):
        result = json.loads(idb.api_ingredient_numcocktails(2))
        self.assertEqual(result, {'numCocktails': 77})

    # ---
    # api_ingredient_numcocktails_route
    # ---

    def test_api_ingred_numcts_route_1(self):
        result = json.loads(app.test_client().get('/api/ingredient/100/numcocktails').data.decode())
        self.assertEqual(result['numCocktails'], 3)

    def test_api_ingred_numcts_route_2(self):
        result = json.loads(app.test_client().get('/api/ingredient/71/numcocktails').data.decode())
        self.assertEqual(result['numCocktails'], 1)

    def test_api_ingred_numcts_route_3(self):
        result = json.loads(app.test_client().get('/api/ingredient/150/numcocktails').data.decode())
        self.assertEqual(result['numCocktails'], 4)

    # ---
    # query
    # ---

    # def test_query_1(self):
    #     result = json.loads(idb.query())
    #     self.assertEqual(result, {'numCocktails': 7})
    #
    # def test_query_2(self):
    #     result = json.loads(idb.query())
    #     self.assertEqual(result['numCocktails'], 7)
    #
    # def test_query_3(self):
    #     result = json.loads(idb.query())
    #     self.assertEqual(result, {'numCocktails': 77})

    # ---
    # query_route
    # ---

    def test_query_route_1(self):
        result = json.loads(app.test_client().get('/api/query').data.decode())
        with self.assertRaises(KeyError):
          result['numCocktails']

    def test_query_route_2(self):
        result = json.loads(app.test_client().get('/api/query').data.decode())
        self.assertEqual(result, {'cocktails': {'and': {}, 'or': {}},
            'ingredients': {'and': {}, 'or': {}}})

    def test_query_route_3(self):
        result = json.loads(app.test_client().get('/api/query').data.decode())
        self.assertIsNotNone(result)

    # def test_query_route_4(self):
    #     headers = {'query': 'blue'}
    #     result = requests.get(HOST + '/api/query', headers=headers)
    #     result_data = result.json()
    #     self.assertEqual(result_data['cocktail'], 4)

# ----
# main
# ----

if __name__ == "__main__":
    main()

# Coverage3 output

# .............................................................................
#......................................
# ----------------------------------------------------------------------
# Ran 115 tests in 0.708s
#
# OK
# Name        Stmts   Miss Branch BrPart  Cover   Missing
# -------------------------------------------------------
# idb.py        139     33     30      2    71%   36, 41, 46, 197-223, 228-238,
#   241, 195->197, 240->241
# models.py      40      0      0      0   100%
# -------------------------------------------------------
# TOTAL         179     33     30      2    77%   ------
