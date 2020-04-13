from graphic import outer,exit
#a=[23,-45,75,68,91,56,-67,34,90,100,104,198,9]


class sort:
    def __init__(self,l):
        self.the_list=l
        self.represent=l
    
    def bubble_sort(self):
        for _ in range(len(self.the_list)-1):   
            for i in range(1,len(self.the_list)):
                if self.the_list[i-1]>self.the_list[i]:
                    temp=self.the_list[i-1]
                    self.the_list[i-1]=self.the_list[i]
                    self.the_list[i]=temp
                outer(self.the_list,[i-1,i])
        exit()
        return self.the_list
    
    def merge_sort(self,array):
        the_list=array
        if len(the_list)>1:
            mid = len(the_list)//2
            L=the_list[:mid]
            R=the_list[mid:]
            self.merge_sort(L)
            self.merge_sort(R)
            i=j=k=0
            while i<len(L) and j<len(R):
                if L[i]<R[j]:
                    the_list[k]=L[i]
                    self.represent[k]=L[i]
                    k+=1
                    i+=1
                    outer(self.represent,[k,i])
                    
                else:
                    the_list[k]=R[j]
                    self.represent[k]=R[j]
                    k+=1
                    j+=1
                    outer(self.represent,[k,j])

                    
                
            while i<len(L):
                the_list[k]=L[i]
                self.represent[k]=L[i]
                k+=1
                i+=1
                outer(self.represent,[k,i])
                

            while j<len(R):
                the_list[k]=R[j]
                self.represent[k]=R[j]
                k+=1
                j+=1
                outer(self.represent,[k,j])
        
    def selection(self):
        for i in range(len(self.the_list)):
            min_inx=i
            for j in range(i+1,len(self.the_list)):
                if self.the_list[min_inx]>self.the_list[j]:
                    min_inx=j
            
            self.the_list[min_inx],self.the_list[i]=self.the_list[i],self.the_list[min_inx]
            outer(self.the_list,(min_inx,i))
        return self.the_list     

    def insertion(self):

        for i in range(1,len(self.the_list)):

            key=self.the_list[i]
            j=i-1
            
            while key<self.the_list[j] and j>=0:
                self.the_list[j+1]=self.the_list[j]
                outer(self.the_list,(key,j))
                j-=1
            self.the_list[j+1]=key
            
        return self.the_list