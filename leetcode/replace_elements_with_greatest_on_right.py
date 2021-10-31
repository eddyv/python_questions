class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        i = len(arr)-1
        greatestElement = -1
        while i >= 0:
            currNum = arr[i]
            arr[i] = greatestElement
            print(f"{currNum}, {greatestElement}")
            if currNum > greatestElement:
                greatestElement = currNum
            i-=1
        return arr