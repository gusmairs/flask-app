add_name = function(n, a) {
    $.ajax({
        url: '/add',
        contentType: 'application/json',
        method: 'POST',
        data: JSON.stringify({'name': n, 'age': parseInt(a)}),
        success: function(resp) {
            $('#tbl').html(resp['table'])
        }
    })
}

$(document).ready(function() {
    $.ajax({
        url: '/show',
        contentType: 'application/json',
        method: 'GET',
        success: function(resp) {
            $('#tbl').html(resp['table'])
            $('#name').focus()
        }
    })
    $('#age').on('keypress', function(e){
        if(e.which == 13) {
            add_name($('#name').val(),
                     $('#age').val())
            $('#age').val('')
            $('#name').val('').focus()
        }
    })
})
