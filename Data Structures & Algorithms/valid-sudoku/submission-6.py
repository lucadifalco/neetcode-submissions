class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        hash_set = set()
    
        #rows
        for i in range(9):
            for j in range(9):
                value = board[i][j]
                if value in hash_set:
                    return False
                if value != ".":
                    hash_set.add(value)
            hash_set.clear()



        #columns
        for i in range(9):
            for j in range(9):
                value = board[j][i]
                if value in hash_set:
                    return False
                if value != ".":
                    hash_set.add(value)
            hash_set.clear()

        #sub-box
        #0,0 0,1 0,2   1,0 1,1 1,2   2,0 2,1 2,2
        #0,3 0,4 0,5   1,3 1,4 1,5   2,3 2,4 2,5
        #

        #3,0 3,1 3,2   4,0
        for k in range(3):
            for l in range(3):
                for i in range(3):
                    for j in range(3):
                        value = board[i+(k*3)][j+(l*3)]
                        if value in hash_set:
                            return False
                        if value != ".":
                            hash_set.add(value)
                hash_set.clear()
        
        return True


    