class TimeMap:

    # We can build this data structure as a hashmap, where the key is the key, and the value is
    # a sorted list, sorted on the time 

    # Insertions are strictly in increasing order so we can just add to list

    # To retrieve we can binary search the list that exists at that key (bias right elemenent as more recent)

    ### TEST RUN ###

    # self.time_map = {
    # 'alice' = [('happy', 1)]
    # }

    def __init__(self):
        self.time_map = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.time_map:
            self.time_map[key] = [(value, timestamp)]
        else:
            self.time_map[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:

        if key not in self.time_map:
            return ""
        
        ### BINARY SEARCH ###
        arr = self.time_map[key]

        l = 0
        r = len(arr) - 1
        res = ""

        while l <= r:

            middle = (l + r) // 2

            if arr[middle][1] <= timestamp:
                l = middle + 1
                res = arr[middle][0]
            elif arr[middle][1] > timestamp:
                r = middle - 1

        return res
