// helpRequest.js
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
context.fillText("HALP!", 50, 100);

$(".delete-button").click(function() {
    $( this ).parent().slideUp();
});