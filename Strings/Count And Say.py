class Solution:
    # @param A : integer
    # @return a strings
    def countAndSay(self, A):
        def inc_string(st):
            if st == "":
                return ""

            l = len(st)
            res = ""

            counter = 0
            current = ""

            pointer = 0
            while True:

                if current == "":
                    current = st[pointer]
                    counter = 1
                elif current != st[pointer]:
                    res += str(counter) + current
                    current = st[pointer]
                    counter = 1
                elif current == st[pointer]:
                    counter += 1

                pointer += 1

                if pointer == l:
                    res += str(counter) + current
                    break
            return res

        r = "1"
        for i in xrange(A-1):
            r = inc_string(r)
        return r
