const str = "aaaabbcddd"
const expected1 = "a4b2c1d3"

const str5 = "aaabbbcccaaa"

const str2 = ""
const expected2 = ""

const str3 = "a"
const expected3 = "a1"

const str4 = "bbcc"
const expected = "bbcc"

function encodeStr(str) {
    let solution = "";
    let count = 1;
    for (var i = 1; i <= str.length; i++) {
        if (str[i] === str[i - 1]) {
            count++;
        } else {
            solution += str[i - 1] + count;
            count = 1;
        }
    }
    // console.log(solution)

    if (solution.length < str.length) {
        console.log(solution);
    } else {
        console.log("The string output is not longer than the origional string");
    }
} 

encodeStr(str);

