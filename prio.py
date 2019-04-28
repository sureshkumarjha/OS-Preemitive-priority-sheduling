class process(object):
	def __init__(self,n,at,bt,pi):
		self.n=n
		self.at=at
		self.bt=bt
		self.pi=pi
def getprio(arr):
    mi=arr[0]
    for x in range(1,len(arr)):
        if(int(arr[x].pi) < mi.pi):
            mi=arr[x]
    return int(mi.n)          
arr=[]
wtarr=[] 
btsum=0
ogbt=[]
tat=[]
n=int(input("Enter no of Process: "))
for i in range(n):
    print("ENTER PROCESS ",i)
    arr.append(process(i,int(input("Enter Arrival time: ")),int(input("Enter Burst time: ")),int(input("Enter Priority: "))))
    print("--------------------------------------------------------------------------------------------------")
    ogbt.append(arr[i].bt)
    btsum+=arr[i].bt
    wtarr.append(0)
print("\t P[]\t AT\t BT\t PI\t")    
for i in range(n):    
    print("\tP[",arr[i].n,"]\t",arr[i].at,"\t",arr[i].bt,"\t",arr[i].pi,"\t")
print("-------------------------------------------------------------------------------------------------------")
piarr=[]
cat=0
cp=0
def wt(prior,cp,wtarr,arr):
    for x in range(len(prior)):
        if(x==cp or arr[x].bt=="X"):
            continue
        else:
            wtarr[x]+=1    
for x in range(btsum):
    if(x==arr[cat].at):    
        piarr.append(arr[cat])
        if(cat!=0):
                if arr[cp].bt==1:
                        arr[cp].bt="X"
                        piarr[cp].pi=10
                        cp=getprio(piarr)
                else:
                        arr[cp].bt-=1   
        cp=getprio(piarr) 
        if(cat!=n-1):    
            cat+=1

    else:
         if(arr[cp].bt!="X"):
                 if arr[cp].bt==1:
                        arr[cp].bt="X"
                        piarr[cp].pi=10
                        cp=getprio(piarr)
                 else:
                        arr[cp].bt-=1  
    wt(piarr,cp,wtarr,arr)                     
    print(x,end="")            
    for i in range(n):
                print("\t",arr[i].bt,"\t",end="")       
    print("P[",cp,"]",end="")
    print("")
print("-------------------------------------------------------------------------------------------------------")
for x in range(n):
        tat.append(wtarr[x]+ogbt[x])
        print("P[",x,"]---",wtarr[x],"---",tat[x])
        
print("The Average Wating Time is:",sum(wtarr)/n)                        
            
print("The Average Turn Around Time is:",sum(tat)/n) 


        
        





	
