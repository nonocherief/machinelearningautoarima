import datetime
import random

items = ["phone","laptop","tablet","printer","smartwatch","cameras","desktop","tv","monitor"]

def gen_price(item):
    if item == "phone":
        return 100+random.randrange(900)
    elif item == "laptop":
        return 120+random.randrange(3000)
    elif item == "tablet":
        return 104+random.randrange(1400)
    elif item == "printer":
        return 10+random.randrange(300)
    elif item == "smartwatch":
        return 20+random.randrange(700)
    elif item == "cameras":
        return 35+random.randrange(3700)
    elif item == "desktop":
        return 700+random.randrange(5000)
    elif item == "tv":
        return 200+random.randrange(7000)
    else:
        return random.randrange(3000)

def gen_item():
    return random.choice(items)

def gen_items_today():
    return random.randrange(210)

currentDate = datetime.date.fromisoformat("2000-01-02")
delta = datetime.timedelta(days=1)

with open("data.csv", "w") as f:
    f.write("date,item,price\n")
    for i in range(1095):
        for j in range(gen_items_today()):
            item = gen_item()
            data=(currentDate.isoformat(),
            item,
            gen_price(item))
            
            line = f'%s,"%s",%s' % data
            #print(line)
            
            f.write(line+"\n")
        currentDate += delta
