var canvas = document.getElementById("myCanvas")
canvas.width = 3625
canvas.height = 4096
canvas.style.width = "100%"
var context = canvas.getContext("2d")
var map = new Image()
map.src = "/450/450_map.jpeg"
var hand = new Image()
hand.src = "/450/hand_right.png"

var x_slider = document.getElementById("x_coordinate")
var y_slider = document.getElementById("y_coordinate")

var x_string = document.getElementById("x_string")
var y_string = document.getElementById("y_string")

map.onload = function() {
	context.drawImage(map,0,0, 3625, 4096)
	context.drawImage(hand, 0, 0)
}

function redraw() {
	context.clearRect(0, 0, canvas.width, canvas.height)
	context.drawImage(map,0,0, 3625, 4096)
	
	x_string.innerHTML = "x: " + x_slider.value.toString()
	y_string.innerHTML = "y: " + y_slider.value.toString()
	
	context.drawImage(hand, x_slider.value, y_slider.value)
}

x_slider.oninput = function() {
	redraw()
}

y_slider.oninput = function() {
	redraw()
}