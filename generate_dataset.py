import pandas as pd
import random

data = []

# Generate Normal Traffic
for i in range(500):
    src = random.choice(["h1", "h2", "h3"])
    dst = random.choice(["h1", "h2", "h3"])

    while src == dst:
        dst = random.choice(["h1", "h2", "h3"])

    protocol = random.choice(["TCP", "UDP", "ICMP"])

    packets = random.randint(10,80)
    bytes_ = packets * random.randint(60,120)

    duration = random.uniform(0.5,5)

    label = "Normal"

    data.append([src,dst,protocol,packets,bytes_,duration,label])


# Generate Attack Traffic
for i in range(500):

    src = random.choice(["h1","h2","h3"])
    dst = random.choice(["h1","h2","h3"])

    while src==dst:
        dst=random.choice(["h1","h2","h3"])

    protocol=random.choice(["TCP","UDP","ICMP"])

    packets=random.randint(150,500)

    bytes_=packets*random.randint(100,150)

    duration=random.uniform(5,15)

    label="Attack"

    data.append([src,dst,protocol,packets,bytes_,duration,label])


df=pd.DataFrame(data,columns=[
"Source",
"Destination",
"Protocol",
"Packets",
"Bytes",
"Duration",
"Label"
])

df=df.sample(frac=1).reset_index(drop=True)

df.to_csv("data/sdn_dataset.csv",index=False)

print("Dataset Generated Successfully!")

print(df.head())
