# import random 
# print(random.randint(1,9))
# employees = ["Amy","Cathy","Mike"]
# print(random.choice(employees))

# import math 
# print(math.sqrt(25))
# print(math.ceil(2.1))
# print(math.floor(2.1))
# print(math.factorial(3))
# print(math.prod([2,3,4]))

# from datetime import date 
# dt = date.today()
# # dt = date(2025,1,1)
# print(dt)
# print(dt.year)
# print(dt.month)
# print(dt.day)
# print(dt.weekday())
# print(dt.strftime("%B %d %y"))
# print(dt.strftime("%B %d %Y"))
# print(dt.strftime("%m/%d/%Y"))

# from datetime import time 
# t = time(20,2,10)
# print(t)
# print(t.hour)
# print(t.second)
# print(t.minute)

# from datetime import datetime 
# dt = datetime.now()
# # dt = datetime(2026,1,1,10,10,10)
# # dt = datetime.utcnow()
# print(dt)
# print(dt.hour)

# from datetime import datetime,date,timedelta 
# today = date.today()
# print(today)
# yesterday = today - timedelta(days=1)
# print(yesterday)
# tomorrow = today + timedelta(days=1)
# print(tomorrow)

# from datetime import datetime,date,timedelta 
# t1 = datetime(2027,1,1)
# t2 = datetime.now()
# t = t1 - t2 
# print(t)
# print(t.days)
# print(t.seconds)

# from datetime import datetime 
# dt = datetime.now() 
# print(dt)
# print(dt.strftime("%Y-%m-%d"))
# print(dt.strftime("%B %d %Y %H:%M:%S"))
# print(dt.strftime("%B %d %Y %I%p"))

# from datetime import datetime
# dt = datetime.now() 
# print(dt)
# timestamp = dt.timestamp()
# print(timestamp)

import time 
print("Start")
time.sleep(2)
print("End")