
// function change_pokemon() {

//     async function getPokemonData() {
//         var response = await fetch("https://pokeapi.co/api/v2/pokemon/")
//         var pokeData = await response.json();
    
//         return pokeData;
//     }

//     var pokemon_data = getPokemonData();

//     console.log(pokemon_data);
// }

// change_pokemon();

// the promise is no longer pending and data is printed
// function loadData() {
//     fetch("https://pokeapi.co/api/v2/pokemon/")
//     .then(r => r.json())
//     .then(data => (data))
// }

async function fetchJSON() {
    const response = await fetch('https://pokeapi.co/api/v2/pokemon/');

    if (!response.ok) {
        const message = `An error has occured: ${response.status}`;
        throw new Error(message);
    }

    const data = await response.json();
    return data;
}

var x = fetchJSON().then(data => {data});

console.log(x)

fetchJSON().catch(error => {
    error.message; // 'An error has occurred: 404'
});
