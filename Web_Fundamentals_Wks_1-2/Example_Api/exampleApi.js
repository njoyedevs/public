var characterData;
    var characterName
    var homeWorldData;
    var homeWorldNum;
    var homeWorldLink;
    var homeWorld;
    var gameStart = false;
    var remove = true;
    var correctOrNot = false;
    var clear = false;
    var homeWorldVar;
    //console.log(correctOrNot);
    var againButton = document.querySelector("#button");

function play() {

    if (remove == true) {

        // Remove the Message Box
        var element_to_remove = document.getElementsByClassName("remove_message_box");
        element_to_remove[0].remove(); 

        // Only remove once
        remove = false;
    }

    console.log(clear);

    if (clear == true) {

        console.log(clear);

        // Update Placeholder to Guide Player
        homeWorldVar.innerText = ``;
        document.getElementById("input").value = "";
        document.getElementById("input").placeholder = "Enter Home World Here";
        document.getElementById("button").value = "Check Answer";
    }

    // Add the question box{
    const element = document.querySelector('.text_box');
    element.style.border = ".21rem solid rgb(42, 4, 85)";
    element.style.background = 'rgb(49, 4, 231)';
    element.style.backgroundImage = 'linear-gradient(to right, rgb(0, 0, 0), #480a94 20% 40%, rgb(103, 40, 205), #480a94, rgb(20, 9, 39))';

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

        //console.log(homeWorldLink);
        //console.log(homeWorldLink.substring(homeWorldLink.length - 3));

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

    initializeGame();
};

function checkAnswers() {

    if (gameStart == false) {

        console.log("Winning");

        gameStart = true;
        clear = true;

        play();

    } else {

        // Get Player Answer
        const playerAnswer = document.getElementById("input").value;

        // Check For Validity
        console.log("This is home world: " + homeWorld);
        console.log("This is player: " + playerAnswer);

        // Check Answers
        if (homeWorld == playerAnswer) {
        
            // Change Validation Variable
            correctOrNot = true;
            console.log(correctOrNot);

            // Update Home World Box
            homeWorldVar = document.querySelector(".homeworld");
            homeWorldVar.innerText = `Correct! ${homeWorld}!`;

            againButton.innerText = "Play Again!";

            gameStart = false;

        } else {
            // Change Validation Variable
            correctOrNot = false;
            console.log(correctOrNot)

            // Update Home World Box
            const homeWorldVar = document.querySelector(".homeworld");
            homeWorldVar.innerText = `Incorrect!\nPlay Again!`;

            againButton.innerText = "Play Again!";

            gameStart = false;
        }
    };
};
