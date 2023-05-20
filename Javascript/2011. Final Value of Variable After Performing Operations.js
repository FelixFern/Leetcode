var finalValueAfterOperations = function (operations) {
    let temp = 0;
    operations.map((val) => {
        if (val[0] === "+" || val[2] === "+") {
            temp++;
        } else {
            temp--;
        }
    });
    return temp;
};
