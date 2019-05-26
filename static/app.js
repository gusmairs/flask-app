add_name = function(n, a) {
    $.ajax({
        url: '/add',
        contentType: 'application/json',
        method: 'POST',
        data: JSON.stringify({'name': n, 'age': a}),
        success: function(resp) {

        }
    })
}

$(document).ready(function() {
    $('input#age').on('keypress', function(e){
        if(e.which == 13) {
            add_name($('input#name').val()),
                     $('input#age').val()),
            )
        }
    })
})
