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
    questionElement = document.getElementById("question")
    
    let [number1, number2] = randomNumbers(m, n)
    
    questionElement.innerHTML = `${number1} + ${number2}`
    answer = String(number1 + number2)
    
    
    answerText += `${number1} + ${number2} = ${answer}<br>`
    
    answerElement = document.getElementById("answer")
    answerElement.innerHTML = ""
}

function subtraction(m, n) {
    questionElement = document.getElementById("question")
    
    let [number1, number2] = randomNumbers(m, n)
    
    questionElement.innerHTML = `${number1} &ndash; ${number2}`
    answer = String(number1 - number2)
    
    answerText += `${number1} &ndash; ${number2} = ${answer}<br>`
    
    answerElement = document.getElementById("answer")
    answerElement.innerHTML = ""
}


function multiplication(m, n) {
    questionElement = document.getElementById("question")
    
    let [number1, number2] = randomNumbers(m, n)
    
    questionElement.innerHTML = `${number1} x ${number2}`
    answer = String(number1 * number2)
    
    answerText += `${number1} x ${number2} = ${answer}<br>`
    
    answerElement = document.getElementById("answer")
    answerElement.innerHTML = ""
}

function showAnswers() {
    question = document.getElementById("question")
    question.innerHTML = ""
    
    answerElement = document.getElementById("answer")
    answerElement.innerHTML = answerText
    console.log(answerText)
}

function clearAnswers() {
    answerText = ""
    answerElement = document.getElementById("answer")
    answerElement.innerHTML = ""
}