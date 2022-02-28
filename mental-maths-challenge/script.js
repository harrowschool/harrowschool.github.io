var answerText=""

function randomNumbers(m, n) {
    lowerBound1 = Math.pow(10, m-1)
    upperBound1 = Math.pow(10, m-1) * 9
    
    lowerBound2 = Math.pow(10, n-1)
    upperBound2 = Math.pow(10, n-1) * 9
    
    number1 = Math.floor((Math.random() * upperBound1) + lowerBound1)
    number2 = Math.floor((Math.random() * upperBound2) + lowerBound2)
    
    if (number1 == 1) {
        number1 = 2
    }
    
    if (number2 == 1) {
        number2 = 2
    }
    
    return [number1, number2]
}

function addition(m, n) {
    question = document.getElementById("question")
    
    let [number1, number2] = randomNumbers(m, n)
    
    question.innerHTML = `${number1} + ${number2}`
    answer = String(number1 + number2)
    
    
    answerText += answer + "\n"
    
    answer = document.getElementById("answer")
    answer.innerHTML = ""
}

function subtraction(m, n) {
    question = document.getElementById("question")
    
    let [number1, number2] = randomNumbers(m, n)
    
    question.innerHTML = `${number1} &ndash; ${number2}`
    answerText = String(number1 * number2)
    
    answerText += answer + "\n"
    
    answer = document.getElementById("answer")
    answer.innerHTML = ""
}


function multiplication(m, n) {
    question = document.getElementById("question")
    
    let [number1, number2] = randomNumbers(m, n)
    
    question.innerHTML = `${number1} x ${number2}`
    answerText = String(number1 * number2)
    
    answerText += answer + "\n"
    
    answer = document.getElementById("answer")
    answer.innerHTML = ""
}

function showAnswers() {
    question = document.getElementById("question")
    question.innerHTML = ""
    
    answer = document.getElementById("answer")
    answer.innerHTML = answerText
}

function clearAnswers() {
    answerText = ""
    answer = document.getElementById("answer")
    answer.innerHTML = ""
}