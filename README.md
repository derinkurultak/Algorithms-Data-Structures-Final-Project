# INSTARECIPE
# Table of Contents

1. Introduction
2. What Does the Project Do
3. Getting Started with the Project
4. Credits

# Introduction
As BBA DBA second year students in IE University, we are carrying out this project to learn by putting into practice the theoretical concepts we’ve learned in the Algorithms and Data Structures course. The objective is to create an application that helps students (and also university students in general) have efficient management of their meal prepping process, making life easier and allowing less waste of food, money, and time. We want to recommend specific recipes to each person, tailored to their preferences to maximise their satisfaction.

# What Does the Project Do?
For IE students who need an easy means to find recipes that adapt to their lifestyle, preferences/tastes, available ingredients and scarce time to cook, Instarecipe is an app to find recipes in seconds. Unlike Instagram or Pinterest, it's better because it only focuses on recipes and it recommends the most appropriate recipes for each user according to their specifications (what ingredients they have, what cuisines they prefer etc). The user is shown only the recipes for which he/she has over 70% of the ingredients, also considering the importance of each ingredient in the recipe. 

In the Python file “**INSTARECIPE_main.py**”, the main algorithm takes available ingredients and preferred cuisines in order as **inputs** and the **output** is the recommended recipes. As additional features, the user can just search recipes according to cuisine or difficulty level.


## Why Is the Project Useful?
With our app, the users can easily find recipes in seconds, making their meal prep process way more efficient and enjoyable. After our market research and surveys, we developed this app considering the insights we obtained. This app eliminates problems such as being overwhelmed about cooking, spending extra money on overpriced food for being lazy to cook, having food go bad in the fridge, looking for good recipes for hours on social media and still eating the same unhealthy meals every week.
## Extra Information About the Code
In our code, we used a graph which is a non-linear data structure because non-linear data structures are better for multi-level storage. Moreover, graphs are great for recommendations which is the main activity of our app. A depth-first search algorithm is used to traverse the graph.

In the graph, each node is a recipe containing information regarding ingredients, difficulty level, cuisine, a link to access the full recipe, the rating given by user after they try the recipe, and whether they have saved the recipe or not.

Our main algorithm is recommending recipes according to the users available ingredients and preferred cuisines. However, the user has the option to view recipes according to only cuisine or only difficulty level.

**Limitations**
* The algorithm currently has only 60 recipes and 6 cuisines (10 recipe per each cuisine.)
* There is no advanced GUI for the user to interact with.

# Getting Started with the Project
**Resources:**
To start using this app, make sure you have installed the following:
- Python programming language (The app was developed using Python 3.9.12 on MacOs Monterey 12.3.1)
- Python environment (Pycharm 2022.2 has been used for this project.)
- The following library: If you would like to use the code which includes the GUI, make sure you download **PySimpleGUI** library. After the download, it should be imported like the following:
``` import PySimpleGUI ```

1. The user should open the Python file in a Python environment. 
2. In the variable "cuisines" on line 288, the user should input their favorite types of cuisines in a list in preference order. (The available cuisines are 'spanish', 'mexican', 'japanese', 'general/not specified', 'thai', 'italian'.)
3. In the variable "availableIngredients" on line 307, the user should input the ingredients he/she has in a list in order to get recipes recommended. 
4. The user should make sure that there are no gramatical errors made while typing down the cuisines and ingredients.
5. The user should input the ingredients and cuisines as singular nouns and in lower case letters.
6. ``` startNode.dfs() ``` should be run.
7. The user will receive the recommended recipes according to their cuisine preference order and difficulty level (from easiest to hardest).
8. If the user wishes to view only recipes to one specific cuisine, the user should run the lines 315-318 (including 315-318).
9. If the user wishes to view only recipes to one specific difficulty level (level 1, level 2, level 3), the user should run the lines 321-324 (including 321-324).

# Credits
Our group consists of six determined students of the Dual Degree in Business Administration & Data and Business Analytics. The development team is as follows: 
* Adrian Con
* Derin Kurultak
* Esteban Sanchez
* Laura Bradford
* Romane Prisant
* Valeria Ulloa

In addition to our team, we have a skilled and experienced mentor, Antonio Lopez, who is also our professor for the course and has been a key resource along the process of the development of the app.
