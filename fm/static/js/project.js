function checkProjectForm() {
    i=0;
    pform = document.getElementById("project_form");
    if (pform.pro_name.value == "") {
        i = 1;
        document.getElementById("pro_name_error").innerHTML = "pro_name error";
    }
    if (pform.pro_lots.value == "") {
        i = 1;
        document.getElementById("pro_lots_error").innerHTML = "pro_lots error";
    }
    if (pform.pro_qty.value == "") {
        i = 1;
        document.getElementById("pro_qty_error").innerHTML = "pro_qty error";
    }
    if (pform.pro_duedate == "") {
        i = 1;
        document.getElementById("pro_duedate_error").innerHTML = "pro_duedate error";
    }
    if(i == 1) {
        return false;
    }
    pform.action="laser.html";
}