// Select ingredient
$('input[type="checkbox"]').click(function() {
    var id = $(this).attr('id').split('-')[2];

    if ($(this).hasClass('like-ingre')) {
        if ($('#hate-ingre-'+id).prop('checked') == true)
            $('#hate-ingre-'+id).prop('checked', false);
    }
     else {
        if ($('#like-ingre-'+id).prop('checked') == true)
            $('#like-ingre-'+id).prop('checked', false);
    }

    like_ingres = '';
    $('input[type=checkbox].like-ingre:checked').each(function() {
        var string = $(this).val() + ",";
        like_ingres += string;
    });
    hate_ingres = '';
    $('input[type=checkbox].hate-ingre:checked').each(function() {
        var string = $(this).val() + ",";
        hate_ingres += string;
    });

    $.get('/search', {'ingredients': like_ingres, 'noingredients': hate_ingres}, function(data) {
        if (data['success']) {
            var recipe_cnt = data['output'].length;
            $('#sidenav-recipes').html(recipe_cnt);
        }
    });

    var like_cnt = $('input[type=checkbox].like-ingre:checked').length;
    $('#sidenav-ingres').html(like_cnt);
});