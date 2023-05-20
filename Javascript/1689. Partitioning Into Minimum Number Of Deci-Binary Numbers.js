const minPartitions = (n) => {
    const strN = n.toString().split("").map(Number);
    let max = 0;
    strN.map((val) => {
        if (val >= max) {
            max = val;
        }
    });
    return max;
};

console.log(minPartitions(12323));
