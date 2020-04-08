$(document).ready(function () {
    $("#file").change(function(e){
        var filename = e.target.files[0].name;
        console.log(`The file ${filename} has been selected`);
    })
});