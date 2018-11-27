function showMenu(){
        document.getElementById("menu").style.display = "block";
        document.getElementById("body").style.background = "gray";
}

    function hideMenu() {
        document.getElementById("menu").style.display = "none";
        document.getElementById("body").style.background = "#333333";
        document.getElementById("Email").value = "";
        document.getElementById("pwd").value = "";
    }

    function login() {
        hideMenu();
        document.getElementById("menuList").style.display = "block";
        showMainButtons();
        showPkgLi();
    }

    function logout() {
        userID = "";
        curpkg = "";
        hideMainButtons();
        hidePkgLi();
        $('ul li').remove();
        document.getElementById("ad").style.display = "none";
        showMenu();
    }

    function hideCreateWin(){
        document.getElementById("createWin").style.display = "none";
        document.getElementById("menu").style.display = "block";
        document.getElementById("cname").value = "";
        document.getElementById("cemail").value = "";
        document.getElementById("cpwd").value = "";
        document.getElementById("cphone").value = "";
        document.getElementById("captnum").value = "";
        document.getElementById("cst").value = "";
        document.getElementById("ccity").value = "";
        document.getElementById("cstate").value = "";
        document.getElementById("ccountry").value = "";
        document.getElementById("czip").value = "";
    }

    function createAccountWin() {
        document.getElementById("menu").style.display = "none";
        document.getElementById("createWin").style.display = "block";
    }

    function showMainButtons(){
        document.getElementById("logout").style.display = "block";
        document.getElementById("ad").style.display = "block";
        document.getElementById("MyAccount").style.display = "block";
    }

    function hideMainButtons(){
        document.getElementById("logout").style.display = "none";
        document.getElementById("MyAccount").style.display = "none";
        document.getElementById("ad").style.display = "block";
        showMenu();

    }

    function addLi(package){
        var li = document.createElement("li");
        li.setAttribute("class", "newLi");
        addSpan(li, package);
        li.id = package;
        li.onclick = function () { getUserOnePackage(package) };
        document.getElementById("allPkg").appendChild(li);
    }

    function addSpan(li, package){
        var span = document.createElement("span");
        span.innerHTML = "TrackingID: " + package;
        li.appendChild(span);
    }

    function addPackage(){
        confirm("Are you sure to add a new package?");
        $('ul li').remove();
        getUserAllPackages();
        hideAddPkgWin();
    }



    function showAddPkgWin(){
        document.getElementById("addPkg").style.display = "block";
    }

    function hideAddPkgWin(){
        document.getElementById("addPkg").style.display = "none";
        document.getElementById("receiver").value = "";
        document.getElementById("sender").value = "";
        document.getElementById("pkgType").value = "";
        document.getElementById("pkgWeight").value = "";
        document.getElementById("saptnum").value = "";
        document.getElementById("sst").value = "";
        document.getElementById("scity").value = "";
        document.getElementById("sstate").value = "";
        document.getElementById("scountry").value = "";
        document.getElementById("szip").value = "";
    }



    function hidePkgDetailsWin(){

        document.getElementById("pkgDetails").style.display = "none";

    }

    function deletePackage(){
        if(confirm("Are you sure to delete this package?")) {
            document.getElementById(curpkg).remove();
        }
        hidePkgDetailsWin();
    }

    function showPkgLi(){
        document.getElementById("pkgLi").style.display = "block";
    }

function hidePkgLi(){
    document.getElementById("pkgLi").style.display = "none";
}

function showAccountWin(list){
    document.getElementById("uname").innerHTML = "Name: " + list[1];
    document.getElementById("uemail").innerHTML = "Email: " + list[2];
    document.getElementById("uphone").innerHTML = "Phone Number: " + list[3];
    document.getElementById("uaptnum").innerHTML = "Account Number: " + list[6];
    document.getElementById("ust").innerHTML = "Routing Number: " + list[7];
    document.getElementById("ucity").innerHTML = "Holder Name: " + list[10];
    document.getElementById("ustate").innerHTML = "Card Number: " + list[11];
    document.getElementById("ucountry").innerHTML = "cvv2: " + list[12];
    document.getElementById("uzip").innerHTML = "Expiration Date: " + list[14] + " / " + list[13];
    document.getElementById("profile").style.display = "block";
}

function hideAccountWin(){
    document.getElementById("profile").style.display = "none";
    document.getElementById("Email").innertext = "";
    document.getElementById("pwd").innerText = "";
}

