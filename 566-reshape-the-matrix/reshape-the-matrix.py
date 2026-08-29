class Solution:

    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        import numpy as np

        if len(mat) * len(mat[0]) != r * c:
            return mat

        return np.array(mat).reshape(r, c).tolist()