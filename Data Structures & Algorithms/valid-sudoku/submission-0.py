class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        # Iterate through every element, to be valid it must pass these conditions

        def check_elem(element: str, x:int, y:int, seen:dict):

            # seen[elem] is not none, will look like [(1,2), (3,4)]

            for coordinate in seen[element]:

                if coordinate[0] == x: # No elem in row
                    return False

                if coordinate[1] == y: # No elem in column
                    return False

                if ((((x // 3) * 3) <= coordinate[0] <= (((x // 3) * 3) + 2)) and (((y // 3) * 3) <= coordinate[1] <= (((y // 3) * 3) + 2))): # No elem in grid
                    print('herro')
                    return False

            return True 

        seen = {}

        for y in range(len(board)):
            for x in range(len(board[y])):
                
                if board[y][x] != '.':

                    if board[y][x] not in seen:
                        seen[board[y][x]] = [(x, y)]

                    else:
                        # Validate rules

                        if check_elem(board[y][x], x, y, seen):
                            seen[board[y][x]].append((x, y))

                        else:
                            return False

        return True 