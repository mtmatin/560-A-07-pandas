# https://goheels.com/sports/mens-basketball/roster

import pandas as pd

player = {"Last Name": ["Evans", "High", "Brown", "Dixon", "Young", "Denis", "Davis", "Trimble", "Wilson", "Powell"],
          "First Name": ["Kyan", "Zayden", "James", "Derek", "Jaydon", "Isaiah", "Elijah", "Seth", "Caleb", "Jonathan"],
          "height": [74, 82, 82, 77, 76, 76, 75, 75, 82, 78],
          "weight": [175, 230, 240, 200, 200, 180, 205, 200, 215, 190]
}

data = pd.DataFrame(player)   

# bmi = weight in kg/height in m squared
data["bmi"] = (data["weight"]/2.205)/((data["height"]/39.37)**2)
data["bmi"] = data["bmi"].round(2)

print(data)

data.to_csv("bmi.csv")