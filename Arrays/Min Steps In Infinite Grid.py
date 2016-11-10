class Solution:
    # @param X : list of integers
    # @param Y : list of integers
    # Points are represented by (X[i], Y[i])
    # @return an integer
    def coverPoints(self, X, Y):
        if len(X) <= 1 or len(Y) <= 1: return 0

        self.start = (X[0], Y[0])
        ps = zip(X[1::], Y[1::])
        del X, Y

        seq = map(self.distance, ps)
        return reduce(lambda f, g: f + g, seq)


    def distance(self, val):
        r = max(abs(val[0] - self.start[0]), abs(val[1] - self.start[1]))
        self.start = val
        return r