// The Story: We want an app that once it measures a kid's height, can display //
// whether the child is tall enough to ride the rollercoaster. //
// We're tasked with building the function that will display the right message to the child. //

// The Task: Build a function that will display the right message to the child. //

// The Code: //


// Step 1: a variable called childHeight that is a number. Give it any whole, positive number you like. //
var childHeight = 45

// Step 2: Create a function called displayIfChildIsAbleToRideTheRollerCoaster//
function displayIfChildIsAbleToRideTheRollerCoaster(height) {

    // Step 3: Inside the function, create the following conditional //
    var message;

    if (height > 52) {
        message = "Get on that ride, kiddo!";
    } else {
        message = "Sorry kiddo. Maybe next year.";
    }
    
    console.log(message);
}

displayIfChildIsAbleToRideTheRollerCoaster(childHeight)

