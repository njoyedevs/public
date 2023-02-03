var characterData;
var characterName
var homeWorldData;
var homeWorldNum;
var homeWorldLink;
var homeWorld;
var gameStart = false;
var homeWorldVar = "";
var againButton = document.querySelector("#button");

const initializeGame = async () => {

    // Get random number for character
    const random_num = Math.ceil(Math.random() * 82);
    //console.log(random_num);

    // Fetch Character
    var response_1 = await fetch(`https://swapi.dev/api/people/${random_num}/`);
    characterData = await response_1.json();
    console.log(characterData);

    // Get Character name
    characterName = characterData.name;
    //console.log(characterName);

    // Update Character name in Div
    const question = document.querySelector(".character_name");
    question.innerText = `What is the\n home world of:\n ${characterName}?`;

    // Get Home World Link and Splice for Home World Number
    homeWorldLink = characterData.homeworld;

    const string = homeWorldLink.substring(homeWorldLink.length - 3);

    const newString = string.replace('/', '');

    // Parce Home World Number String into Integer
    homeWorldNum = parseInt(newString);
    //console.log(homeWorldNum);

    // Get Home World Data
    var response_2 = await fetch(`https://swapi.dev/api/planets/${homeWorldNum}/`);
    homeWorldData = await response_2.json();
    console.log(homeWorldData);

    // Get Home World Name
    homeWorld = homeWorldData.name;
    //console.log(homeWorld);

    // Update Text Box Placeholder
    document.getElementById("input").placeholder = "Enter Home World Here";

    // Update gameStart variable to True
    gameStart = true;
    //console.log(gameStart);
};

function clear() {
    //console.log(clear);
    console.log("Cleared");

    // Update Placeholder to Guide Player
    homeWorldVar.innerText = "";
    document.getElementById("input").value = "";
    document.getElementById("input").placeholder = "Enter Home World Here";
    againButton.innerText = "Check Answer";
};

function remove() {
    console.log("Removed");

    // Remove the Message Box
    const element_to_remove = document.getElementsByClassName("remove_message_box");
    element_to_remove[0].remove(); 
};

function play() {

    remove();

    // Add the question box
    const element = document.querySelector('.text_box');
    element.style.border = ".21rem solid rgb(42, 4, 85)";
    element.style.background = 'rgb(49, 4, 231)';
    element.style.backgroundImage = 'linear-gradient(to right, rgb(0, 0, 0), #480a94 20% 40%, rgb(103, 40, 205), #480a94, rgb(20, 9, 39))';

    initializeGame();
};

function checkAnswers() {

    // Check if the game was finshed and if so, then start over.
    if (gameStart == false) {

        // Console.log Start Over
        console.log("Start Over");

        // Clear Data
        clear();

        // Repopulate Data
        initializeGame();

        // If not finished, then check the answers and set the game to finished.
    } else {

        // Get Player Answer
        const playerAnswer = document.getElementById("input").value.trim();

        // Check For Validity
        console.log("This players' answer was: " + playerAnswer);
        console.log("This correct home world is: " + homeWorld);

        // Update Home World Box
        homeWorldVar = document.querySelector(".homeworld");

        // Check Answers
        homeWorldVar.innerText = homeWorld == playerAnswer?`Correct!\n${homeWorld}!`:`Incorrect!\nPlay Again!`;
        
        // Update the main button
        againButton.innerText = "Play Again!";

        // Change Validation Variable
        gameStart = false;
    };
};
