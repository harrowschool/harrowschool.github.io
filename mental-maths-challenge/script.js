var answerText=""

function multiplication2x2() {
    question = document.getElementById("question")
    number1 = Math.floor((Math.random() * 90) + 10)
    number2 = Math.floor((Math.random() * 90) + 10)
    
    question.innerHTML = `${number1} x ${number2}`
    answerText = String(number1 * number2)
    
    answer = document.getElementById("answer")
    answer.innerHTML = ""
}

function showAnswer() {
    answer = document.getElementById("answer")
    answer.innerHTML = "= " + answerText
}