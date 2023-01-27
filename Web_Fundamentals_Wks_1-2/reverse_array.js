var arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];

var reverse_arr = [];

// arr.reverse();

// console.log(arr);

function reverse_array_func(array) {
    for (var i=9; i>=0; i--) {
        reverse_arr.push(array[i]);
        
    };

    arr = reverse_arr;

    return arr;
}

console.log(reverse_array_func(arr));
