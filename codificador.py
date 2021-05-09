import matplotlib.pyplot as plt

def unipolar(inp):
    inp1=list(inp)
    inp1.insert(0,0)
    return inp1
    

def polar_nrz_l(inp):
    inp1=list(inp)
    inp1.insert(0,0)
    inp1=[-1 if i==0 else 1 for i in inp1]
    return inp1

def polar_nrz_i(inp):
    inp2=list(inp)
    lock=False
    for i in range(len(inp2)):
        if inp2[i]==1 and not lock:
            lock=True
            continue
        if lock and inp2[i]==1:
            if inp2[i-1]==0:
                inp2[i]=1
                continue
            else :
                inp2[i]=0
                continue
        if lock:
            inp2[i]=inp2[i-1]
    inp2=[-1 if i==0 else 1 for i in inp2]        
    return inp2
    

def polar_rz(inp):
    inp1=list(inp)
    inp1=[-1 if i==0 else 1 for i in inp1]
    li=[]
    for i in range(len(inp1)):
        li.append(inp1[i])
        li.append(0)
    return li
    

def Biphase_manchester(inp):
    inp1=list(inp)
    li,init=[],False
    for i in range(len(inp1)):
        if inp1[i]==0:
            li.append(-1)
            if not init:
                li.append(-1)
                init=True
            li.append(1)
        elif inp1[i]==1 :
            li.append(1)
            li.append(-1)
    return li        
    

def Differential_manchester(inp):
    inp1=list(inp)
    li,lock,pre=[],False,''
    for i in range(len(inp1)):
        if inp1[i]==0 and not lock:
            li.append(-1)
            li.append(-1)
            li.append(1)
            lock=True
            pre='S'
        elif inp1[i]==1 and not lock :
            li.append(1)
            li.append(1)
            li.append(-1)
            lock=True
            pre='Z'
        else:
            if inp1[i]==0:
                if pre=='S':
                    li.append(-1);li.append(1)
                else:
                    li.append(1);li.append(-1)
            else:
                if pre=='Z':
                    pre='S'
                    li.append(-1);li.append(1)
                else:
                    pre='Z'
                    li.append(1);li.append(-1)                     
    return li                        


def AMI(inp):
    inp1=list(inp)
    inp1.insert(0,0)
    lock=False
    for i in range(len(inp1)):
        if inp1[i]==1 and not lock:
            lock=True
            continue
        elif lock and inp1[i]==1:
            inp1[i]=-1
            lock=False
    return inp1  

    

def plot(li, cods, i=0):
    print(i)
    lista = []
    if "0" in cods:
        lista = [1 ,2 ,3 ,4 ,5 ,6 ,7]
    else:
        for i in range(len(cods.split(","))):
            lista.append(int(cods.split(",")[i]))
    if 1 in lista:
        i+=1
        plt.subplot(7,1,i)
        plt.ylabel("Unipolar-NRZ{}".format(i))
        plt.plot(unipolar(li),color='red',drawstyle='steps-pre',marker='>')
    if 2 in lista:
        i+=1
        plt.subplot(7,1,i)
        plt.ylabel("P-NRZ-L{}".format(i))
        plt.plot(polar_nrz_l(li),color='blue',drawstyle='steps-pre',marker='>')
    if 3 in lista:
        i+=1
        plt.subplot(7,1,i)
        plt.ylabel("P-NRZ-I{}".format(i))
        plt.plot(polar_nrz_i(li),color='green',drawstyle='steps-pre',marker='>')
    if 4 in lista:
        i+=1
        plt.subplot(7,1,i)
        plt.ylabel("Polar-RZ{}".format(i))
        plt.plot(polar_rz(li),color='red',drawstyle='steps-pre',marker='>')
    if 5 in lista:
        i+=1
        plt.subplot(7,1,i)
        plt.ylabel("B_Man{}".format(i))
        plt.plot(Biphase_manchester(li),color='violet',drawstyle='steps-pre',marker='>')
    if 6 in lista:
        i+=1
        plt.subplot(7,1,i)
        plt.ylabel("Dif_Man{}".format(i))
        plt.plot(Differential_manchester(li),color='red',drawstyle='steps-pre',marker='>')
    if 7 in lista:
        i+=1
        plt.subplot(7,1,i)
        plt.ylabel("A-M-I{}".format(i))
        plt.plot(AMI(li),color='blue',drawstyle='steps-pre',marker='>')
    return i


if __name__=='__main__':
    print("\n"*50)
    print("0-Todos\n1-Unipolar-NRZ\n2-P-NRZ-L\n3-P-NRZ-I\n4-Polar-RZ\n5-B_Man\n6-Dif_Man\n7-A-M-I\n")
    codigos = str(input("Seleccion el tipo de codificacion, podes separarlos por \",\" (ej: 1, 3, 5): "))
    binarios = input("\nIngresa el binario:  ")
    if "," not in binarios:
        binario = [int(x) for x in str(binarios)]
        plot(binario, codigos)
    else:
        num = 0
        for i in range(len(binarios.split(","))):
            print(binarios.split(",")[i])
            binario = [int(x) for x in str(binarios.split(",")[i])]
            num = plot(binario, codigos, num)
    plt.show()