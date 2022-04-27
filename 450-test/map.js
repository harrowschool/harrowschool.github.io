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
	const scale = 1
	const size = {x: 3625 * scale, y: 4096 * scale}
	
	var canvas = document.getElementById(event_id).getElementsByTagName("canvas")[0]
	canvas.style.display = "block"
	canvas.width = size.x
	canvas.height = size.y
	canvas.style.width = "100%"
	var context = canvas.getContext("2d")
	var map = document.getElementById("map")
	var hand = document.getElementById(`hand_${location.direction}`)
	
	context.drawImage(map, 0, 0, size.x, size.y)
	context.drawImage(hand, location.x * scale, location.y * scale, hand.naturalWidth * scale, hand.naturalHeight * scale)
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