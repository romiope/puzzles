class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def threeSumClosest(self, A, B):
        n = len(A)
        if n < 3:
            return sum(A)

        A = sorted(A)
        first = 0
        best_sum = sum(A[:3])

        while first <= n - 3:
            second = first + 1
            third = n - 1
            while second < third < n:
                su = A[first] + A[second] + A[third]
                if abs(B - best_sum) > abs(B - su):
                    best_sum = su
                if su < B:
                    second += 1
                else:
                    third -= 1

            first += 1
        return best_sum
