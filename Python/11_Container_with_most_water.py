class MostWater:
    def __init__(self, heights):
        """
        initial method to save list of heights
        :param heights: list of int values which represent height of `area box's sides`
        """
        assert type(heights) == list, "Wrong type of data"
        for h in heights:
            assert type(h) == int, "Wrong type of data"
        self.heights = heights

    def calculate_area(self):
        """
        Function that calculate max area of water which can be 'store' between some heights
        :return:
        """
        max_area = 0  # our start maximum area of water should be 0
        left_pointer = 0 # we just declare pointers to know on which index we are in `heights` list
        right_pointer = len(self.heights) - 1

        while left_pointer < right_pointer:
            # main caluculus, we check which area of water is larger -> our saved max_area or area of water between
            # heights for each pointer
            max_area = max(max_area, min(self.heights[left_pointer],
                                         self.heights[right_pointer]) * (right_pointer - left_pointer))

            # when we done our max_are calculus, we can check to which pointer should go inwards, to have at least
            # larger area of water -> right(left pointer +1) or left (right pointer -1)
            if self.heights[left_pointer] < self.heights[right_pointer]:
                left_pointer += 1
            else:
                right_pointer -= 1

        return max_area
