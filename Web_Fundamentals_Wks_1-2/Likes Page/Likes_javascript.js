var clickAmount_neil = 0;
var clickAmount_nichole = 0;
var clickAmount_jim = 0;

function increase_neil(id) {
    var like_button = document.querySelector("#" + id)
    clickAmount_neil++;
    like_button.innerText = clickAmount_neil + " likes(s)";
}

function increase_nichole(id) {
    var like_button = document.querySelector("#" + id)
    clickAmount_nichole++;
    like_button.innerText = clickAmount_nichole + " likes(s)";
}

function increase_jim(id) {
    var like_button = document.querySelector("#" + id)
    clickAmount_jim++;
    like_button.innerText = clickAmount_jim + " likes(s)";
}
