# https://goheels.com/sports/mens-basketball/roster

import pandas as pd

player = {"Last Name": ["Evans", "Davis", "Trimble"],
          "First Name": ["Kyan", "Elijah", "Seth"],
          "height": [74, 75, 75],
          "weight": [175, 205, 200]}
data = pd.DataFrame(player)    
print(data)