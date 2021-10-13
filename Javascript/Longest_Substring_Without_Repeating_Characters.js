// Problem Link: https://leetcode.com/problems/longest-substring-without-repeating-characters/

// Time Complexity - O(n)
// Space Complexity - O(n)

const lengthOfSubstring = (s) => {
  //Return the length of string if it is less than or equal to 1
  //as that would be the longest count
  if (s.length <= 1) return s.length;

  //Init values
  //map - To keep track of chars we have seen
  //left - To keep track of beginning of substring
  //right - counter for our loop
  //maxLength - maxSubstring Length
  let map = {},
    left = 0,
    right = 0,
    maxLength = 0;

  //Go through loop till we get to end of string
  while (right < s.length) {
    //Get the value of the current character from the map
    let currentIndex = map[s[right]];

    //If it exists and is within our current substring
    //set the left value to the character immediately after it
    if (currentIndex !== undefined && currentIndex >= left) {
      left = map[s[right]] + 1;
    }

    //Set value of character in map to its latest index
    map[s[right]] = right;

    //Set maxLength to the greater value between itself and the length of the current substring
    maxLength = Math.max(maxLength, right - left + 1);

    //Increase counter
    right++;
  }
  return maxLength;
};
