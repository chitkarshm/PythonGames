from datetime import datetime
from datetime import timedelta


def world_times():
    mycity = datetime.now()
    india = mycity + timedelta(hours=13.5)
    nepal = mycity + timedelta(hours=13.75)
    iran = mycity + timedelta(hours=11.5)
    all_times = f"It is {mycity:%I:%M %p} in my city. That means it is {india:%I:%M %p} in India, {nepal:%I:%M %p} in Nepal, and {iran:%I:%M %p} in Iran! "
    print(all_times)


world_times()
