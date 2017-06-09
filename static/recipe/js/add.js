// Ingredient - close icon
$('#add-ingredients > i.close').click(function() {
  $('#input-ingredients').val('');
})

/* Ingredient - autocomplete */
$( ".selector" ).autocomplete({
  appendTo: "#input-ingredients"
});
$(function() {
  function split( val ) {
    return val.split( /,\s*/ );
  }
  function extractLast( term ) {
    return split( term ).pop();
  }
  $("#input-ingredients")
    // don't navigate away from the field on tab when selecting an item
    .bind( "keydown", function( event ) {
      if ( event.keyCode === $.ui.keyCode.TAB && $( this ).autocomplete( "instance" ).menu.active ) {
        event.preventDefault();
      }
    })  
    .autocomplete({
      source: function( request, response ) {
        $.getJSON( "/tag/get_tags", {
          term: extractLast( request.term )
        }, response );
      },
      minLength: 1,
      focus: function() {
        // prevent value inserted on focus
        return false;
      },
      select: function( event, ui ) {
        var terms = split( this.value );
        // remove the current input
        terms.pop();
        // add the selected item
        terms.push( ui.item.value );
        // add placeholder to get the comma-and-space at the end
        terms.push( "" );
        this.value = terms.join( ", " );
        return false;
      }
    });
});
$(document).ready(function() {
  $('#add-modal').modal({
    ready: function () {
      $('#input-ingredients').autocomplete('option', 'appendTo', '#input-ingredients');
    }
  })
});