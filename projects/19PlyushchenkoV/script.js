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

    if(numCorrect > 15){
      resultsContainer.innerHTML = `Congratulations! You got ${numCorrect} out of ${myQuestions.length}! That is an outstanding score!`;
    }
    else if(numCorrect < 8) {
    resultsContainer.innerHTML = `${numCorrect} out of ${myQuestions.length}... I guess not everyone can be good at geography`; 
    }
    else {
    resultsContainer.innerHTML = `${numCorrect} out of ${myQuestions.length}. That's not that bad but I know you can do better!`; 
    }

  }

  const quizContainer = document.getElementById('quiz');
  const resultsContainer = document.getElementById('results');
  const submitButton = document.getElementById('submit');
  const myQuestions = [
    {
      question: "1. What is the capital of Sweden?",
      answers: {
        a: "Helsinki",
        b: "Stockholm",
        c: "Copenhagen",
        d: "Reykjavík"
      },
      correctAnswer: "b"
    },
    {
      question: "2. What is the national language of Brazil?",
      answers: {
        a: "English",
        b: "Spanish",
        c: "French",
        d: "Portugese"
      },
      correctAnswer: "d"
    },
    {
      question: "3. What country is Vilnius the capital of?",
      answers: {
        a: "Estonia",
        b: "Hungary",
        c: "Czech Republic",
        d: "Lithuania"
      },
      correctAnswer: "d"
    },
    {
      question: "4. What is the largest country in the world?",
      answers: {
        a: "Canada",
        b: "Greenland",
        c: "Russia"
      },
      correctAnswer: "c"
    },
    {
      question: "5. Which one of these countries does Slovenia border?",
      answers: {
        a: "Slovakia",
        b: "Italy",
        c: "Czech Republic",
        d: "Serbia",
        e: "Albania"
      },
      correctAnswer: "b"
    },
    {
      question: "6. Which one of these countries is below the equator?",
      answers: {
        a: "Phillipenes",
        b: "Venezuela",
        c: "Tanzania",
        d: "Malasiya",
        e: "South Sudan"
      },
      correctAnswer: "c"
    },
    {
      question: "7. How many US states border Canada?",
      answers: {
        a: "8",
        b: "13"
      },
      correctAnswer: "b"
    },
    {
      question: "8. What is the capital of Cyprus?",
      answers: {
        a: "Nicosia",
        b: "Vilna",
        c: "Patras",
        d: "Limassol"
      },
      correctAnswer: "a"
    },
    {
      question: "9. Geographically, which country is directly above Germany?",
      answers: {
        a: "Netherlands",
        b: "Denmark",
        c: "Luxembourg",
        d: "Norway"
      },
      correctAnswer: "b"
    },
    {
      question: "10. Does Russia border North Korea?",
      answers: {
        a: "Yes",
        b: "No"
      },
      correctAnswer: "a"
    },
    {
      question: "11. What is the capital of New Zeland?",
      answers: {
        a: "Wellington",
        b: "Christchurch",
        c: "Auckland",
        d: "Dunedin"
      },
      correctAnswer: "a"
    },
    {
      question: "12a. Which US state has the highest population?",
      answers: {
        a: "Texas",
        b: "New York",
        c: "California",
        d: "Florida"
      },
      correctAnswer: "c"
    },
    {
      question: "12b. Which US state has the lowest population?",
      answers: {
        a: "Alaska",
        b: "Rhode Island",
        c: "Wyoming",
        d: "Delaware",
        e: "North Dakota",
        f: "Vermont"
      },
      correctAnswer: "c"
    },
    {
      question: "13. Which African country did Star Wars use as the setting for Tatooine?",
      answers: {
        a: "Angola",
        b: "Morocco",
        c: "Kenya",
        d: "Tunisia"
      },
      correctAnswer: "d"
    },
    {
      question: "14. What is the oldest city in the world?",
      answers: {
        a: "Athens",
        b: "Damascus",
        c: "Jerusalem",
        d: "Jericho"
      },
      correctAnswer: "d"
    },
    {
      question: "15. What is the flattest continent?",
      answers: {
        a: "Africa",
        b: "Australia",
        c: "South America",
        d: "Antarctica"
      },
      correctAnswer: "b"
    },
    {
      question: "16. What is the most densely populated country?",
      answers: {
        a: "Vatican City",
        b: "China",
        c: "India",
        d: "Monaco"
      },
      correctAnswer: "d"
    },
    {
      question: "17. What is the capital of Nigeria?",
      answers: {
        a: "Ibadan",
        b: "Lagos",
        c: "Abuja",
        d: "Kano"
      },
      correctAnswer: "c"
    },
    {
      question: "18. What mountain is closest to the moon?",
      answers: {
        a: "Mt. Everest",
        b: "K2",
        c: "Mt. Chimborazo",
        d: "Mt. Kilimanjaro"
      },
      correctAnswer: "c"
    },
    {
      question: "19. How many countries are there in North America?",
      answers: {
        a: "12",
        b: "3",
        c: "23",
        d: "5"
      },
      correctAnswer: "c"
    },
    {
      question: "20. Which country has the most ancient pyramids?",
      answers: {
        a: "Namibia",
        b: "Egypt",
        c: "Mexico",
        d: "Sudan"
      },
      correctAnswer: "d"
    }
  ];

quiz();

submitButton.addEventListener('click', showResults);

})();

// I got most of my information from w3schools.
// While I was in Russia, a programmer helped me write the first ~30 lines of this code, making sure I understood all the concepts.