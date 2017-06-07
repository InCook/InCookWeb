/**
 * Created by ichunggi on 2017. 6. 6..
 */
$(document).ready(function() {

  function updateClock() {
    var currentTime = new Date();
    var currentHours = currentTime.getHours();
    var currentMinutes = currentTime.getMinutes();
    var currentSeconds = currentTime.getSeconds();

    currentMinutes = (currentMinutes < 10 ? "0" : "") + currentMinutes;
    currentSeconds = (currentSeconds < 10 ? "0" : "") + currentSeconds;

    var timeOfDay = (currentHours < 12) ? "AM" : "PM";

    currentHours = (currentHours > 12) ? currentHours - 12 : currentHours;
    currentHours = (currentHours === 0) ? 12 : currentHours;

    var currentTimeString = currentHours + ":" + currentMinutes + " " + timeOfDay;

    $("#time").html(currentTimeString);

  }

  setInterval(updateClock(), 1000);

  $("#home-btn").click(function() {
    sendHome();
  });

  $("#home-button").click(function() {
    $("#start-menu").toggle('slide');
  });

  $("#desktop").click(function() {
    if ($("#start-menu").is(':visible')) {
      $("#start-menu").toggle('slide');
    }
  });

  $(function() {
    $("#window-wrapper").draggable({
      containment: $("#desktop")
    });
    $("#window-wrapper").resizable({
      handles: 'all'
    });
  });

  $(".start-menu-item:first-child").click(function() {
    $("#window-wrapper").fadeToggle();
    $("#start-menu").fadeToggle('fast');
  });

  $("#window-exit").click(function() {
    $("#window-wrapper").fadeToggle('fast');
    sendHome();
  });

  $(".folder").click(function() {
    $(this).toggleClass("folder-clicked");
  });
  $(".folder").hover(function() {
    $(this).toggleClass("folder-hover");
  });

  function setFrameSource() {
    var frameSource = $("#address-bar").val();
    $("#frame").attr('src', "http://" + frameSource);
    $("#address-bar").attr("placeholder", frameSource);
    $("#address-bar").val("");
  }

  function sendHome() {
    var home = "www.duckduckgo.com";
    $("#frame").attr('src', "http://" + home);
    $("#address-bar").attr("placeholder", home);
  }

});