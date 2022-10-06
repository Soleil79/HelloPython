
with open('poli.txt', 'r', encoding="utf-8") as f1, \
    open('poli2.txt', 'r', encoding="utf-8") as f2,\
    open('poli_sum.txt', 'a', encoding='utf-8') as f3:
        while True:
            str1 = f1.readline() 
            str2 = f2.readline()
            if not str1 or not str2:
                break
            sum = str1[:-4] + '+ ' + str2
            f3.write(f"{sum}")


