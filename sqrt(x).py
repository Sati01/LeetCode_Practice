class Solution:
    def mySqrt(self, x: int) -> int:
        #Solution with Pointers and Binary Search
        l, r = 0, x
        res = 0
        while l<= r:
            midd = l + ((r-l) // 2)
            if midd * midd > x:
                r = midd - 1
            elif midd * midd < x:
                l = midd + 1
                res = midd
            else:
                return midd
        return res
        

        