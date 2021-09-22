(function(){
  function quiz(){
    const output = [];

    myQuestions.forEach(
      (currentQuestion, questionNumber) => {

        const answers = [];

        for(letter in currentQuestion.answers){

          answers.push(
            `<label>
              <input type="radio" name="question${questionNumber}" value="${letter}">
              ${letter} :
              ${currentQuestion.answers[letter]}
            </label>`
          );
        }

        output.push(
          `<div class="question"> ${currentQuestion.question} </div>
          <div class="answers"> ${answers.join('')} </div>`
        );
      }
    );

    quizContainer.innerHTML = output.join('');
  }

  function showResults(){

    const answerContainers = quizContainer.querySelectorAll('.answers');

    let numCorrect = 0;

    myQuestions.forEach( (currentQuestion, questionNumber) => {

      const answerContainer = answerContainers[questionNumber];
      const selector = `input[name=question${questionNumber}]:checked`;
      const userAnswer = (answerContainer.querySelector(selector) || {}).value;

      if(userAnswer === currentQuestion.correctAnswer){

        numCorrect++;

        answerContainers[questionNumber].style.color = 'lime';
      }
      else{
        answerContainers[questionNumber].style.color = 'red';
      }
    });

    if(numCorrect > 7){
      resultsContainer.innerHTML = `${numCorrect} out of ${myQuestions.length}! That's a great score! You should be proud of that!`;
    }
    else if(numCorrect < 4) {
    resultsContainer.innerHTML = `${numCorrect} out of ${myQuestions.length}... I think you might be having a bad day. Or, of course, you're just bad at history.`; 
    }
    else {
    resultsContainer.innerHTML = `${numCorrect} out of ${myQuestions.length}. That's pretty much average, well done!`; 
    }
  }

  const quizContainer = document.getElementById('quiz');
  const resultsContainer = document.getElementById('results');
  const submitButton = document.getElementById('submit');
  const myQuestions = [
    {
      question: "1. When did WW1 start and end?",
      answers: {
        a: "1917-1921",
        b: "1915-1919",
        c: "1914-1918",
        d: "1911-1917"
      },
      correctAnswer: "c"
    },
    {
      question: "2. Who was the second person ever on the moon?",
      answers: {
        a: "Michael Collins",
        b: "Yuri Gagarin",
        c: "Neil Armstrong",
        d: "Buzz Aldrin"
      },
      correctAnswer: "d"
    },
    {
      question: "3. Who was nominated for the nobel peace prize in 1939?",
      answers: {
        a: "Adolf Hitler",
        b: "Neville Chamberlain",
        c: "Benito Mussolini",
        d: "Winston Churchill"
      },
      correctAnswer: "a"
    },
    {
      question: "4. Who was the first democratically elected president of Russia?",
      answers: {
        a: "Boris Yeltsin",
        b: "Vladimir Putin",
        c: "Nikita Khrushchev",
        d: "Mikhail Gorbachev"
      },
      correctAnswer: "a"
    },
    {
      question: "5. What did Ancient Egyptians use as pillows?",
      answers: {
        a: "Stones",
        b: "Cats",
        c: "Papyrus paper",
        d: "Bags of sand"
      },
      correctAnswer: "a"
    },
    {
      question: "6. Which one of these Us presidents worked as a lifeguard?",
      answers: {
        a: "Joe Biden",
        b: "Dwight D. Eisenhower",
        c: "Ronald Reagan",
        d: "John F. Kennedy"
      },
      correctAnswer: "c"
    },
    {
       question: "7. The Parthenon was a temple dedicated to Ares, the God of War",
      answers: {
        a: "True",
        b: "False"
      },
      correctAnswer: "b"
    },
    {
      question: "8. What did Ancient Romans use as mouthwash?",
      answers: {
        a: "Sea water",
        b: "Wine",
        c: "Fish blood",
        d: "Human urine"
      },
      correctAnswer: "d"
    },
    {
      question: "9. Where was John F. Kennedy assassinated?",
      answers: {
        a: "Dallas",
        b: "Washington D.C.",
        c: "Philadelphia",
        d: "New Orleans"
      },
      correctAnswer: "a"
    },
    {
      question: "10. When Burger King first opened, how much did a burger cost?",
      answers: {
        a: "55 cents",
        b: "18 cents",
        c: "42 cents",
        d: "5 cents"
      },
      correctAnswer: "b"
    }
  ];

quiz();

submitButton.addEventListener('click', showResults);

})();

// I got most of my information from w3schools.
// While I was in Russia, a programmer helped me write the start of this code, making sure I understood all the concepts.