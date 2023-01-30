
// Create a function that will assemble a pizza object based upon given parameters: crust, sauce, cheese, toppings
function pizzaOven(crust, sauce, cheese, toppings) {
    
    // Create a variable to hold the pizza
    var pizza = {};
    
    // Connect the parameters with key pair of pizza object
    pizza.crust = crust;
    pizza.sauce = sauce;
    pizza.cheese = cheese;
    pizza.toppings = toppings;

    // Return pizza object
    return pizza;
};

// Create a function that will assemble a random pizza based on Math.random() randomizer..
function randomPizza() {

    // Create a variable to hold the pizza
    var random_pizza = {};

    // Create arrays for the toppings
    var crust_types = ["flat_bread", "hand_tossed", "panned", "deep_dish"];
    var sauce_types = ["marinara", "traditional", "white", "oil"];
    var cheese_types = ["feta", "mozzarella", "pepper_jack", "chedder"];
    var toppings_types = ["pepperoni", "sausage", "onions", "olives","mushrooms", "tomatos", "green_peppers"];

    // Get Math.min of the toppings arrays to get smallest length to prevent indexing error
    var smallest_length = Math.min(crust_types.length, sauce_types.length, cheese_types.length, toppings_types.length)

    // Generate a Pseudo-random number
    var rand_num = Math.floor(Math.random() * smallest_length)

    //Create a random number based upon the length of 
    random_pizza.crust = crust_types[rand_num];
    random_pizza.sauce = sauce_types[rand_num];
    random_pizza.cheese = cheese_types[rand_num];
    random_pizza.toppings = toppings_types[rand_num];

    return random_pizza;
}

// Create 2 pizzas a instructed and 2 as desired
var s1 = pizzaOven("deep_dish", "traditional", ["mozzarella"], ["pepperoni","sausage"]);
var s2 = pizzaOven("hand_tossed", "marinara", ["mozzarella", "feta"], ["mushrooms","olives", "onions"]);
var s3 = pizzaOven("flat_bread", "oil", ["feta"], ["tomatos","onions", "green_peppers"]);
var s4 = pizzaOven("panned", "traditional", ["mozzarella"], ["pepperoni","sausage"]);
var random_1 = randomPizza()
var random_2 = randomPizza()

// Create array of pizzas to iterate through
var list_pizzas = [s1, s2, s3, s4, random_1, random_2]

for (var i=0; i<list_pizzas.length; i++) {
    console.log(list_pizzas[i]);
};


