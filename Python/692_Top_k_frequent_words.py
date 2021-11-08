class FreqWords:

    def __init__(self, words, k):
        """
        Initial function with assertions
        :param words: list of words
        :param k: (int) given amount of most frequent elements in list
        """
        assert type(words) == list, "Wrong type of data"
        assert type(k) == int, "Wrong type of data"
        assert k <= len(self.get_unique_elements(words)), "Too big `k` argument"
        for w in words:
            assert type(w) == str, "Wrong type of data"

        self.words = words
        self.k = k

    def get_top_freq_words(self):
        """
        Function to get top `k` frequent elements from list
        :return: list of `k` elements
        """
        # in first step, we just sort our dictionary of word -> amount(in list) to a list of tuples(word,
        # amount) sorted by amounts
        desc_sorted_map_elements = sorted(self.map_elements_of_list().items(),
                                          key=lambda item: item[1],
                                          reverse=True)
        top_elements = []
        for i in range(self.k):
            top_elements.append(desc_sorted_map_elements[i][0])  # we get only `k` first elements from sorted list

        return top_elements

    def map_elements_of_list(self):
        """
        Method to get dictionary with key -> element from list, value -> replicates of given element in list
        :param given_list: list of elements
        :return: (dict) of reduce elements
        """
        map_elements = {}
        for unique_element in self.get_unique_elements(self.words):
            map_elements[unique_element] = self.words.count(unique_element)
        return map_elements

    @staticmethod
    def get_unique_elements(given_list):
        """
        Simple static method to get unique elements from list
        :param given_list: list of given elements
        :return: unique list based on given list
        """
        unique_list = []
        for element in given_list:
            if element not in unique_list:
                unique_list.append(element)

        return unique_list
