const str = "Hello World";

const rotateAmnt1 = 0;
const expected1 = "Hello World";

const rotateAmnt2 = 1;
const expected2 = "dHello Worl";

const rotateAmnt3 = 2;
const expected3 = "ldHello Wor";

const rotateAmnt4 = 4;
const expected4 = "orldHello W";

const rotateAmnt5 = 13;
const expected5 = "ldHello Wor";

//BONUS How can we do this 1,000,000 times with out losing speed?


/* 
Explanation: this is 2 more than the length so it ends up being the same
as rotating it 2 characters because after rotating every letter it gets back
to the original position.
*/

/**
 * Rotates a given string's characters to the right by the given amount,
 * wrapping characters to the beginning.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str
 * @param {number} amnt The amount of characters in the given str to rotate to the
 *    right.
 * @returns {string} The string rotated by the given amount.
 */


function rotateString(str, amnt) {
    
    let stringArr = str.split('');

    for (i=0; i<amnt%str.length; i++) {
        let last = stringArr.pop();
        // console.log(last)
        stringArr.unshift(last);
    }

    return stringArr.join('')

}

console.log(rotateString(expected1, 15000000000000000000000000))

function rotateStr(str, amnt) {
    if (amnt < 0) {
        amnt += str.length;
    }
    amnt %= str.length;
    return str.slice(str.length - amnt) + str.slice(0, str.length - amnt);
}


console.log(rotateStr(expected1, 15000000000000000000000000))

function rotateStringBackToFront(str, shifts) {
    // Ensure that shifts is a positive integer
    shifts = Math.abs(Math.floor(shifts)) % str.length;
    // console.log(shifts)

    // Rotate the string by slicing and concatenating
    const rotated = str.slice(str.length - shifts) + str.slice(0, str.length - shifts);
    // console.log(str.slice(str.length - shifts))
    // console.log(str.slice(0, str.length - shifts))

    return rotated;
}

console.log(rotateStringBackToFront(expected1, 15000000000000000000000000))