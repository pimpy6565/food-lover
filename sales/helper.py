import requests

class food(): 
    def __init__(self,n):
        url = requests.get(f'https://www.themealdb.com/api/json/v1/1/search.php?s={n.capitalize()}').json()
        self.data = url['meals']
        self.n = n
        self.instructions = self.data[0]['strInstructions']
        self.img = self.data[0]['strMealThumb']
        self.video = self.data[0]['strYoutube']
       
    def get_ingredients(self):
        url = f"https://www.themealdb.com/api/json/v1/1/search.php?s={self.n.capitalize()}"
        response = requests.get(url)
        data = response.json()

        if data['meals']:
            meal = data['meals'][0]  # Get first matched meal
            ingredients = []

            for i in range(1, 25):  # Max 20 ingredients
                ingredient = meal.get(f"strIngredient{i}")
                measure = meal.get(f"strMeasure{i}")
                if ingredient and ingredient.strip():
                    ingredients.append({
                        "Ingredient": ingredient.strip(),
                        "Measure": measure.strip() if measure else ""
                    })
            
            return ingredients
        else:
            return None


def CATEGORY():
    url = requests.get('https://www.themealdb.com/api/json/v1/1/categories.php').json()
    category = url['categories']
    categorys = [i["strCategory"] for i in category]
    img = [j["strCategoryThumb"] for j in category]
    return categorys,img

def ITEM(n):
    url = requests.get(f'https://www.themealdb.com/api/json/v1/1/filter.php?c={n}').json()
    
    meals = url['meals']  # This is a list of meal dicts
    
    categorys = [meal["strMeal"] for meal in meals]
    img = [meal["strMealThumb"] for meal in meals]
    
    return categorys, img