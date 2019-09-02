$(document).ready(function () {
    $('form').on('submit', function (event) {
        $.ajax({
            data: {
                name: $('#nameInput').val(),
                email: $('#emailInput').val(),
            },
            type: 'POST',
            url: '/ajax_test_calc'
        }).done(function (data) {
            if (data.error) {
                $('#errorAlert').text(data.error).show();
                $('#successAlert').hide();
            } else {
                $('#errorAlert').hide();
                $('#successAlert').text(data.name).show();
            }
        });
        event.preventDefault();
    });
});