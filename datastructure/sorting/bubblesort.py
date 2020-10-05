class BubbleSort():
    def sort(self, arr):
        for i in range(len(arr)):
            for j in range(i, len(arr),1):
                if arr[j] <arr[i]:
                    temp = arr[j]
                    arr[j] = arr[i]
                    arr[i] = temp
        return arr

if __name__ == "__main__":
    arr = [2,6,7,4,0,10,-6]
    print(arr)
    i = BubbleSort()
    print(i.sort(arr))