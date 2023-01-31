var clickAmount = 0;

function increase() {
    var like_button = document.querySelector("#like_count")
    clickAmount++;
    like_button.innerText = clickAmount + " likes(s)";
}