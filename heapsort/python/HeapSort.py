'''
Created on Mar 10, 2016

@author: Edielson
'''

class HeapSort(object):
    '''
    classdocs
    '''
    __heapSize = 0
    __Heap = []
    
    def __init__(self):
        '''
        Constructor
        '''
    def __DecrementHeapSize(self):
        self.__heapSize=self.__heapSize-1
    
    def __MaxHeapify(self,i): 
        
        l=self.__Left(i)
        r=self.__Right(i)

        if((l <= self.GetHeapSize()-1) and (self.GetItem(l) > self.GetItem(i))): 
            maior=l 
        else:  
            maior=i 
        
        if((r<=self.GetHeapSize()-1) and (self.GetItem(r) > self.GetItem(maior))): 
            maior=r 
          
        if (maior!=i): 
            aux = self.GetItem(i) 
            self.SetItem(i, self.GetItem(maior))
            self.SetItem(maior, aux) 
            self.__MaxHeapify(maior) 
    
    def __BuildMaxHeap(self,A):
        
        self.__Heap = A
        self.__heapSize = len(A)
        
        #for must go from (Size A)/2 to 0 (inclusive), so in Python must be -1. Index starts in 0 so the last position is (Size A -1)
        for i in range((len(A)-1)/2, -1, -1):   
            self.__MaxHeapify(i) 
    
    def __CleanHeap(self):
        self.__heapSize = 0
        self.__Heap=[]
    
    def __Parent(self,i):
        return (i-1)/2
    
    def __Left(self,i):
        return 2*i+1
    
    def __Right(self,i):
        return 2*i+2
    
    def GetItem(self,i):
        return self.__Heap[i]
    
    def SetItem(self,i,value):
        self.__Heap[i] = value
     
    def GetHeapSize(self):
        return self.__heapSize
    
    def GetHeap(self):
        return self.__Heap
    
    def Sort(self, A): 
        
        self.__BuildMaxHeap(A)
        if self.GetHeapSize() > 0:
        
            #for must go from HeapSize to 1 (inclusive), so in Python must be 0
            for i in range (self.GetHeapSize()-1, 0, -1): 
                aux=self.GetItem(0) 
                self.SetItem(0, self.GetItem(i)) 
                self.SetItem(i, aux) 
                self.__DecrementHeapSize() 
                self.__MaxHeapify(0)
        return A    