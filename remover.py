import pickle
try:
    with open("data0.pickle", "rb") as f:
        data = pickle.load(f)
except Exception as ex:
    print("Error during unpickling object (Possibly unsupported):", ex)


count = 0
stat = data
for i in data:
    count = 0
    for j in stat:
        if j[0] == i[1]:
            count += 1

    if count < 1:
        data.remove(i)





print(len(data))

##print(data)
resultr = []
res = ""
for i in data:
    res += i[0] + " "
    res += i[1] + " " 
    count = 1
    nexxt = i[1]

    while count != 0 and len(res) < 1000:
        count = 0        
        for j in data:
            if j[0] == nexxt:
                res += j[1] + " "
                nexxt = j[1]
                count += 1
                break
            

    print(res)
    resultr.append(res) 
    res = ""

s = []
for i in resultr:
    if len(i) < 100:
        s.append(i)
    
print("result: " + str(max(s, key=len)))        
        
        
