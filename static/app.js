add_name = function(n, a) {
    $.ajax({
        url: '/add',
        contentType: 'application/json',
        method: 'POST',
        data: JSON.stringify({'name': n, 'age': a}),
        success: function(resp) {
            console.log('got it')
            location.reload()
            // $('#table_loc' ).load(resp)
        }
    })
}

$(document).ready(function() {
    $('#age').on('keypress', function(e){
        if(e.which == 13) {
            add_name($('#name').val(),
                     $('#age').val())
        }
    })
})
