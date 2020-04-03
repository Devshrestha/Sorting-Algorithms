from graphic import *

a=[300,-10,6,-15,8,-200]*2
#a=[5,57,23,22,67,43,12,34,10,5]*2
class sort:
    def __init__(self,l):
        self.the_list=l

    def bubble_sort(self):

        for _ in range(len(self.the_list)-1):   
            for i in range(1,len(self.the_list)):
                if self.the_list[i-1]>self.the_list[i]:
                    temp=self.the_list[i-1]
                    self.the_list[i-1]=self.the_list[i]
                    self.the_list[i]=temp
                display_loop(self.the_list,[i-1,i])
        return self.the_list

do=sort(a)
print(do.bubble_sort())