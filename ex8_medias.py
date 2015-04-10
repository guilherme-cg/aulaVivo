x=0
maior=0
m=0
i=-1
while x>=0:      
    m=m+x
    i=i+1
    try:    
        x=float(raw_input("Digite a Nota ->"))
        if (x>maior):
            maior=x
    except:
        x=0
        i=i-1
        print ("numero invalido")
if (i>0):
    mf=m/i
    print "Media ->", mf
    print "Maior Nota ->", maior
else:
    print "Nenhuma Nota"
