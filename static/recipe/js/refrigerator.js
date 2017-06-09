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

    $('#preloader').show();
    $.get('/search', {'ingredients': like_ingres, 'noingredients': hate_ingres}, function(data) {
        $('#preloader').hide();
        $('#recipes').html(data);
        $('.grid').masonry({
            itemSelector: '.grid-item',
            columnWidth: 300,
            gutter: 20,
            fitWidth: true
        });
        $('.modal').modal();

        var recipe_cnt = $(".grid").data('cnt');
        $('#sidenav-recipes').html(recipe_cnt);
    });

    var like_ingre_cnt = $('input[type=checkbox].like-ingre:checked').length;
    $('#sidenav-ingres').html(like_ingre_cnt);
});