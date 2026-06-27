class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda x:x[1])

        curr = 0
        min_heap = []

        for num, start, end in trips:
            while min_heap and min_heap[0][0] <= start:
                curr -= heapq.heappop(min_heap)[1]
            
            curr += num
            if curr > capacity:
                return False
            
            heapq.heappush(min_heap, [end, num])
        
        return True