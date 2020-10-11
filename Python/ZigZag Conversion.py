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

def convert(self, s, numRows):
    if numRows==1:
        return s
	p=2*numRows-2				# notice each down, up segment is made up of numRows+numRows-2 numbers
    zz=""
    n=len(s)
    for i in range(numRows):	# each row starts with the index of the number in the first column
        a=(p-i*2)%p				# step pattern found in examples
        if a==0:				# correction for first and last row
            a=p
            b=p
        else:
            b=(p-a)%p			# corresponding alternating step
        j=i
		stp=True				# keep track of alternating step
        while j<n:
            zz+=s[j]
            if stp:
                j+=a
                stp=not stp
            else:
                j+=b
                stp=not stp
    return zz
