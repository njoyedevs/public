function remove_cookie_mes() {
    var element_to_remove = document.getElementById("#remove_cookie");
    element_to_remove.remove();
};

function changeTemp() {

    function converstion(temp) {
        var conversion = (temp * 9/5) + 32
        return conversion;
    }

    var temp_change = document.getElementById("#select_temps");

    var r = document.querySelector(':root');

    var rs = getComputedStyle(r);

    root_temp1 = rs.getPropertyValue("--temp1");
    root_temp2 = rs.getPropertyValue("--temp2");
    root_temp3 = rs.getPropertyValue("--temp3");
    root_temp4 = rs.getPropertyValue("--temp4");
    root_temp5 = rs.getPropertyValue("--temp5");
    root_temp6 = rs.getPropertyValue("--temp6");
    root_temp7 = rs.getPropertyValue("--temp7");
    root_temp8 = rs.getPropertyValue("--temp8");

    if (temp_change == "F") {
        temp1.innerText = conversion(root_temp1) + "°";
        temp2.innerText = conversion(root_temp2) + "°";
        temp3.innerText = conversion(root_temp3) + "°";
        temp4.innerText = conversion(root_temp4) + "°";
        temp5.innerText = conversion(root_temp5) + "°";
        temp6.innerText = conversion(root_temp6) + "°";
        temp7.innerText = conversion(root_temp7) + "°";
        temp8.innerText = conversion(root_temp8) + "°";
    };

    if (temp_change == "C") {
        temp1.innerText = root_temp1 + "°";
        temp2.innerText = root_temp2 + "°";
        temp3.innerText = root_temp3 + "°";
        temp4.innerText = root_temp4 + "°";
        temp5.innerText = root_temp5 + "°";
        temp6.innerText = root_temp6 + "°";
        temp7.innerText = root_temp7 + "°";
        temp8.innerText = root_temp8 + "°";
    };
    
}