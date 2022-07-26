from datetime import datetime
list = []
for i in range(1,60,2):
    list.append(i)
right_this_minute = datetime.today().minute
if right_this_minute in list:
    print("This minute is little odd.")
else:
    print("Not an odd minute.")
