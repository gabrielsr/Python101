from datetime import datetime

right_this_minute = datetime.today().minute

months = ("January" ,"February" )
index = months.index("February")
print(index)
x = "March" in months
print(x)
