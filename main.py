import requests
import json

ingredient = input("Enter an ingredient: ")
url = f"https://www.themealdb.com/api/json/v1/1/filter.php?i={ingredient}"

response = requests.get(url)

if response.status_code == 200:
    data = json.loads(response.content)
    meals = data['meals']
    
    if meals is None:
        print("No meals found with that ingredient.")
    else:
        print(f"Meals containing {ingredient}:")
        for meal in meals:
            print(meal['strMeal'])
else:
    print("Unable to retrieve data from API.")