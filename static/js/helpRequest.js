// helpRequest.js

var makeLogo = function() {
    // Halp logo made from html5 canvas element
    var canvas = document.getElementById("halp-logo");
    var context = canvas.getContext("2d");
    var startX = 20;
    var startY = 20;
    var height = 120;
    var width = 225;
    context.fillStyle = '#FF0000';
    context.beginPath();
    context.moveTo(startX, startY);
    context.lineTo(startX + width, startY);
    context.lineTo(startX + width, startY + height);
    context.lineTo(startX + width - 45, startY + height);
    context.lineTo(startX + width - 5, startY + height + 30);
    context.lineTo(startX + width - 15, startY + height);
    context.lineTo(startX, startY + height);
    context.closePath();
    context.fill();
    context.fillStyle = "White";
    context.font = "55px Sans-Serif";
    context.fillText("HALP!", 50, 90);
    context.font = "12px Sans-Serif";
    context.fillText("(Click here to request help)", 57, 110);
};

makeLogo();

$(".delete").click(function() {
    var this_post = $( this ).parent();
    this_post.slideUp();
    $.getJSON("/nevermind?corgi=" + this_post.attr('id').toString(), function(data) {
    });
});

var hoverOn = function() {
    $(this).css("color", "#FFA19F");
};
var hoverOff = function() {
    $(this).css("color", "white");
};

$(".nav-link").hover(hoverOn, hoverOff);