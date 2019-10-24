/*document.onkeydown = function (e) {
        if(e.keyCode==116 || e.keyCode==82 || e.keyCode==70){
        return false;
        }
}*/
window.onbeforeunload = function () {
    alert("cant reload");
    return false;
}