class InsertionSort():
    """
    Main logic: arr = sorted+unsorted
    2,4   8 1 3
    pick one from unsorted arry and insert it in the right position
    """
    def sort(self, arr):
        for i in range(len(arr)):
            curr = arr[i]
            j = i-1
            while(j >=0 and arr[j] >curr):
                arr[j+1] = arr[j]
                j-=1
            arr[j+1] = curr
        return arr

if __name__ == "__main__":
    arr = [2,6,7,4,0,10,-6]
    print(arr)
    i = InsertionSort()
    print(i.sort(arr))