class Solution:
    def addBinary(self, a: str, b: str) -> str:
        ran = min(len(a),len(b))
        a = a[::-1]
        b = b[::-1]
        res = []
        carry = 0
        i = 0
        while i<ran:
            a1 = a[i]
            b1 = b[i]
            bit = int(a1) + int (b1) + carry
            if bit == 3:
                res.append("1")
            elif bit == 2:
                res.append("0")
                if not carry:
                    carry = 1
            elif bit == 1:
                res.append("1")
                if carry:
                    carry = 0
            elif bit == 0:
                res.append("0")

            i+=1

        if len(a)>len(b):
            ran = len(a)
            temp = a
        else:
            ran = len(b)
            temp = b
        while i < ran:
            t = temp[i]
            bit = int(t) + carry
            if bit == 2:
                res.append("0")
            elif bit == 1:
                res.append("1")
                if carry:
                    carry = 0
            elif bit == 0:
                res.append("0")
            i+=1
        if carry:
            res.append("1")
        res.reverse()
        return ''.join(res)