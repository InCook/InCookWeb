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
            $('#detail-modal > .modal-content > h4').html(data['output']['name']);
            $('#detail-modal > .modal-content > p').html(data['output']['direction']);
            $('#detail-modal').modal('open');
        }
        else 
            alert("Error");
    })
});
