class Solution(object):
    def compareVersion(self, version1, version2):
        min = len(version1.split(".")) if len(version1.split(".")) < len(version2.split(".")) else len(version2.split("."))
        for i in range(min):
            if int(version1.split(".")[i]) != int(version2.split(".")[i]):
                return version1 if int(version1.split(".")[i]) > int(version2.split(".")[i]) else version2

sol = Solution()
version1 = "1.23.3.2.14.87"
version2 = "1.23.3.02.14.88"
print(sol.compareVersion(version1,version2));