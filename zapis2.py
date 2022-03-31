import glob

txt_files = glob.glob('*.txt')
#print(txt_files)

def sort_func():
    slovar = {}
    list_num = []
    
    for file in txt_files:
        s = 0
        list_f = []
        with open(file,encoding='utf-8') as f:
            for line in f:
                list_f.append(line.strip())
                s += 1
            list_num.append(s)    
            slovar[str(s)] = [file,[list_f]]
            list_num.sort()
    with open('text3.txt','w',encoding='utf-8') as file:
        for i in list_num:
            for k,v in slovar.items():
                if k == str(i):
                    file.write(v[0]+ '\n')
                    #file.write()
                    file.write(str(k)+'\n')
                    for stroka in v[1]:
                        for i in stroka:
                            file.write(i +'\n')
            

sort_func()
