

class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        
        if len(mat)*len(mat[0]) != r*c:
            return mat

        values = []

        for row in mat:
            for value in row:
                values.append(value)
        
        result = [[0]*c for _ in range(r)]

        for i in range(r):
            for j in range(c):
                result[i][j] = values.pop(0)
        
        return result
        