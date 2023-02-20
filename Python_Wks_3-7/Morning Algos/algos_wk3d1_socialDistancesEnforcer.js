// Given an array of ints representing a line of people where the space between
// indexes is 1 foot, with 0 meaning no one is there and 1 meaning someone is in
// that space,
// return whether or not there is at least 6 feet separating every person.
// Bonus: O(n) linear time (avoid nested loops that cause re-visiting indexes).


const queue1 = [0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1];
const expected1 = false;

const queue2 = [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1];
const expected2 = true;

const queue3 = [1, 0, 0, 0, 0, 0, 0, 0, 1];
const expected3 = true;

const queue4 = [];
const expected4 = true;

/**
 * Determines whether each occupied space in the line of people is separated by
 * 6 empty spaces.
 * - Time: O(?).
 * - Space: O(?).
 * @param {Array<0|1>} queue
 * @returns {Boolean}
 */

function socialDistancingEnforcer(queue) {

    var counter = 6;

    for (var i=0;i<queue.length;i++) {
        // console.log(queue[i])

        if (queue[i] == 0) {
            counter++;
        } else {
            if (counter < 6) {
                return false;
            }
            counter = 0;
        }

    }

    return true
}

console.log(socialDistancingEnforcer(queue2))


function sixFeetApart(arr) {
    let lastPersonIndex = -1;
    for (let i = 0; i < arr.length; i++) {
        if (arr[i] === 1) {
            if (lastPersonIndex !== -1 && i - lastPersonIndex < 6) {
                return false;
            }
            lastPersonIndex = i;
        }
    }
    return true;
}

console.log(sixFeetApart(queue2))