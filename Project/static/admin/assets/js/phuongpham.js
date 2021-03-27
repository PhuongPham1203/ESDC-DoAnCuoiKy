function getCookie(cname) {
    var name = cname + "=";
    var decodedCookie = decodeURIComponent(document.cookie);
    var ca = decodedCookie.split(';');
    for (var i = 0; i < ca.length; i++) {
        var c = ca[i];
        while (c.charAt(0) == ' ') {
            c = c.substring(1);
        }
        if (c.indexOf(name) == 0) {
            return c.substring(name.length, c.length);
        }
    }
    return null;
}

$(document).ready(function () {
    // your code

    var token = getCookie("token");

    if (token == null) {
        //console.log("no token");
        if(location.href.split("/").slice(-1)!="login"){
            window.location.replace("/login")
        }
    } else {
        //console.log(token);
        if(location.href.split("/").slice(-1)=="login"){
            window.location.replace("/admin")
        }
    }




});

