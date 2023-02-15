// let stack = []
// stack.push()
// stack.pop()

const str1 = "Y(3(p)p(3)r)s";
const expected1 = true;

const str2 = "N(0(p)3";
const expected2 = false;
// Explanation: not every parenthesis is closed.

const str3 = "N(0)t ) 0(k";
const expected3 = false;
// Explanation: because the second ")" is premature: there is nothing open for it to close.

const str4 = "a(b))(c";
const expected4 = false;
// Explanation: same number of opens and closes but the 2nd closing closes nothing.

/**
 * Determines whether the parenthesis in the given string are valid.
 * Each opening parenthesis must have exactly one closing parenthesis.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str
 * @returns {boolean} Whether the parenthesis are valid.
 */

// "Y(3(p)p(3)r)s"
// "N(0(p)3"

function parensValid(str) {
    
    let stack = []

    for (var i=0; i<str.length;i++) {
        if (str[i] == '(') {
            stack.push(str[i]);
            console.log(stack)
        } else if (str[i] == ')' && stack.length == 0) {
            return false
        } else if (str[i] == ')') {
            stack.pop();
            console.log(stack);
        } 
    }

    if (stack.length > 0) {
        console.log(stack)
        return false
    }

    return true
}

console.log(parensValid(str4))