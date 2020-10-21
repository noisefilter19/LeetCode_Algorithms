class ProductOfNumbers:

    def __init__(self):
        self.arr=[1]
        self.mul=1

    def add(self, num: int) -> None:
        if num == 0:
            self.mul=1
            self.arr=[1]
        else:
            self.mul*=num
            self.arr.append(self.mul)

    def getProduct(self, k: int) -> int:
        l=len(self.arr)-1 # -1 is because I add more 1 to the list at the beggining
        if k>l:
            return 0
        else:
            return (self.mul//self.arr[l-k])


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)
