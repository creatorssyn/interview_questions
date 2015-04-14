$(document).ready(function() {
    $.ajax({
        url: 'data.json',
        type: 'get',
        dataType: 'json',
        success: function(data) {
            $.each(data, function(i, row) {
                $('table tbody').append('<tr><td>'+row.id+'</td><td>'+row.name+'</td><td>'+row.description+'</td></tr>');
            });
        }
    });
});