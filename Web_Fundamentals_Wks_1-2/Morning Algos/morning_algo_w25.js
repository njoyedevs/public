// Create either If/then or for loop to select integer and then iterate
// through the 3x3 spaces around the integer.

// Locate can be found at from location zero: theDojo[0][X][Y] +1 and -1 from second dimension

// Starting Array
var theDojo = [ [1, 0, 1, 1, 1, 0, 4, 0, 8, 0],
                [3, 1, 0, 7, 0, 0, 6, 0, 8, 8],
                [5, 0, 7, 0, 3, 6, 6, 6, 0, 0],
                [2, 3, 0, 9, 0, 0, 6, 0, 8, 0],
                [6, 0, 3, 3, 0, 2, 0, 3, 0, 4],
                [0, 0, 3, 3, 0, 0, 2, 2, 3, 0],
                [0, 0, 0, 0, 5, 0, 1, 2, 0, 6],
                [2, 2, 2, 2, 0, 7, 1, 1, 1, 0],
                [5, 2, 0, 2, 0, 0, 0, 1, 1, 2],
                [9, 2, 2, 2, 0, 7, 0, 1, 1, 0] ];

// Variable Creation
var random_num_i;
var random_num_j;
var number;
var coordinates = [];
var numbers = [];

// Random Number Generator and Selector
for(var i=0; i<theDojo.length; i++) {
    // console.log(theDojo[i]);
    for(var j=0; j<theDojo[i].length; j++) {
        //console.log(theDojo[i][j]);

        random_num_i = Math.floor(Math.random() * (theDojo.length-1));
        random_num_j = Math.floor(Math.random() * (theDojo[i].length-1));
    }
}

//  Get the location and number
number = theDojo[random_num_i][random_num_j];
// number = theDojo[5][5];
// number_coordinates = [5,5];
console.log(`The location is: ${random_num_i}, ${random_num_j}`);
console.log(`The number is: ${number}`);

// // Get all numbers at those locations 
try {
    var number1 = theDojo[random_num_i-1][random_num_j-1];
}
catch(err) {
    var number1 = undefined;
}
try {
    var number2 = theDojo[random_num_i-1][random_num_j];
}
catch(err) {
    var number2 = undefined;
}
try {
    var number3 = theDojo[random_num_i-1][random_num_j+1];
}
catch(err) {
    var number3 = undefined;
}
try {
    var number4 = theDojo[random_num_i][random_num_j-1];
}
catch(err) {
    var number4 = undefined;
}
try {
    var number6 = theDojo[random_num_i][random_num_j+1];
}
catch(err) {
    var number6 = undefined;
}
try {
    var number7 = theDojo[random_num_i+1][random_num_j-1];
}
catch(err) {
    var number7 = undefined;
}
try {
    var number8 = theDojo[random_num_i+1][random_num_j];
}
catch(err) {
    var number8 = undefined;
}
try {
    var number9 = theDojo[random_num_i+1][random_num_j+1];
}
catch(err) {
    var number9 = undefined;
}

numbers.push(number1,
            number2,
            number3,
            number4,
            number,
            number6,
            number7,
            number8,
            number9);
console.log(numbers);

var sum = 0;

// Sum only integers and skip undefined
for (const element of numbers) {
    if (element !=  undefined) {
        sum += element;
    }
}

console.log(sum);