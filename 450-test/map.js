function showMap(event_id, location_id) {
	const locations = {
		high_street: {
			x: 906,
			y: 988,
			direction: "right_down" 
		},
		grove_hill: {
			x: 1730,
			y: 137,
			direction: "right"
		}
	}
	
	const location = locations[location_id]
	const size = {x: 1000, y: 1129}
	
	var canvas = document.getElementById(event_id).getElementsByTagName("canvas")[0]
	canvas.style.display = "block"
	canvas.width = size.x
	canvas.height = size.y
	canvas.style.width = "100%"
	var context = canvas.getContext("2d")
	//var map = new Image()
	//map.src = "/450-test/450_map.jpg"
	var map = document.getElementById("map")
	//var hand = new Image()
	//hand.src = `/450-test/hand_${location.direction}.png`
	var hand = document.getElementById(`hand_${location.direction}`)
	
	context.drawImage(map, 0, 0, size.x, size.y)
	context.drawImage(hand, location.x, location.y)
	
	// map.onload = function() {
	// 	context.drawImage(map, 0, 0, size.x, size.y)
	// 	context.drawImage(hand, location.x, location.y)
	// }
}

function toggleMap(event_id, location_id) {
	var canvas = document.getElementById(event_id).getElementsByTagName("canvas")[0]
	var button = document.getElementById(event_id).getElementsByTagName("p")[0].getElementsByTagName("button")[0]
	
	if (canvas.style.display == "none") {
		showMap(event_id, location_id)
		button.innerHTML = "Hide Map"
	} else {
		canvas.style.display = "none"
		button.innerHTML = "Show Map"
	}
}