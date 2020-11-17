/*

  The distribution of the elements is period.
  P   A   H   N
  A P L S I I G
  Y   I   R
  For example, the following has 4 periods(cycles):
  P   | A   | H   | N
  A P | L S | I I | G
  Y   | I   | R   |
  
  The size of every period is defined as "cycle"
  cycle = (2*nRows - 2), except nRows == 1.
  
  In this example, (2*nRows - 2) = 4.
  In every period, every row has 2 elements, except the first row and the last row.
  Suppose the current row is i, the index of the first element is j:
  j = i + cycle*k, k = 0, 1, 2, ...
  
  The index of the second element is secondJ:
  secondJ = (j - i) + cycle - i
  (j-i) is the start of current period, (j-i) + cycle is the start of next period.
  
I HOPE U GOT THE LOGIC 
HAPPY CODING HACTOBER FEST 2020 

*/



char * convert(char * s, int numRows){
    char m[1000][500] = { { s[0] } };
    int j = 0;
    for (int k = 1 ; s[k - 1] && s[k] && numRows > 1 ;) {
        for (int i = 1 ; i < numRows && s[k] ; m[i++][j] = s[k++]);
        for (int i = numRows - 2 ; i >= 0 && s[k] ; m[i--][++j] = s[k++]);
    }
    for (int i = 0, r = 0 ; s[r] && numRows > 1 && i < numRows ; i++)
        for (int k = 0; k <= j ; m[i][k++] ? s[r++] = m[i][k - 1] : 0);
    return s;
}
