import json, os
from datetime import datetime

SUP='data/suppliers.json'
TX='data/transactions.json'

def load(p):
    return json.load(open(p)) if os.path.exists(p) else []

def save(p,d):
    json.dump(d,open(p,'w'),indent=2)

sup=load(SUP); tx=load(TX)

while True:
    print("\n1.Add Supplier\n2.List Suppliers\n3.New Weighment\n4.View Transactions\n5.Exit")
    c=input("Choice: ")
    if c=="1":
        sid=f"SUP{len(sup)+1:03}"
        name=input("Name: "); village=input("Village: ")
        sup.append({"id":sid,"name":name,"village":village})
        save(SUP,sup)
        print("Added",sid)
    elif c=="2":
        for s in sup: print(s)
    elif c=="3":
        sid=input("Supplier ID: ")
        s=next((x for x in sup if x['id']==sid),None)
        if not s:
            print("Supplier not found"); continue
        g=float(input("Gross kg: "))
        t=float(input("Tare kg: "))
        if t>g:
            print("Invalid weights"); continue
        n=g-t
        r=float(input("Rate/kg: "))
        amt=n*r
        tid=f"TXN{len(tx)+1:06}"
        rec={"id":tid,"supplier":sid,"gross":g,"tare":t,"net":n,"rate":r,"amount":amt,"time":datetime.now().isoformat()}
        tx.append(rec); save(TX,tx)
        print(rec)
    elif c=="4":
        for r in tx: print(r)
    else:
        break
