// An anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
// typically using all the original letters exactly once.
// Is there a quick way to determine if they aren't an anagram before spending more time?
// Given two strings
// return whether or not they are anagrams


const strA1 = "yes";
const strB1 = "eys";
const expected1 = true;

const strA2 = "yes";
const strB2 = "eYs";
const expected2 = true;

const strA3 = "no";
const strB3 = "noo";
const expected3 = false;

const strA4 = "silent";
const strB4 = "listen";
const expected4 = true;

/**
* Determines whether s1 and s2 are anagrams of each other.
* Anagrams have all the same letters but in different orders.
* - Time: O(?).
* - Space: O(?).
* @param {string} s1
* @param {string} s2
* @returns {boolean} Whether s1 and s2 are anagrams.
*/

function isAnagram(str1, str2) {
    // Convert strings to lowercase and remove non-letter characters
    str1 = str1.toLowerCase();
    str2 = str2.toLowerCase();

    // Create dictionary object
    const dict = {};

    // Loop through first string and add each character to dictionary
    for (let i = 0; i < str1.length; i++) {
        if (dict[str1[i]] === undefined) {
            dict[str1[i]] = 1;
        } else {
            dict[str1[i]]++;
        }
    }

    // Loop through second string and decrement dictionary values
    for (let i = 0; i < str2.length; i++) {
        if (dict[str2[i]] === undefined) {
            dict[str2[i]] = -1;
        } else {
            dict[str2[i]]--;
        }
    }

    console.log(dict)

    // Check if all dictionary values are 0
    for (const key in dict) {
        if (dict[key] !== 0) {
            return false;
        }
    }

    return true;
}

console.log(isAnagram(strA4, strB4))