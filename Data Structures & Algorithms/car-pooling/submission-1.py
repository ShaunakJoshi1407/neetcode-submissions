class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda x:x[1])

        curr = 0
        minHeap = []

        for num, start, end in trips:
            while minHeap and minHeap[0][0] <= start:
                _ , numpass = heapq.heappop(minHeap)
                curr -= numpass
            
            curr += num
            if curr > capacity:
                return False
            
            heapq.heappush(minHeap, ([end, num]))
        
        return True