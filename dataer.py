import pickle

stat = []

a = ["22"]
for fi in a:
    f = open(str(fi) + ".txt")

    stat = f.readlines()

    data = []
    for i in stat:
        if i[0] != "—" and i != "":
            data.append(i[0:len(i)-1])

##print(data[0:10])

stat = []
app = ""
for i in data:
    for j in i:
        if j != '!' and j != '.' and j != ',' and j != "-" and j != ":" and j != "—" and j != "«" and j != "»" and j != ";" and j != "(" and j != ")":
            app += j
        else:
            stat.append(app)
            app = ""

##print(stat[0:10])

data = []
data1 = []
app = ""
for i in stat:
    for j in i:
        if j != " ":
            app += j
        else:
            data1.append(app)
            app = ""

    data1.append(app)
    app = ""
    data.append(data1)
    data1 = []

##print(data[0:10])

x = 0
for i in data:
    for j in i:
        if j == "":
            data[x].remove(j)
    x += 1

##print(data[0:10])

##после выполнения программы
##имеем список со словами по порядку,
##разделённый по предложениям и обособляемым частям

stat = []
for i in data:
    count = 1
    for j in i:
        if count < len(i):
            app = []
            app.append(j)
            app.append(i[count])
            
            count += 1

        stat.append(app)


for i in stat:
    if i[0] == "" or i[1] == "":
        stat.remove(i)

##print(stat[0:10])
data = []
for  i in stat:
    t = 0
    for j in data:
        if i[0] == j[0]:
            j.append(i[1])
            t += 1
            break

    if t == 0:
        data.append(i)


stat = []
count = 0
for i in data:
    stat.append([i[0],[],[]])

    for j in i[1:len(i)-1]:
        stat[count][2].append(i[1:len(i)-1].count(j))
        stat[count][1].append(j)

    count += 1


data = []
for i in stat:
    if len(i) > 2:
        if i[2] == []:
            stat.remove(i)
        else:
##            print(i[2])
            data.append([i[0], i[1][i[2].index(max(i[2]))]])
print(len(data))

for i in data:
    if i[0] == " " or i[0] == "" or i[1] == " " or i[1] == "" or len(i[0]) > 20 or len(i[1]) > 20:
        data.remove(i)


print(len(data))


try:
    with open("data0.pickle", "wb") as f:
        pickle.dump(data, f, protocol=pickle.HIGHEST_PROTOCOL)
except Exception as ex:
    print("Error during pickling object (Possibly unsupported):", ex)
