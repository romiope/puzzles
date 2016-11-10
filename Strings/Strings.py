class Solution:
    # @param A : list of strings
    # @param B : integer
    # @return a list of strings
    def fullJustify(self, A, B):
        if not A:
            return ""
        r = []
        line = []
        while A:
            line.append(A.pop(0))
            if not A:
                r.append(justifySlots(line, B, True))
            elif lenWithMinSlots(line) <= B < lenWithMinSlots(line + [A[0]]):
                r.append(justifySlots(line, B))
                line = []
        return r


def lenWithMinSlots(line):
    return len(" ".join(line))


def justifySlots(line, b, last=False):
    words = len(line)
    gaps_pool = b - len("".join(line))
    gaps_groups = words - 1

    if len(line) == 1:
        return line[0] + " " * gaps_pool

    if last:
        return " ".join(line) + " " * (gaps_pool - gaps_groups)

    generated_gaps = {}
    for i in xrange(gaps_pool):
        generated_gaps[i % gaps_groups] = generated_gaps.get(i % gaps_groups, "") + " "

    res = ""
    for index, item in enumerate(line):
        res += item
        if index in generated_gaps.keys():
            res += generated_gaps[index]

    return res