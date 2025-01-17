let col = 0;

function expandAllExercises() {
	if(challenges) {
		challenges.forEach(expandExercise);
	}
}

function expandExercise(item, index) {
  if(item.length >= 3) {
	var newHTML = challengeHTML.replace("$$0", item[0]).replace("$$1", item[1]).replace("$$2", item[2]);
  }
  if(item.length >= 4) {
	newHTML = newHTML.replace("$$3", item[3]);
  }
	
  $("#col" + col)[0].innerHTML += newHTML;
  
  col = (col + 1) % 3;
}

expandAllExercises();