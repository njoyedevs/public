function changeName() {
    var name = document.querySelector("#name_text");
    name.innerText = "Nicolas Joye, DBA PMP";
}

function removeUser(user_id, connection_requests_num=2) {
    var user = document.querySelector("#"+ user_id);
    user.remove();
}


