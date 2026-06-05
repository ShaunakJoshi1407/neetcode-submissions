class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda t : t[1])

        min_heap = [] # pait of [end, numPassengers]
        curr_pass = 0

        for num, start, end in trips:
            while min_heap and min_heap[0][0] <= start:
                _, num_pass = heapq.heappop(min_heap)
                curr_pass -= num_pass
            
            curr_pass += num
            if curr_pass > capacity:
                return False
            
            heapq.heappush(min_heap, ([end, num]))
        
        return True

