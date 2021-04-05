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
        if (location.href.split("/").slice(-1) != "login") {
            window.location.replace("/login")
        }
    } else {
        //console.log(token);
        if (location.href.split("/").slice(-1) == "login") {
            window.location.replace("/admin")
        }
    }




});

function openForm() {
    //console.log("Hiển thị");
    document.getElementById("nhanphong").style.display = "block";
    topFunction();
}

function closeForm() {
    //console.log("Đóng Hiển thị");
    document.getElementById("nhanphong").style.display = "none";
}

// * Kiểu phòng
function openKieuPhong() {
    //console.log("Hiển thị");
    document.getElementById("kieuphong").style.display = "block";
}

function closeKieuPhong() {
    //console.log("Đóng Hiển thị");
    document.getElementById("kieuphong").style.display = "none";
}

function openThemKieuPhong() {
    //console.log("Hiển thị");
    document.getElementById("themkieuphong").style.display = "block";
    document.getElementById("suakieuphong").style.display = "none";
}

function closeThemKieuPhong() {
    //console.log("Đóng Hiển thị");
    document.getElementById("themkieuphong").style.display = "none";
}

function openSuaKieuPhong(id, name, description, number_adult, number_children) {

    topFunction()

    document.getElementById("suakieuphong").style.display = "block";
    document.getElementById("themkieuphong").style.display = "none";

    document.getElementsByName("idroom")[0].value = id;
    document.getElementsByName("suanameroom")[0].value = name;
    document.getElementsByName("suanumbera")[0].value = number_adult;
    document.getElementsByName("suanumberc")[0].value = number_children;
    document.getElementsByName("suadescription")[0].value = description;

    //console.log(document.getElementsByName("suanameroom")[0].value);
}

function closeSuaKieuPhong() {
    //console.log("Đóng Hiển thị");
    document.getElementById("suakieuphong").style.display = "none";
}
// todo : giá phòng
function openCapNhatGia(id, name) {

    topFunction()

    document.getElementById("capnhatgia").style.display = "block";
    document.getElementById("themkieuphong").style.display = "none";
    document.getElementById("suakieuphong").style.display = "none";

    get_gia(id);
    //document.getElementsByName("idroom")[0].value = id;
    //document.getElementsByName("giaphong")[0].value = name;

}

function closeCapNhatGia() {
    //console.log("Đóng Hiển thị");
    document.getElementById("capnhatgia").style.display = "none";
}

function get_gia(id) {

    $.ajax({
        url: '/getpricebyid',
        type: 'POST',
        data: JSON.stringify(id),
        contentType: 'application/json;charset=UTF-8',
        xhrFields: {
            withCredentials: true
        },

        success: function (response) {
            console.log(response[0][0]);
            console.log(response[0][5]);
            console.log(response[0][6]);

            document.getElementById("idroom").value = response[0][0];
            document.getElementById("idgiagio").value = response[0][5];
            document.getElementById("idgiangay").value = response[0][6];
        }
    })
}

function onchangegiagio() {
    var checkBox = document.getElementById("giagio");

    if (checkBox.checked == true) {
        document.getElementById("listgio").style.visibility = "visible";
        document.getElementById("buttonaddgiagio").style.visibility = "visible";

    } else {
        document.getElementById("listgio").style.visibility = "hidden";
        document.getElementById("buttonaddgiagio").style.visibility = "hidden";


        // 1 : while ( el.firstChild ) el.removeChild( el.firstChild );
        // 2 :
        document.getElementById('listgio').textContent = '';

    }
}

function addgiagio(parent, children) {

    var khung = document.getElementById(children).cloneNode(true);
    khung.id = null;
    document.getElementById(parent).appendChild(khung);
}

function deleteGrandParent(element) {
    element.remove();
}

function onchangegiangay() {
    var checkBox = document.getElementById("giangay");

    if (checkBox.checked == true) {
        document.getElementById("listngay").style.visibility = "visible";
        
    } else {
        document.getElementById("listngay").style.visibility = "hidden";
        document.getElementById("giangiosom").checked = false;
        document.getElementById("giangiotre").checked = false;
        onchangenhanphongsom();
        onchangetraphongtre() ;
    }
}

function onchangenhanphongsom() {
    var checkBox = document.getElementById("giangiosom");

    if (checkBox.checked == true) {
        document.getElementById("listngaynhanphongsom").style.visibility = "visible";
        document.getElementById("buttonaddgianhanphongsom").style.visibility = "visible";
    } else {
        document.getElementById("listngaynhanphongsom").style.visibility = "hidden";
        document.getElementById("buttonaddgianhanphongsom").style.visibility = "hidden";
        
        document.getElementById("listngaynhanphongsom").textContent = '';

    }
}

function onchangetraphongtre() {
    var checkBox = document.getElementById("giangiotre");

    if (checkBox.checked == true) {
        document.getElementById("listngaytraphongtre").style.visibility = "visible";
        document.getElementById("buttonaddgiatraphongtre").style.visibility = "visible";

    } else {
        document.getElementById("listngaytraphongtre").style.visibility = "hidden";
        document.getElementById("buttonaddgiatraphongtre").style.visibility = "hidden";

        document.getElementById('listngaytraphongtre').textContent = '';
    }
}




// * Tầng
function openTang() {
    //console.log("Hiển thị");
    document.getElementById("tang").style.display = "block";
    document.getElementById("suatang").style.display = "none";
}

function closeTang() {
    //console.log("Đóng Hiển thị");
    document.getElementById("tang").style.display = "none";
}

function openThemTang() {
    //console.log("Hiển thị");
    document.getElementById("themtang").style.display = "block";

    document.getElementById("suatang").style.display = "none";
}

function closeThemTang() {
    //console.log("Đóng Hiển thị");
    document.getElementById("themtang").style.display = "none";
}


function openSuaTang(id, name, description) {
    topFunction()

    document.getElementById("suatang").style.display = "block";
    document.getElementById("themtang").style.display = "none";

    document.getElementsByName("idroom")[0].value = id;
    document.getElementsByName("suanametang")[0].value = name;
    document.getElementsByName("suadescription")[0].value = description;


}

function closeSuaTang() {
    //console.log("Đóng Hiển thị");
    document.getElementById("suatang").style.display = "none";
}


// * Phòng
function openPhong() {
    //console.log("Hiển thị");
    document.getElementById("phong").style.display = "block";
}

function closePhong() {
    //console.log("Đóng Hiển thị");
    document.getElementById("phong").style.display = "none";
}

function openThemPhong() {
    //console.log("Hiển thị");
    document.getElementById("themphong").style.display = "block";

    document.getElementById("suaphong").style.display = "none";
}

function closeThemPhong() {
    //console.log("Đóng Hiển thị");
    document.getElementById("themphong").style.display = "none";
}


function openSuaPhong(id, name, description, room_type, room_level) {

    topFunction()

    document.getElementById("suaphong").style.display = "block";
    document.getElementById("themphong").style.display = "none";

    document.getElementsByName("idroom")[0].value = id;
    document.getElementsByName("suanamephong")[0].value = name;
    document.getElementsByName("suadescription")[0].value = description;
    document.getElementsByName("suaselectkieuphong")[0].value = room_type;
    document.getElementsByName("suaselecttang")[0].value = room_level;



}

function closeSuaPhong() {
    //console.log("Đóng Hiển thị");
    document.getElementById("suaphong").style.display = "none";
}

function topFunction() {
    document.body.scrollTop = 0;
    document.documentElement.scrollTop = 0;
}
