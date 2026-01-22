var singleNumber = function(nums) {
    let result = 0;

    for (let i = 0; i < 32; i++) {
        let count = 0;

        for (let num of nums) {
            if ((num >> i) & 1) {
                count++;
            }
        }

        if (count % 3 !== 0) {
            result |= (1 << i);
        }
    }

    return result;
};
