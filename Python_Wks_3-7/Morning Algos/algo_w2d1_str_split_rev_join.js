var str3 = "abc def ghi"

function reverseString(str) {
    var strArray = str.split(" ")
    var reverseString = []
    for (var i=0; i<strArray.length; i++) {
        var word = strArray[i];
        var reverserWord = ""
        for (var j=word.length-1;j>=0; j--) {
            reverserWord += word[j]
        }
        reverseString.push(reverserWord)
    }
    return reverseString.join(" ")
}

console.log(reverseString(str3))

function reverseString_1(str) {
    var reversedStr = str.split(" ");
    var newArray = []
    for (var i=0; i<reversedStr.length; i++) {
        var word = reversedStr[i]
        var reverseWord = word.split("").reverse().join("");
        newArray.push(reverseWord)
    }
    var newString = newArray.join(" ")
    return newString
}
console.log(reverseString_1(str3))
