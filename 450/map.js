function showMap(event_id, location_id) {
	const locations = {
		high_street: {
			x: 753,
			y: 1392,
			direction: "right" 
		},
		grove_hill: {
			x: 1730,
			y: 137,
			direction: "right"
		},
		bill_yard: {
			x: 1040,
			y: 411,
			direction: "right"
		},
		st_marys: {
			x: 2215,
			y: 29,
			direction: "left"
		},
		opposite_druries: {
			x: 1461,
			y: 671,
			direction: "right"
		},
		vaughan: {
			x: 1691,
			y: 534,
			direction: "right"
		},
		grove_drive: {
			x: 2693,
			y: 382,
			direction: "left_up"
		},
		outside_druries: {
			x: 2259,
			y: 959,
			direction: "left_up"
		},
		athletics: {
			x: 2284,
			y: 127,
			direction: "right"
		},
		war_memorial: {
			x: 2413,
			y: 704,
			direction: "left_up"
		},
		sports_hall: {
			x: 2553,
			y: 533,
			direction: "right"
		},
		speech_room: {
			x: 2581,
			y: 507,
			direction: "left_up"
		},
		cricket: {
			x: 13,
			y: 1211,
			direction: "left"
		},
		park_drive: {
			x: 798,
			y: 2012,
			direction: "right"
		},
		hundred_steps: {
			x: 836,
			y: 94,
			direction: "right_down"
		},
		roof_terrace: {
			x: 1149,
			y: 296,
			direction: "right_down"
		},
		old_well: {
			x: 2068,
			y: 1017,
			direction: "left"
		},
		the_castle: {
			x: 996,
			y: 692,
			direction: "left_down"
		},
		bandstand: {
			x: 1136,
			y: 1990,
			direction: "left_down"
		},
		osrg: {
			x: 2272,
			y: 656,
			direction: "left_up"
		},
		bradbys: {
			x: 1385,
			y: 1976,
			direction: "left"
		},
		observatory: {
			x: 2521,
			y: 0,
			direction: "right_down"
		},
		chapel_terrace: {
			x: 2904,
			y: 779,
			direction: "left_up"
		},
		kings_head: {
			x: 549,
			y: 2264,
			direction: "left_down"
		},
		old_house: {
			x: 1430,
			y: 281,
			direction: "right_down"
		},
		grove_drive: {
			x: 1315,
			y: 0,
			direction: "right"
		}
	}
	
	const location = locations[location_id]
	const scale = 0.5
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