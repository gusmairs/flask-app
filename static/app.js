add_name = function(n, a) {
    $.ajax({
        url: '/add',
        contentType: 'application/json',
        method: 'POST',
        data: JSON.stringify({'name': n, 'age': parseInt(a)}),
        success: function(resp) {
            $('#tbl').html(resp['table'])
            $('#name').focus()
        }
    })
}

get_detail = function(i) {
    $.ajax({
        url: '/detail',
        contentType: 'application/json',
        method: 'POST',
        data: JSON.stringify({'id': i}),
        success: function(resp) {
            $('#click').show();
            $('#detail').text(resp['name'])
            $('#name').focus()
        }
    })
}

$().ready(function() {
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
            add_name(
                $('#name').val(),
                $('#age').val()
            )
            $('#age').val('')
            $('#name').val('').focus()
        }
    })

    $('#tbl').on('click', '.dataframe tr', function(){
        id = $(this).find('td:nth-child(1)').text()
        get_detail(id)
    })
})
