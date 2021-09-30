# https://leetcode.com/problems/letter-combinations-of-a-phone-number/


class Solution:
    class Node:
        def __init__(self, val=None, nextNode=None):
            self.val = val
            self.nextNode = nextNode

    def constructMappings(self):
        letterZ = self.Node("z")
        letterY = self.Node("y", letterZ)
        letterX = self.Node("x", letterY)
        letterW = self.Node("w", letterX)
        letterV = self.Node("v")
        letterU = self.Node("u", letterV)
        letterT = self.Node("t", letterU)
        letterS = self.Node("s")
        letterR = self.Node("r", letterS)
        letterQ = self.Node("q", letterR)
        letterP = self.Node("p", letterQ)
        letterO = self.Node("o")
        letterN = self.Node("n", letterO)
        letterM = self.Node("m", letterN)
        letterL = self.Node("l")
        letterK = self.Node("k", letterL)
        letterJ = self.Node("j", letterK)
        letterI = self.Node("i")
        letterH = self.Node("h", letterI)
        letterG = self.Node("g", letterH)
        letterF = self.Node("f")
        letterE = self.Node("e", letterF)
        letterD = self.Node("d", letterE)
        letterC = self.Node("c")
        letterB = self.Node("b", letterC)
        letterA = self.Node("a", letterB)

        numberDict = dict()
        numberDict["2"] = letterA
        numberDict["3"] = letterD
        numberDict["4"] = letterG
        numberDict["5"] = letterJ
        numberDict["6"] = letterM
        numberDict["7"] = letterP
        numberDict["8"] = letterT
        numberDict["9"] = letterW

        return numberDict

    def getCombinations(
        self, currentIndex: int, digitNodes: List[Node], accumulatedString: str
    ):
        if currentIndex is len(digitNodes):
            self.answer.append(accumulatedString)
            return

        combinations = []
        currentNode = digitNodes[currentIndex]
        while currentNode is not None:

            self.getCombinations(
                currentIndex + 1, digitNodes, accumulatedString + currentNode.val
            )
            currentNode = currentNode.nextNode

        return

    def letterCombinations(self, digits: str) -> List[str]:

        self.answer = []
        numberDict = self.constructMappings()

        if len(digits) is 0:
            return []

        digitNodes = list()
        for index in range(0, len(digits)):
            digitNodes.append(numberDict[digits[index]])

        self.getCombinations(0, digitNodes, "")
        return self.answer
