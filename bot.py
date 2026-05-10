import requests
from datetime import datetime
TOKEN = "8608245715:AAGGH4eZu0J6oMBYSR8HkWS2P7h4kQxDtQk"
CHAT_ID = "2137957785"
def send(msg):
    requests.post("https://api.telegram.org/bot"+TOKEN+"/sendMessage",json={"chat_id":CHAT_ID,"text":msg})
try:
    r1=requests.get("https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum,solana&vs_currencies=usd&include_24hr_change=true",timeout=15).json()
    r2=requests.get("https://api.alternative.me/fng/?limit=1",timeout=15).json()
    btc=r1["bitcoin"]["usd"]
    eth=r1["ethereum"]["usd"]
    sol=r1["solana"]["usd"]
    chg=round(r1["bitcoin"]["usd_24h_change"],1)
    fg=int(r2["data"][0]["value"])
    fgl=r2["data"][0]["value_classification"]
    now=datetime.now().strftime("%d %b %H:%M")
    send("BTC Bot OK
"+now+"
BTC: $"+str(round(btc))+" ("+str(chg)+"%)
ETH: $"+str(round(eth))+"
SOL: $"+str(round(sol,1))+"
Fear Greed: "+str(fg)+" ("+fgl+")")
    if btc<57000:send("ALERTA BTC sub 57K: $"+str(round(btc)))
    if fg<=10:send("ALERTA Fear Greed CRITIC: "+str(fg))
    print("OK BTC:"+str(round(btc)))
except Exception as e:
    print("ERR:"+str(e))
