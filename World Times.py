from datetime import datetime
from datetime import timedelta


def world_times():
    mycity = datetime.now()
    india = mycity + timedelta(hours=13.5)
    london = mycity + timedelta(hours=8)
    paris = mycity + timedelta(hours= 9)
    all_times = f"It is {mycity:%I:%M %p} in my city. That means it is {india:%I:%M %p} in Mumbai, {london:%I:%M %p} in London, and {paris:%I:%M %p} in Paris! "
    print(all_times)


world_times()
