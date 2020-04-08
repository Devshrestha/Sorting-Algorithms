from graphic import outer


class sort:
    
    def bubble_sort(self,l):
        self.the_list=l
        for _ in range(len(self.the_list)-1):   
            for i in range(1,len(self.the_list)):
                if self.the_list[i-1]>self.the_list[i]:
                    temp=self.the_list[i-1]
                    self.the_list[i-1]=self.the_list[i]
                    self.the_list[i]=temp
                outer(self.the_list,[i-1,i])
        return self.the_list
    
    def merge_sort(self,array):
        self.the_list=array
        if len(self.the_list)>1:
            mid = len(self.the_list)//2
            L=self.the_list[:mid]
            R=self.the_list[mid:]
            self.merge_sort(L)
            self.merge_sort(R)
            i=j=k=0
            while i<len(L) and j<len(R):
                if L[i]<R[j]:
                    self.the_list[k]=L[i]
                    k+=1
                    i+=1
                    display_loop(self.the_list,[k,i])
                else:
                    self.the_list[k]=R[j]
                    k+=1
                    j+=1
                    display_loop(self.the_list,[k,j])
                
            while i<len(L):
                self.the_list[k]=L[i]
                k+=1
                i+=1
                display_loop(self.the_list,[k,i])

            while j<len(R):
                self.the_list[k]=R[j]
                k+=1
                j+=1
                display_loop(self.the_list,[k,j])

