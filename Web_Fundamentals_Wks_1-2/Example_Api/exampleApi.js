var pokemon_choice = 0
var pokemon_data;

const initializeGame = async () => {
    var response = await fetch(`https://pokeapi.co/api/v2/pokemon/${}`); // add id here
    pokemon_data = await response.json();

    // console.log(pokemon_data.results[pokemon_choice].name);
    // document.getElementById('inner_container').innerText = pokemon_data.results[pokemon_choice].name

    document.getElementById('start_image').src = `https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-i/red-blue/back/gray/${}.png`; // add id here

    // https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-i/red-blue/back/gray/1.png
};

function getPokemonImg_Correct() {

    // Get input from text box

    // Compare it to the name pokemon_data.name

    // If correct, add balloons in background / else if incorrect, show a frown face

    // Change the Icon to front by getElementById
    //https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/1

    // Change the name of Pokemon

    // Change the Start button to Play Again
}



