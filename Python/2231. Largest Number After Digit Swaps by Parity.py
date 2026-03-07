class Solution:
    def largestInteger(self, num: int) -> int:
        res = []
        order = []
        
        even_heap = []
        odd_heap = []

        for i in str(num):
            if(int(i) % 2 == 0):
                order.append("even")
                heappush_max(even_heap, i)
            else: 
                order.append("odd")
                heappush_max(odd_heap, i)

        for i in order:
            if(i == "even"):
                res.append(heappop_max(even_heap))
            else:
                res.append(heappop_max(odd_heap))
            
        return int("".join(res))