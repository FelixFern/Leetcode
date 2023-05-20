var numJewelsInStones = function (jewels, stones) {
    const jewelsArr = jewels.split("");
    const hash = {};
    for (let i = 0; i < stones.length; i++) {
        if (!hash[stones[i]]) {
            hash[stones[i]] = 0;
        }
        hash[stones[i]] += 1;
    }

    let jewel = 0;
    jewelsArr.map((val) => {
        jewel += hash[val] ?? 0;
    });

    return jewel;
};

numJewelsInStones((jewels = "aA"), (stones = "aAAbbbb"));
