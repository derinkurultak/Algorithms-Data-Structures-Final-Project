# INSTARECIPE
# Table of Contents

1. Introduction
2. What Does the Project Do
3. Getting Started with the Project
4. Credits

# Introduction
As BBA DBA second year students in IE University, we are carrying out this project to learn by putting into practice the theoretical concepts we’ve learned in the Algorithms and Data Structures course. The objective is to push ourselves and learn further coding techniques/concepts to create an application that helps IE students (and also university students in general) have efficient management of their meal prepping process, making life easier and allowing less waste of food, money, and time. We want to recommend specific recipes to each person, tailored to their preferences to maximise their satisfaction.

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

## Getting Started with the Project
**Resources:**
To start using this app, make sure you have installed the following:
- Python programming language (The app was developed using Python 3.9.12 on MacOs Monterey 12.3.1)
- Python environment (Pycharm 2022.2 has been used for this project.)
- The following library: If you would like to use the code which includes the GUI, make sure you download **PySimpleGUI** library. After the download, it should be imported like the following:
``` import PySimpleGUI ```

1. Initially, the user should input in the app their favorite types of cuisines (in preference order)
2. The user should input the ingredients he/she has in order to get recipes recommended. 
3. The user will receive the recommended recipes according to their cuisine preference order and difficulty level (from easiest to hardest).

## Credits
Our group consists of six determined students of the Dual Degree in Business Administration & Data and Business Analytics. The development team is as follows: 
* Adrian Con
* Derin Kurultak
* Esteban Sanchez
* Laura Bradford
* Romane Prisant
* Valeria Ulloa
In addition to our team, we have a skilled and experienced mentor, Antonio Lopez, who is also our professor for the course and has been a key resource along the process of the development of the app.
