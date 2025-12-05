# https://goheels.com/sports/mens-basketball/roster

import pandas as pd

roster = ["Evans", "Davis", "Trimble"]
player = {"Last Name": roster}
data = pd.DataFrame(roster)    
print(data)