function remove_mes() {
    var element_to_remove = document.getElementsByClassName("remove_message_box");
    element_to_remove[0].remove();
};

function play() {
    var characterData;
    var characterName
    var homeWorldData;
    var homeWorldNum;
    var homeWorldLink;
    var homeWorld;
    
    const initializeGame = async () => {

        // Add the question box
        const button = document.querySelector('button');
        button.addEventListener('click', () => {
            const element = document.querySelector('.text_box');
            element.style.border = ".21rem solid rgb(42, 4, 85)";
            element.style.background = 'rgb(49, 4, 231)';
            element.style.backgroundImage = 'linear-gradient(to right, rgb(0, 0, 0), #480a94 20% 40%, rgb(103, 40, 205), #480a94, rgb(20, 9, 39))';
        });

        // Get random number for character
        const random_num = Math.ceil(Math.random() * 82);
        console.log(random_num);

        // Fetch Character
        var response_1 = await fetch(`https://swapi.dev/api/people/${random_num}/`);
        characterData = await response_1.json();
        console.log(characterData);
    
        // Get Character name
        characterName = characterData.name;
        console.log(characterName);

        // Update Character name in Div
        const question = document.querySelector(".character_name");
        question.innerText = `What is the\n home world of:\n ${characterName}`;

        // Get Home World Link and Splice for Home World Number
        homeWorldLink = characterData.homeworld;

        console.log(homeWorldLink);
        console.log(homeWorldLink.substring(homeWorldLink.length - 3));

        const string = homeWorldLink.substring(homeWorldLink.length - 3);

        const newString = string.replace('/', '');

        // Parce Home World Number String into Integer
        homeWorldNum = parseInt(newString);
        console.log(homeWorldNum);

        // Get Home World Data
        var response_2 = await fetch(`https://swapi.dev/api/planets/${homeWorldNum}/`);
        homeWorldData = await response_2.json();
        console.log(homeWorldData);

        // Get Home World Name
        homeWorld = homeWorldData.name;
        console.log(homeWorld);

        // Update Button to Say Check Answer
        const again_button = document.querySelector("#button");
        again_button.innerText = `Check Answer`;

        const placeHolderText = document.getElementById("input").placeholder = "Enter Home World Here";
        
        // console.log(data.results[choice].name);
        // document.getElementById('inner_container').innerText = data.results[choice].name
    
        // document.getElementById('change_image').src = `https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-i/red-blue/back/gray/${}.png`; // add id here
    
        // https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-i/red-blue/back/gray/1.png
    };

    initializeGame();

    function checkAnswer() {
    
        // Get input from text box
    
        // Compare it to the name data.name
    
        // If correct, add balloons in background / else if incorrect, show a frown face
    
        // Change the Icon to front by getElementById
        // https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/1
    
        // Change the name of homeland
    
        // Change the Start button to Play Again
    }

    checkAnswer();
}