_about = ()=>
      print(`Welcome to Σ Terminal, brought to you with ♥ from 
      <a href="https://github.com/Harrow-Enigma" target="_blank" rel="noopener noreferrer">Team Enigma</a>,
      Harrow School.<br/>
      We hope you'll find this a useful resource in conjunction with the Cross-Curricular Lecture.<br/>
      Type <code>/help</code> to learn more about how to use Sigma Terminal.<br/>
      You can check out our <a href="https://github.com/PerceptronV/sigma_terminal" 
      target="_blank" rel="noopener noreferrer">source code here</a>.`, html=true, color="white");

_examples = ()=>{
  runTerminal(`// OK. Let's see some examples of using Sigma Terminal.`, false);
  runTerminal(`// This Terminal runs everything JavaScript, plus some additional functions that Vincent has written up.`, false);
  runTerminal(`a = 18 // You can define variables`, false);
  runTerminal(`a * 2 // and operate on them`, false);
  runTerminal(`gcd(210, 742) // Compute Greatest Common Divisor`, false);
  runTerminal(`primesUpto(100); // Compute prime numbers up to 100`, false);
  runTerminal(`for (n=1; n<10; n++) print("ϕ("+n+")="+totient(n)); // Compute Euler's totient function on numbers up to 10`, false);
}
    
_help = ()=>
  print(`
  <h3>Terminal Functions</h3>
  <code>print(s, html=false, color="inherit")</code> Prints string <code>s</code>,
    optionally as html and with a different color; e.g.
    <code>print("&lt;i&gt;Hello World!&lt;/i&gt;", true, "blue")</code><br/>
  <code>/about</code>    Tells you about the story of Σ Sigma Terminal<br/>
  <code>/examples</code> Gives a few examples of what you can do here<br/>
  <code>/rsa</code>      Takes you to our interactive demonstration of the RSA Cryptosystem<br/>
  <code>/slides</code>   Takes you to the slides that accopany the talk (and this terminal!)<br/>
  <br/>
  <h3>Number Theory Functions</h3>
  <code>primesUpto(n)</code> Computes all primes up to <code>n</code> using the 
  <a href="https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes"
  target="_blank" rel="noopener noreferrer">Sieve of Eratosthenes</a><br/>
  <code>mod(a, m)</code> Computes the remainder of <code>a</code> when divided by <code>m</code><br/>
  <code>gcd(a, b, steps=true)</code> Computes Greatest Common Divisor of <code>a</code> and <code>b</code> using the
  <a href="https://www.khanacademy.org/computing/computer-science/cryptography/modarithmetic/a/the-euclidean-algorithm"
  target="_blank" rel="noopener noreferrer">Euclidean Algorithm</a>, optionally showing algorithm steps<br/>
  <code>extEuc(a, b, steps=true)</code> Uses the <a href="http://www-math.ucdenver.edu/~wcherowi/courses/m5410/exeucalg.html"
  target="_blank" rel="noopener noreferrer">Extended Euclidean Algorithm</a> to find
  <code>x</code> and <code>y</code> such that <code>ax + by = gcd(a, b)</code>,
  optionally showing algorithm steps<br/>
  <code>inv(a, m, steps=true)</code> Computes modular inverse of <code>a</code> (modulo <code>m</code>)
  using the <a href="http://www-math.ucdenver.edu/~wcherowi/courses/m5410/exeucalg.html"
  target="_blank" rel="noopener noreferrer">Extended Euclidean Algorithm</a>,
  optionally showing algorithm steps<br/>
  <code>totient(n)</code> Computes <a href="https://en.wikipedia.org/wiki/Euler%27s_totient_function"
  target="_blank" rel="noopener noreferrer">Euler's totient function</a> of <code>n</code>
  `, html=true);

_slides = ()=>
      print(`Interested in the slides that accompany this lecture? You can find them
      <a href="https://github.com/PerceptronV/sigma_terminal/blob/main/static/ccl_crypto_slides.pdf" 
      target="_blank" rel="noopener noreferrer">here</a>!`,
      html=true, color="white");

_vincent = ()=> 
  print(`Hmmm wassup? Since you've ended up here, either you're very smart (meaning you probably found
    this function in the source code), or you're very smart (you somehow guessed that someone like me 
    would hide a command like this), or you're very smart (cuz I can't figure out how you got here).<br/>
    In any case, I hope the talk's been interesting! Feel free to email me at
    <a href="mailto:19songy@harrowschool.org.uk">19songy@harrowschool.org.uk</a>
    if you have any questions, or ideas, or anything!`, html=true, color="yellow");

_mit = ()=>
  print(`<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/0/0c/MIT_logo.svg/2560px-MIT_logo.svg.png"
  width="400em;"></img>`, html=true);

_random = ()=>
  print(Math.random())

function print(str, html=false, color="inherit", breakline=false) {
  if (_DEVICE == "console") console.log(str);
  else {
    if (!(str == null || str == undefined)) {
      if (html) var newDiv = $(`<div style="color: ` + color + `;">` + str + "</div>");
      else var newDiv = $(`<div style="color: ` + color + `;"></div>`).text(str);
      newDiv.addClass("terminal-line");
      newDiv.addClass("hiddenscrollbar");
      if(breakline) newDiv.addClass("terminal-break");
      $("#"+_DEVICE).append(newDiv);
    }
  }
}

function runTerminal(script, breakline=true) {
  script = script.trim();
  if (script.length != 0) {
    print("↩ " + script, html=false, color="green");

    if (script[0] == "/" && script[1] != "/") {
      var cmd = "_" + script.slice(1) + "()"; // Convert, say, /about to _about()
      try {eval(cmd);}
      catch {print(script + " is not a valid `/` command. Run <code>/help</code> if you are unsure what do to.", html=true, color="red");}
    } else {
      try {print(eval(script), html=false, color="inherit");}
      catch (error) {print(error, html=false, color="red");}
    }

    print("", html=false, color="inherit", breakline=breakline);

    document.getElementById(_KEYBOARD).scrollIntoView();
    
  }
}

function initTerminal() {
  $("#"+_KEYBOARD).keydown(function(event) {
    if (event.which==13) {
      var val = $("#"+_KEYBOARD).val();
      $("#"+_KEYBOARD).val("");
      runTerminal(val, _KEYBOARD);
    };
  });
}
