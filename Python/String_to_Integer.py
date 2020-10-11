class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        length = len(str)
        alpha = 'abcdefghijklmnopqrstuvwxyz'
        num = '1234567890'
        Signal = 0  # positive and negative record mark
        Answer = ''  # Number storage
        Num_exists = 0  # There is a number in the record string
        for i in range(length):
            if str[i] == ' ':
                continue
                # The first non-space character is the letter
                if str[i] in alpha and Num_exists == 0:
                    return 0
            if str[i] in alpha and Num_exists == 1:
                return int(Answer)
            if str[i] == '-' and i < length-1 and str[i+1] in num:
                Signal = 1  # record negative number
                continue
            if str[i] in num:
                Answer = Answer+str[i]
                num_exists = 1

        if Num_exists == 1 and Signal == 0:
            return int(Answer)
        elif Num_exists == 1 and Signal == 1:
            return -int(Answer)
        else:
            return 0
