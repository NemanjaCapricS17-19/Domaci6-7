$(document).ready(function () {
    $("#unos").on("keyup", function () {
        var value = $(this).val().toLowerCase();
        $("#raspored tr").filter(function () {
            $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
        });
    });
    $(".info").click(function () {
        var value = $(this).html().toLowerCase();
        $("#unos").val(value);
        $("#raspored tr").filter(function () {
            $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
        });
    });
});