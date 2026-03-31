class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        cars = [] # [(f1position, f1speed, time_to_targer), (f2position, f2speed, time_to_target)]

        for i in range(len(position)):
            time_to_target = (target - position[i]) / speed[i]
            cars.append((position[i], speed[i], time_to_target))

        # Sort into ascending order of position 

        cars = sorted(cars, key = lambda p: p[0])

        print(cars)
        
        fleet_counter = 0 # 
        last_time = 0 #

        while cars: # [(3, 4, 2), (4, 4, 2), (5, 4, 2), (6, 4, 1), (7, 4, 1), (8, 4, 1)]
            curr = cars.pop() # 

            if curr[2] <= last_time: # 
                continue
            else:
                fleet_counter += 1
                last_time = curr[2] # 

        return fleet_counter

        
