function remove_cookie_mes() {
    var element_to_remove = document.getElementById("remove_cookie");
    element_to_remove.remove();
};

function conversion_fah(temp) {
    var conversion = ((temp * 9/5) + 32).toPrecision(2)
    return conversion;
}

function conversion_cel(temp) {
    var conversion = ((temp - 32) * 5/9).toPrecision(2)
    return conversion;
}

function changeTemp() {

    var temp_change = document.getElementById("select_temps");

    var temps_array = document.querySelectorAll(".temp_low, .temp_high");

    for (var temp of temps_array) {
        if (temp_change.value == "Fahrenheit") {
            temp.innerText = conversion_fah(temp.innerText)
        } else if (temp_change.value == "Celsius") {
            temp.innerText = conversion_cel(temp.innerText)
        }
    }
}