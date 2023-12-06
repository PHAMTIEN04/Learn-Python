class Canbangchanban:
    def __init__(self,T):
        self.T = int(T)
    def handle(self):
        while(self.T > 0):
            list_a = input().split()
            for i in range(len(list_a)):
                list_a[i] = int(list_a[i])

            for i in range(1,len(list_a)-1):
                if list_a[i] < list_a[i-1]:
                    list_a[i] = list_a[i] + list_a[len(list_a)-1]
                    break
                elif list_a[i] > list_a[i-1]:
                    list_a[i-1] = list_a[i-1] + list_a[len(list_a)-1]
                    break
            check = False
            for i in range(1,len(list_a)-1):
                if list_a[i] == list_a[i-1]:
                    check = True
                elif list_a[i] != list_a[i-1]:
                    check = False 
                    break
    
            if check == True:
                print("Yes")
            elif check == False:
                print("No")
    
    
            self.T = self.T - 1
T = input()
c = Canbangchanban(T=T)
c.handle()