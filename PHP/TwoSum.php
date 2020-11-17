//The Two Sum problem in PHP

<?php
function twoSum($numbers, $sum) {
  for ($i = 0; $i < count($numbers); $i++) {
    for ($j = $i + 1; $j < count($numbers); $j++) {
      if ($numbers[$j] + $numbers[$i] === $sum) {
        return [$i, $j];
      }
    }
  }
}


print_r(twoSum([-2, 7, 11, 15], 5)); // [0, 1]
