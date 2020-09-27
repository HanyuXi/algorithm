class HeapMaxHanyu():

    def __init__(self):
        self.size = 0
        self.heap = []
    
    def push(self, val):
        ##Add to the end then bubble up the item 
       
        self.heap.append(val)
        self.size = self.size +1
        if len(self.heap) > 1:
            self.bubbleup()
        return

    def bubbleup(self):
        ##The main algortihm here is : if the new appended val is less than parent val, then swap parent index with curr_index
        curr_index = self.size-1
        parent_index = curr_index - 1
        while(curr_index > 0 and self.heap[curr_index] > self.heap[parent_index]):
            temp = self.heap[parent_index]
            self.heap[parent_index] = self.heap[curr_index]
            self.heap[curr_index] = temp
            #reset index and parent index
            curr_index = parent_index
            parent_index = (curr_index -1) // 2
        return 
    def pop(self):
        """
        Place the last element to TOP then perform bubble down operation
        """
        if len(self.heap) == 0:
            return "The size of heap is zero"
        if len(self.heap) == 1:
            self.heap = []
            return self.heap[0]
        value = self.heap.pop(0)
        self.size-=1
        
        #Move the last element to first
        self.heap = [self.heap[-1]] + self.heap[:-1]
        self.bubbledown()
        return value

    def bubbledown(self):
        self.heap = [self.heap[-1]] + self.heap[:-1]
        index= 0
        #print(self.isvalidparents())
        while(index < self.size and not self.isvalidparents(index)):
            #Swap the node with larger Children
            tempindex = self.largerChildren(index)        
            temp = self.heap[tempindex]
            self.heap[tempindex] = self.heap[index]
            self.heap[index] = temp
            index = tempindex
        return 


    def largerChildren(self, index):
        if not self.hasleftchild(index):
            return index
        if not self.hasrightchild(index):
            return self.leftchildindex(index)
        if self.leftchild(index) > self.rightchild(index):
            return self.leftchildindex(index)
        else:
            return self.rightchildindex(index) 
       
    def isvalidparents(self, index):
        """
        Check if the current index is a valid parent
        return->Boolean
        """
        if (not self.hasleftchild(index)):
            return True
        isValid = self.heap[index] >=self.leftchild(index) 
        if (not self.hasrightchild(index)):
            return isValid and self.heap[index] >= self.rightchild 

    def hasrightchild(self, index):
   
        return self.leftchildindex(index) <self.size
    def hasleftchild(self, index):
        return self.rightchildindex(index) <self.size
    def leftchildindex(self, index):
        return 2*index +1
    def rightchildindex(self, index):
        return 2*index +2
    def rightchild(self, index):
        return self.heap[self.rightchildindex(index)]
    def leftchild(self, index):
        return self.heap[self.leftchildindex(index)]

            
            


if __name__ == "__main__":
    print("Start here")
    instance = HeapMaxHanyu()
    instance.push(10)
    instance.push(5)
    instance.push(17)
    instance.push(4)
    instance.push(22)
    instance.push(27)
    instance.push(10)
    print(instance.heap)
    instance.pop()
    print(instance.heap)
    instance.pop()
    print(instance.heap)
    print("Done")
