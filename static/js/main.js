// функция отрисовывающая navbar
function lol() {
    $(document).ready(function () {
        $("nav").toggle(100);
    });
}

this._ = function (arg) {
    var expr = $("sdfdsf").val()
};

$(document).ready(function () {
    $('.header').height($(window).height());

    $(".navbar a").click(function () {
        $("body,html").animate({
            scrollTop: $("#" + $(this).data('value')).offset().top
        }, 1000)
    });
});
