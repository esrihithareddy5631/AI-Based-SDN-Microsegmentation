from scapy.all import rdpcap
import pandas as pd

packets = rdpcap("traffic.pcap")

rows = []

for pkt in packets:

    length = len(pkt)

    protocol = pkt.lastlayer().name

    rows.append({
        "PacketLength": length,
        "Protocol": protocol
    })

df = pd.DataFrame(rows)

print(df.head())

df.to_csv("real_features.csv", index=False)

print("Features extracted successfully.")
