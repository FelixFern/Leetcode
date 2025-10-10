/**
 * @param {number[]} nums
 * @return {number}
 */
var removeDuplicates = function (nums) {
  let slot_pointer = 0;
  let running_pointer = 0;
  let curr = nums[running_pointer];
  let count = 0;

  while (running_pointer < nums.length) {
    nums[slot_pointer] = nums[running_pointer];

    if (curr === nums[running_pointer]) {
      count++;
    } else {
      count = 1;
      curr = nums[running_pointer];
    }

    if (count > 2) {
      running_pointer++;
    } else {
      running_pointer++;
      slot_pointer++;
    }
  }
  nums.length = slot_pointer;
};
