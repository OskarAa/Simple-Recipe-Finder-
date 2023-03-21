TheMealDB API - Python Code
This Python code uses TheMealDB API to retrieve meals that contain a specific ingredient. The code prompts the user to enter an ingredient, sends a GET request to the API URL constructed using the entered ingredient, and retrieves the list of meals that contain the specified ingredient. The code then prints the names of the meals retrieved from the API.

Requirements
This code requires the following:

Python 3.x
requests library (you can install this using pip)

Installation
Clone the repository or download the mealdb.py file.
Install the requests library by running the following command:
Copy code
pip install requests

Usage
Open a terminal window and navigate to the directory where the mealdb.py file is located.
Run the following command to start the Python code:
Copy code
python mealdb.py
Enter an ingredient when prompted and press Enter.
The code will retrieve the meals that contain the specified ingredient and print their names.

Example
Here's an example of using the code:

python
Copy code
$ python mealdb.py
Enter an ingredient: chicken
Meals containing chicken:
Chicken Handi
Chicken Alfredo Primavera
Garlic and Lemon Chicken
Honey Balsamic Chicken Breasts
...
License
This code is licensed under the MIT License. See the LICENSE file for details.

Credits
This code was written by [Oskar A.]. The code uses TheMealDB API.
