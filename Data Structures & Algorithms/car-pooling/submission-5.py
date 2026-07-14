class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda x:x[1])
        min_heap = []
        curr = 0
        for num, start, end in trips:
            while min_heap and min_heap[0][0] <= start:
                _, num_pass = heapq.heappop(min_heap)
                curr -= num_pass
            
            curr += num
            if curr > capacity:
                return False
            
            heapq.heappush(min_heap, (end, num))
        return True