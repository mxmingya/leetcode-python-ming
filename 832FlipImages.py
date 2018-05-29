class Solution(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        def flip(arr):
            l = len(arr)
            for i in range(int(math.ceil(l/2))):
                temp = arr[i]
                arr[i] = arr[l-i-1]
                arr[l-i-1] = temp
            return map(lambda n: 1-n, arr)
        for i in range(len(A)):
            A[i] = flip(A[i])
            
        return A