#User function Template for python3

class Solution: 

    def selectionSort(self, arr,n):
        for i in range(len(arr)):
            minI = i
            for j in range(i+1, len(arr)):
                if arr[minI] > arr[j]:
                    minI = j
            arr[i], arr[minI] = arr[minI], arr[i]
        return arr

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        Solution().selectionSort(arr, n)
        for i in range(n):
            print(arr[i],end=" ")
        print()
# } Driver Code Ends