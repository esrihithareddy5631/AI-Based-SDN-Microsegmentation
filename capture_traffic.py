import subprocess

print("Capturing traffic...")

subprocess.run([
    "sudo",
    "tcpdump",
    "-i",
    "any",
    "-c",
    "100",
    "-w",
    "traffic.pcap"
])

print("Capture completed.")
