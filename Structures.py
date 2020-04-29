"""
Class for Min heaps
Takes an input array and automatically builds a min heap structure
Altered for Dijkstra's Algorithm
"""
class min_heap:

    def __init__(self, arr):        #Each element in arr should be a tuple (x,y,value)
        self.heap = [None]          #Initialise empty list (take note index=0 is None)
        self.start = 0              #pointer to the last item in heap, also provides size of heap
        for i in arr:
            self.heap_insert(i)     #Creating the actual heap


    def heap_insert(self, item):
        """
        Method to add new items into the heap. Item will start at the bottom and
        bubble up to the top if needed.
        Since we can maintain a proper tree strcuture like this, this should take
        O(log n) time.
        """
        self.start += 1
        self.heap.append(item)
        self.bubble_up(self.start)


    def bubble_up(self, index):
        """
        Method to maintain heap structure. Since we initialise index=0 as None,
        we ensure that the parent node is index//2, and the child node is index.
        If the child is smaller than the parent, we change places, else we do nothing
        """
        while(index > 1 and self.heap[index][2] < self.heap[index//2][2]):
            self.heap[index],self.heap[index//2] = self.heap[index//2],self.heap[index]
            index = index//2


    def extract_min(self):
        """
        This method removes the smallest number in the heap and returns it to the caller
        It swaps the root with the last element in the heap, and bubbles it down
        """
        if self.start == 0:
            return -1
        self.heap[1], self.heap[self.start] = self.heap[self.start], self.heap[1]
        min_num = self.heap.pop()
        self.start -= 1
        self.bubble_down()
        return min_num


    def bubble_down(self):
        """
        A function to take the root of the heap and bubble it down to its correct position.
        This works together with popping the minimum number in the heap
        """
        parent = 1
        child_left = parent*2
        child_right = (parent*2)+1

        while(True):
            #Checks if both children exists
            if(child_left <= self.start and child_right <= self.start):
                
                #If parent is bigger than both children, swap with the smaller number
                if(self.heap[parent][2] > self.heap[child_left][2] and self.heap[parent][2] > self.heap[child_right][2]):
                    if(self.heap[child_left][2] < self.heap[child_right][2]):
                        self.heap[child_left], self.heap[parent] = self.heap[parent], self.heap[child_left]
                        parent = child_left
                    else:
                        self.heap[child_right], self.heap[parent] = self.heap[parent], self.heap[child_right]
                        parent = child_right

                #If only bigger than left child
                elif(self.heap[parent][2] > self.heap[child_left][2]):
                     self.heap[child_left], self.heap[parent] = self.heap[parent], self.heap[child_left]
                     parent = child_left

                #If only bigger than right child
                elif(self.heap[parent][2] > self.heap[child_right][2]):
                    self.heap[child_right], self.heap[parent] = self.heap[parent], self.heap[child_right]
                    parent = child_right
                
                #If parent is smaller than both children or equal to them
                else:
                    break
                child_left = parent*2
                child_right = parent*2+1

            #Checks if left child is exactly the last index
            elif(child_left == self.start):
                if(self.heap[parent][2]>self.heap[child_left][2]):
                    self.heap[child_left], self.heap[parent] = self.heap[parent], self.heap[child_left]
                break

            #If no children exist, parent will be at a leaf node
            else:
                break


    def find_index(self, node):
        """
        Function to find the index of required node. Made specially for Dijkstra's algorithm
        Input: node: node of interest, (x, y, value)
        Returns: Index of node of interest
        """
        for index in range(1, self.start+1):
            if(self.heap[index][0] == node[0] and self.heap[index][1] == node[1]):
                return index
        return -1   #If node does not exist in heap, we return -1


    def update_heap(self, index, value):
        """
        Function to update the value of a node. Made specially for Dijkstra's algorithm
        Input: index: Index of node of interest
               value: value to be updated
        returns: nothing
        """
        x, y, initial_value = self.heap[index]
        self.heap[index] = (x, y, value)
        self.bubble_up(index)       #We bubble up only because if we update the value, it will be smaller


    def PrintHeap(self):
        print(self.heap[1:])
