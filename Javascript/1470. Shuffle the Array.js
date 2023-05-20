var shuffle = (nums, n) => {
    const temp = [];
    for (let i = 0; i < n; i++) {
        temp.push(nums[i]);
        temp.push(nums[i + n]);
    }
    return temp;
};

console.log(shuffle([2, 5, 1, 3, 4, 7], 3));
