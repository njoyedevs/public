const str1 = "creature";
const expected1 = "erutaerc";

const str2 = "dog";
const expected2 = "god";

const str3 = "hello";
const expected3 = "olleh";

const str4 = "";
const expected4 = "";

function reverseString(str) {

    var new_string = "";

    // Time O(N)
    // Space O(N)
    for (var i=str.length-1; i>=0; i--) {
        new_string += str[i];
    }

    return new_string;
};

console.log(reverseString(str1));