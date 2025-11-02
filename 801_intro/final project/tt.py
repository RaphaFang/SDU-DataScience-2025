import requests
import json
import pandas as pd


url = "https://data.cityofnewyork.us/resource/bnx9-e6tj.json"
params = {
    "$limit": 10,
    "$where": "doc_type = 'DEED' and document_amt > 0",
    "$order": "recorded_datetime DESC"
}

res = requests.get(url, params)

if res.status_code == 200:
    data = res.json()
    print(data)
    with open("again_trad.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

    print("h.json")
else:
    data = res.json()
    print(data)
    print("na na", res.status_code)
# df = pd.DataFrame(res.json())
# print(df.head())
     


# url = "https://api.rentcast.io/v1/markets"
# params = {
#     "city": "New York",
#     "state": "NY",
#     "dataType": "Sale",
#     "historyRange": "2024-01:2025-10"
# }
# headers = {
#     "Accept": "application/json",
#     "X-Api-Key": "64ce33c0085642cf9193810237d3da94"
# }

# res = requests.get(url, headers=headers, params=params)

# if res.status_code == 200:
#     data = res.json()
#     with open("newyork_sale_history.json", "w", encoding="utf-8") as f:
#         json.dump(data, f, ensure_ascii=False, indent=4)

#     print("newyork_sale_history.json")
# else:
#     print("na na", res.status_code)