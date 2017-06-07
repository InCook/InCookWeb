/*
$(".card-image img").hover(
    function() {
        $(this).removeClass('card-image-hover-none');
    }, function() {
        $(this).addClass('card-image-hover-none');
    }
);
*/

// Initialize modal
$(document).ready(function(){
    $('.modal').modal();
});

// Modal
$('.card-image').click(function() {
    var id = $(this).attr('id');

    $.get('/recipe', {'recipe_id': id}, function(data) {
        if (data['success']) {
            $('#detail-name').html(data['output']['name']);
            $('#detail-author').html(data['output']['author']);
            $('#detail-thumbnail').attr('src', '/static/recipe/img/'+data['output']['thumbnail']);
            $('#detail-ingredients > .modal-subcontent').html(data['output']['ingredients'].toString().replaceAll(',', ', '));
            $('#detail-direction > .modal-subcontent').html(data['output']['direction'].replaceAll('\n', '<br>'));

            var no_likes = data['output']['like_num']
            if (data['output']['like']) {
                $('.modal-footer>a.like').html('<i class="material-icons">favorite</i>'+no_likes);
                $('.modal-footer>a.like').addClass('like-red');
            }
            else {
                $('.modal-footer>a.like').html('<i class="material-icons">favorite_border</i>'+no_likes);
                $('.modal-footer>a.like').removeClass('like-red');
            }
            $('.modal-footer>a.like').attr({'id': 'like-'+id})

            if (data['output']['bookmark']) {
                $('.modal-footer>a.bookmark').html('<i class="material-icons">bookmark</i>SAVE');
                $('.modal-footer>a.bookmark').addClass('bookmark-blue');
            }
            else {
                $('.modal-footer>a.bookmark').html('<i class="material-icons">bookmark_border</i>SAVE');
                $('.modal-footer>a.bookmark').removeClass('bookmark-blue');
            }
            $('.modal-footer>a.bookmark').attr({'id': 'bookmark-'+id})

            $('#detail-modal').modal('open');
        }
        else 
            alert("Error");
    })
});
