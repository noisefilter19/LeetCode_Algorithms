char* convert(char* s, int numRows) {
    int len=0;
    char *tmp=s;
    //strore length of string in len 
    //while(*tmp++ != '\0') len++;
    for(;s[len]!='\0';len++);
   
   //judge special condition , only one row or length of string less than rows 
    if(numRows ==1 || numRows>= len)
        return s;
    int zigsize = numRows*2 -2;
	//
    char *s2 = (char*)malloc(sizeof(char)*(len+1));
    char *s1 =s2;
    for(int i=0;i<numRows;i++){
        int base  = i;
        
        while(base < len){
            // 处理所有不在对角线上的
			*s1++ = *(s+base);
			// 处理对角线上元素
			//
            if(i>0 && i<numRows-1){
                int t = base + zigsize - 2*i;
                if(t< len)
                    *s1++ = *(s+t);
            }
			//每次加上一个折线步长
            base  = base + zigsize;
        }
    }
    *s1++ = '\0';
    return s2;
}
