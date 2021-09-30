# Problem link: https://leetcode.com/problems/3sum/

class Solution():
    def three_sum(input_list):
        input_list.sort()
        result = []
        
        for i in range(len(input_list)):
            j = i + 1
            k = len(input_list) -1 
            if ((i > 0) and (input_list[i] == input_list[i-1])):
                continue
        
            while (j < k):
                if ((j-1 > i) and (input_list[j] == input_list[j-1])):
                        j += 1
                        print("2",i,j,k)
                        continue

                if (input_list[i]+input_list[j]+input_list[k] > 0):
                    k -= 1
                elif (input_list[i]+input_list[j]+input_list[k] < 0):
                    j += 1
                else:
                    temp =[]
                    temp.append(input_list[i])
                    temp.append(input_list[j])
                    temp.append(input_list[k])
                    result.append(temp)
                    j += 1
                    k -= 1
        
        return result

