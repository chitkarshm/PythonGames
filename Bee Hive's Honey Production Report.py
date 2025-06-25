import random

needsnectar = 20000
hasnectar = 0
nectardeposits = 0
for hour in range(365 * 18):
    dropoffs = random.randint(hasnectar // 4, 3 * hasnectar // 4)
    pickups = random.randint(needsnectar // 4, 3 * needsnectar // 4)
    hasnectar = hasnectar + pickups - dropoffs
    needsnectar = needsnectar - pickups + dropoffs
    nectardeposits = nectardeposits + dropoffs
honey = round(nectardeposits / 90)
print(f"This hive produced {honey} grams of honey in a year.")
