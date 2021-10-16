//
// Link: https://leetcode.com/problems/rotate-image/
//
// 48. Rotate Image
//
// You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
//
// You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

func rotate(matrix [][]int) {

	n := len(matrix)

	for i := range matrix {
		for j := i; j < n; j++ {
			temp := matrix[i][j]
			matrix[i][j] = matrix[j][i]
			matrix[j][i] = temp
		}
	}

	for i := range matrix {
		for j := 0; j < (n / 2); j++ {
			temp := matrix[i][j]
			matrix[i][j] = matrix[i][n-j-1]
			matrix[i][n-j-1] = temp
		}
	}
}
