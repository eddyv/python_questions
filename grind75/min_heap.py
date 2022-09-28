# `heap[i//2]` - parent
# `heap[i]` - current element
# `heap[i*2]` - left child of current element
# `heap[(i*2)+1]` - right child of current element
class Heap:
    def __init__(self):
        self.heap = [0]

    def push(self, val):
        # add to the end of the array (we need to keep the tree balanced / complete)
        self.heap.append(val)
        curr_index = len(self.heap) - 1
        parent = curr_index // 2

        # perform swaps with parent node O(logn)
        while self.heap[curr_index] < self.heap[parent]:
            tmp = self.heap[curr_index]
            self.heap[curr_index] = self.heap[parent]
            self.heap[parent] = tmp
            curr_index = curr_index // 2
            parent = curr_index // 2

    def pop(self):
        # if the heap is empty, return none as there is nothing to pop
        if len(self.heap) == 1:
            return None
        elif len(self.heap) == 2:
            # only one element so we can just pop it and call it a day
            return self.heap.pop()
        else:
            result = self.heap[1]
            # move the last node to the root
            self.heap[1] = self.heap.pop()
            curr_index = 1
            left_child = 2 * curr_index
            right_child = 2 * curr_index + 1
            # traverse all the way down the tree.
            while left_child < len(self.heap):
                # if we have a right child, check if the right child is smaller than the left node and
                # that its smaller than the node we are sending down
                if right_child < len(self.heap) and \
                        self.heap[right_child] < self.heap[left_child] and \
                        self.heap[curr_index] > self.heap[right_child]:
                    tmp = self.heap[curr_index]
                    self.heap[curr_index] = self.heap[right_child]
                    self.heap[right_child] = tmp
                    curr_index = right_child
                    left_child = 2 * curr_index
                    right_child = 2 * curr_index + 1
                # if the left child is smaller than the node we are sending down
                elif self.heap[curr_index] > self.heap[left_child]:
                    tmp = self.heap[curr_index]
                    self.heap[curr_index] = self.heap[left_child]
                    self.heap[left_child] = tmp
                    curr_index = left_child
                    left_child = 2 * curr_index
                    right_child = 2 * curr_index + 1
                # everything's kosher, lets go home
                else:
                    break
            return result

    def top(self):
        pass

    def heapify(self, arr):
        # send the 0th position to the end
        arr.append(arr[0])
        self.heap = arr
        cur = (len(self.heap) - 1) // 2
        # starting from the middle of the array (a.k.a not a leaf node)
        while cur > 0:
            i = cur

            while 2 * i < len(self.heap):
                # if we have a right child, check if the right child is smaller than the left node and
                # that its smaller than the node we are sending down
                if (2 * i + 1 < len(self.heap) and
                        self.heap[2 * i + 1] < self.heap[2 * i] and
                        self.heap[i] > self.heap[2 * i + 1]):
                    # swap to retain minheap property
                    tmp = self.heap[i]
                    self.heap[i] = self.heap[2 * i + 1]
                    self.heap[2 * i + 1] = tmp
                    i = 2 * i + 1
                elif self.heap[i] > self.heap[2 * i]:
                    tmp = self.heap[i]
                    self.heap[i] = self.heap[2 * i]
                    self.heap[2 * i] = tmp
                    i = 2 * i
                else:
                    break
            cur -= 1


if __name__ == '__main__':
    arr = [10, 80, 30, 40, 20, 50, 60, 70]
    heap = Heap()
    heap.heapify(arr)
    while len(heap.heap) > 1:
        print(heap.pop())
