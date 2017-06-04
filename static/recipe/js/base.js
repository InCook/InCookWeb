// Like
$(document).delegate('.like', "click", function(){
  var id = $(this).attr('id').split('-')[1];

  $.get('/like', { 'recipe_id': id }, function (data) {
    if (data['success']) {
        var no_likes = data['output']['like_num'];
        if (data['output']['like']) {
          $('#like-'+id).html('<i class="material-icons like-red">favorite</i>'+no_likes);
          $('#like-'+id).addClass('like-red');
          Materialize.toast('I like it!', 3000);
        }
        else {
          $('#like-'+id).html('<i class="material-icons">favorite_border</i>'+no_likes);
          $('#like-'+id).removeClass('like-red');
        }
    }
    else {
      alert("Error");
    }
  });
});

// add
$("#add").click(function(){
    alert('asdf');
});

// side-nav
$(".button-collapse").sideNav();