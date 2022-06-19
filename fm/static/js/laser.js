function checkLaserForm() {
        i=0
        iform = document.getElementById("laser_form");
        if(iform.laser_mechine.value == "") {
            i=1
            document.getElementById("laser_mechine_error").innerHTML="mechine error";
        }
        if(iform.laser_project.value == "") {
            i=1
            document.getElementById("project_error").innerHTML="project_error";
        }
        if(iform.laser_part_no.value == "") {
            i=1
            document.getElementById("laser_part_no_error").innerHTML="laser_part_no_error";
        }
        if(iform.laser_producer.value == "") {
            i=1
            document.getElementById("laser_producer_error").innerHTML="laser_producer_error";
        }
        if(iform.laser_qty.value == "") {
            i=1
            document.getElementById("laser_qty_error").innerHTML="laser_qty_error";
        }
        if(iform.laser_bad.value == "") {
            i=1
            document.getElementById("laser_bad_error").innerHTML="laser_bad_error";
        }
        if(i==1) {
            return false
        }
}