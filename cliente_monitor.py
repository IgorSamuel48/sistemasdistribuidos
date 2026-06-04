import requests

ips = [

"IP1",

"IP2",

"IP3"

]

for ip in ips:

    try:

        r = requests.get(f"http://{ip}:5000/info")

        print(r.json())

    except:

        print(ip, "indisponível")
