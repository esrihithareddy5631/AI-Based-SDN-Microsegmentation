import joblib
import pandas as pd
import requests

# Load AI model
model = joblib.load("models/ai_model.pkl")

# Example traffic
traffic = pd.DataFrame([{
    "Source":0,
    "Destination":2,
    "Protocol":1,
    "Packets":300,
    "Bytes":42000,
    "Duration":9
}])

prediction = model.predict(traffic)

if prediction[0]==0:

    print("Attack Detected")
    print("Installing ONOS Flow Rule...")

    ONOS_URL="http://localhost:8181/onos/v1/flows/of:0000000000000001"

    AUTH=("onos","rocks")

    rule={
      "priority":50000,
      "timeout":0,
      "isPermanent":True,
      "treatment":{
        "instructions":[
            {
              "type":"NOACTION"
            }
        ]
      },
      "selector":{
        "criteria":[
          {
            "type":"ETH_TYPE",
            "ethType":"0x0800"
          },
          {
            "type":"IPV4_SRC",
            "ip":"10.0.0.1/32"
          },
          {
            "type":"IPV4_DST",
            "ip":"10.0.0.3/32"
          }
        ]
      }
    }

    r=requests.post(ONOS_URL,json=rule,auth=AUTH)

    print("Status :",r.status_code)

else:

    print("Normal Traffic")
    print("No Rule Installed")
