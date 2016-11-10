class Solution:
    # @param A : list of integers
    # @return a list of integers
    def maxset(self, A):
        A = list(split(A))

        sum = reduce(lambda l, m: l if l[0] > m[0] else m, A)
        first_item = A[0]
        sum = first_item if sum[0] == first_item[0] and len(sum[1]) < len(first_item[1]) else sum
        return sum[1]


def split(l):
    c = []
    for i in l + [-1]:
        if i >= 0:
            c.append(i)
        else:
            yield sum(c), c
            c = []