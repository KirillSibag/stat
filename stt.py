import pickle
import pyttsx3
import time

engine = pyttsx3.init()     # инициализация движка

# зададим свойства
engine.setProperty('rate', 200)     # скорость речи
engine.setProperty('volume', 1)   # громкость (0-1)

try:
    with open("data0.pickle", "rb") as f:
        data = pickle.load(f)
except Exception as ex:
    print("Error during unpickling object (Possibly unsupported):", ex)

import random as r

fill = open("res.txt", "w+")
    

while 1:
    print("режим: список - 1, прогрессия - 2")
    mode = int(input())
    if mode == 1:
        stri = ""
 
        print("длина:")
        i = int(input())
        print("лимит:")
        limit = int(input())
        print("разброс:")
        viiiu = int(input())

        d = r.randint(0, len(data)-1)
        nexxt = data[d][r.randint(1, len(data[d])-1)]
        stri += nexxt

        count = 0
        while count < i:
            t = 1
            while t != 0:
                t = 0
                for j in data:
                    if j[0] == nexxt:
                        nexxt = j[r.randint(1, len(j)-1)]
                        stri += " " + nexxt
                        t += 1
                if t == 0:
                    stri += ". "
                    if len(stri) > limit and len(stri) < limit + viiiu:                     
                        print(str(count + 1) + ". " + stri)
                        fill.write(str(count + 1) + ". " + stri + "\n")

##                        engine.say(stri)      # запись фразы в очередь
##                        engine.runAndWait()
                        count += 1
                    stri = ""

                    d = r.randint(0, len(data)-1)
                    nexxt = data[d][r.randint(1, len(data[d])-1)]
                    stri += nexxt

        fill.close()
        engine.say("всё закончилось. давай пиши ещё.")      # запись фразы в очередь
        engine.runAndWait()

    elif mode == 2:
        stri = ""

        print("длина:")
        i = int(input())
        print("старт:")
        limit = int(input())
        print("шаг:")
        shag = int(input())
        
        d = r.randint(0, len(data)-1)
        nexxt = data[d][r.randint(1, len(data[d])-1)]
        stri += nexxt

        count = 0
        while count < i:
            t = 1
            while t != 0:
                t = 0
                for j in data:
                    if j[0] == nexxt:
                        nexxt = j[r.randint(1, len(j)-1)]
                        stri += " " + nexxt
                        t += 1
                if t == 0:
                    stri += ". "
                    if len(stri) > limit:
                        print(str(count + 1) + ". " + stri + "  ___ " + str(len(stri)))
##                        engine.say(stri)
##                        engine.runAndWait()
                        count += 1
                        limit += shag
                        if len(stri) > limit:
                            limit = len(stri)
                            
                    stri = ""

                    d = r.randint(0, len(data)-1)
                    nexxt = data[d][r.randint(1, len(data[d])-1)]
                    stri += nexxt

    elif mode == 3:
            stri = ""
            nexxt = data[0][1]
            stri += nexxt
            print(nexxt)
            cn = 0
            count = 0
            while cn < len(data):
                nexxt = data[cn][1]
                stri += nexxt

                t = 0
                for j in data:
                    if j[0] == nexxt:
                        nexxt = j[1]
                        stri += " " + nexxt
                        t += 1
##                          break
                        
                if t == 0:
                    stri += ". "                 
                    print(str(count + 1) + ". " + stri)
                    fill.write(str(count + 1) + ". " + stri + "\n")

    ##                        engine.say(stri)      # запись фразы в очередь
    ##                        engine.runAndWait()
                    count += 1
                    stri = ""
                    cn+=1

            fill.close()
            engine.say("всё закончилось. давай пиши ещё.")      # запись фразы в очередь
            engine.runAndWait()


    
    print("")

