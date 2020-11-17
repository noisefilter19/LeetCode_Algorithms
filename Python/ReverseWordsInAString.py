def reverseWords(self, s):
        s = s.strip()
        s = s.split(" ")
        s = [x for x in s if x != '']
        return " ".join(s[::-1])
