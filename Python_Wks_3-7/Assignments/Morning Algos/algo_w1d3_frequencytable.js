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
    output_string = ""
    obj = {}

    for (var i=0;i<str.length;i++) {
        // console.log(str[i]);
        if (`${str[i]}` in obj) {
            obj[`${str[i]}`]++
        } else {
            obj[`${str[i]}`] = 1
        }
        
    }

    for (var i=0; i<Object.keys(obj).length;i++) {
        output_string += Object.keys(obj)[i]
        output_string += Object.values(obj)[i]
    }

    // console.log(output_string)

    if (output_string.length < str.length) {
        console.log(output_string);
    } else {
        console.log("The string output is not longer than the origional string");
    }
}

encodeStr(str5);

