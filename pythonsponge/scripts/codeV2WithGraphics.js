var ready = false;
var currOutput = null;
var currInps = null;
var path = window.location.pathname;
var filename = path.split("/").pop();
var pageID = filename.replace("page", "P").replace(".html", "");
var pageExercises = "";
var origCode = Object;
var editors = Object;
var codeQS = null;
var testQS = null;
var modeQS = "t";
const INDENT = "    ";

const LIBRARY_PATCH = `
from time import sleep
from js import sleep_patch
sleep = sleep_patch
`

const OUTPUT_PATCH = `
import sys
import io
sys.stdout = io.StringIO()
from js import addToOutput
orig_print = print
# redirect print via output textarea and console
def new_print(*args, **kwargs):
  stdout_len = len(sys.stdout.getvalue())
  orig_print(*args, **kwargs)
  stdout = sys.stdout.getvalue()
  addToOutput(stdout[stdout_len:])
  sys.stdout.flush()
print = new_print
`

const INPUT_PATCH = `
from js import input_patch, asyncinput
input = input_patch
__builtins__.input = input_patch
`

class Context {
	constructor() {
		this.canvas = document.getElementById("canvas")
		this.ctx = canvas.getContext("2d")
	}
  
	beginPath() {
		this.ctx.beginPath();
	}
	
	closePath() {
		this.ctx.closePath();
	}

	fill() {
		this.ctx.fill();
	}
	
	get fillStyle() {
		return this.ctx.fillStyle;
	}
	
	set fillStyle(newVal) {				
		this.ctx.fillStyle = newVal;
	}			

	rect(x, y, w, h) {
		this.ctx.rect(x, y, w, h);
	}	
	
	arc(x, y, rad, ang_start, ang_end, isFilled) {
		this.ctx.arc(x, y, rad, ang_start, ang_end, isFilled);
	}
	
}

function getGraphicsContext() {
	let ctx = new Context();
	return ctx;
}	

function clearAllTimeouts() {
	// Set a fake timeout to get the highest timeout id
	var highestTimeoutId = setTimeout(";");
	for (var i = 0 ; i < highestTimeoutId ; i++) {
		clearTimeout(i); 
	}
}

// USED IN async input cases
// wait for DOM: wait for 2 frame draws (1 is not always enough, as the first frame might be during reflow)
window.waitForDOM = ms => new Promise(resolve => requestAnimationFrame(() => {requestAnimationFrame(() => resolve());}));

const cipher = salt => {
    const textToChars = text => text.split('').map(c => c.charCodeAt(0));
    const byteHex = n => ("0" + Number(n).toString(16)).substr(-2);
    const applySaltToChar = code => textToChars(salt).reduce((a,b) => a ^ b, code);

    return text => text.split('')
        .map(textToChars)
        .map(applySaltToChar)
        .map(byteHex)
        .join('');
};

const decipher = salt => {
    const textToChars = text => text.split('').map(c => c.charCodeAt(0));
    const applySaltToChar = code => textToChars(salt).reduce((a,b) => a ^ b, code);
    return encoded => encoded.match(/.{1,2}/g)
        .map(hex => parseInt(hex, 16))
        .map(applySaltToChar)
        .map(charCode => String.fromCharCode(charCode))
        .join('');
};

const DECIPH = decipher('scrambleSalt');
const CIPH = cipher('scrambleSalt');

// check for template code
const urlParams = new URLSearchParams(window.location.search);
if(urlParams.has('code')) {
	if(urlParams.get('code')) {
		codeQS = decodeURIComponent(DECIPH(urlParams.get('code')));
	} else {
		codeQS = " ";
	}
}
if(urlParams.has('test')) {
	testQS = decodeURIComponent(DECIPH(urlParams.get('test')));
}
if(urlParams.has('desc')) {
	if(urlParams.get('desc')) {
		descQS = decodeURIComponent(DECIPH(urlParams.get('desc')));
		if($("#taskDescription")) {
			$("#taskDescription")[0].innerHTML = descQS;
		}
	}
}
if(urlParams.has('mode')) {
	modeQS = urlParams.get('mode');
	if (modeQS == "p") {
		if($("#divParsons")) {
			$("#divParsons").css("display", "inline");
		}
		activateParsons();
	}
}

function addToOutput(s) {
  currOutput.value += s;
  console.log(s);
}

async function main(){
  expandExercises();
  storeOriginalCode();
  await loadPyodide({ indexURL : 'https://cdn.jsdelivr.net/pyodide/v0.17.0/full/' });  
}

function input_patch(text) {
	if(currInps){
		return currInps.shift();
	}
	else{
		msg = text
		if(currOutput.value != "")
			if(msg) {
			    msg = currOutput.value + "\n" + msg;
			} else
			{
				msg = currOutput.value;
			}
		
		if(typeof clearOutput !== 'undefined' && clearOutput) {
			currOutput.value = "";
		}
		
		return prompt(msg);

	}
}

async function sleep_patch(time) {
  await new Promise(resolve => setTimeout(resolve, time * 1000));
}

async function asyncinput(id, prompt) {
	
	await window.waitForDOM(100);  // this could be replaced with any other async function (including a promise for a button click)
	$("#output"+id).scrollTop($("#output"+id)[0].scrollHeight);
	
	if(currInps){
		return currInps.shift();
	}
	else{	
		
		if(typeof prompt == 'undefined') {
			prompt = "INPUT:"
		}
		
		msg = $("#result"+id)[0];
		msg.innerHTML = prompt;
		msg.className = "result";
		$("#inp"+id).val("");
		await new Promise(
			function(resolve, reject) {
				console.log(prompt);
				console.log("input requested from input box...");
				document.getElementById('inpsub'+id).addEventListener('click', function(e) {$("#inputbar"+id).addClass("hidden");$("#result"+id)[0].className = "hidden";resolve();}, {once: true});
				$("#inputbar"+id).removeClass("hidden");
				$("#inp"+id)[0].focus();
			});
			

		return $('#inp'+id).val();

	}
}

function setOutputHidden(id, state) {
	if(state){
		$("#output" + id).attr('hidden','');
	} else {
		$("#output" + id).removeAttr('hidden');
	}
	
}

pyodideReadyPromise = main();

function expandExercises() {
	$.each($("div"), function(index, el) {
		
		if(el.id.startsWith("ex")){			
			var outsize = $(this).attr("outsize");
			var exId = el.id.replace("ex", "");
			var codeTextarea = $(this).find("textarea");
			codeTextarea[0].id = "code" + exId;
			
			if(codeQS) {
				if(modeQS == "p") {
					el.innerHTML = el.innerHTML.replace("$$", "");
				} else {
					el.innerHTML = el.innerHTML.replace("$$", codeQS);
				}
			}	

			if(testQS) {
				el.innerHTML = el.innerHTML.replace("@@", testQS.replaceAll("$","$$$$"));
			}			
			
			// set just in case we are using the fallback text area - auto-height is set on custom css tweak to codemirror
			// see 2nd answer - https://stackoverflow.com/questions/30098071/codemirror-autoresize-upto-a-given-number-of-lines
			if(!codeTextarea.attr("rows")){
				codeTextarea.attr("rows", codeTextarea[0].value.trim().split(/\r|\r\n|\n/).length + 2);
			}
				
			extraHTML = `
			<p>
			  <button id='run@@' onclick='evaluatePython(\"@@\")'>Run</button>
			  ##
			  <button id='copy@@' onclick='copyPython(\"@@\")'>Copy</button>
			  <button id='reset@@' onclick='resetPython(\"@@\")'>Reset</button>
			</p>
			<p>
			  <b>Output:</b>
			</p>
			<p>
			  <textarea id='output@@' rows='$$' disabled></textarea>
			</p>
			<span id='result@@' class='hidden'></span>
			<div id="inputbar@@" class="inputbar hidden">
			  <input class="inpbox" id="inp@@" type="text" onkeyup="if (event.keyCode === 13) {$('#inpsub@@').click();}"></input>
			  <input id="inpsub@@" type="button" value="enter" />
			</div>`;
			
			submitHTML = "";
			if(el.id.endsWith("T")){
				var hiddenEl =  $(this).find("input");
				if(hiddenEl && hiddenEl[0].value.trim() != "")
				{ 
				 hiddenEl[0].id = "tests" + exId;
				 submitHTML = "<button id='submit@@' onclick='submitPython(\"@@\")'>Submit</button>";
				}
			}

			if(el.hasAttribute("controllocation")) {
				el.innerHTML = extraHTML.replace("##", submitHTML).replaceAll("@@", exId).replace("$$", outsize) + el.innerHTML;
			}
			else {
				el.innerHTML += extraHTML.replace("##", submitHTML).replaceAll("@@", exId).replace("$$", outsize);
			}
			$("#code" + exId)[0].value = $("#code" + exId)[0].value.trim() + "\n";
			
			
			if(CodeMirror) {
			
				try {
					var editor = CodeMirror.fromTextArea($("#code" + exId)[0], {
					  lineNumbers: true,
					  mode: "python",
					  matchBrackets: true,
					  tabSize: 4,
					  indentUnit: 4
					});
			
					editor.setOption("extraKeys", {
					  Tab: function(cm) {
					  var spaces = Array(cm.getOption("indentUnit") + 1).join(" ");
					  cm.replaceSelection(spaces);
					  }  
					});
					
					editors[exId] = editor;
				}
				catch(err) {
				  console.log(err.message);
				}

			}
			
		} else if (el.id.startsWith("pp")) {
		
			activateParsons();
			
			var runHTML = "";
			var turtleStarterHTML = ""
			
			if(typeof initial != 'undefined'){
				runHTML = `<button id="btnRunParsonsCode" onclick="runParsonsCode();">Run/debug</button>`;
				
			}			
			
			el.innerHTML = `
				<div id="sortableTrash" class="sortable-code"><p>Drag from here</p><ul id="ul-sortableTrash" class="ui-sortable"></ul></div>
				<div id="sortable" class="sortable-code"><p>Construct your solution herex</p><ul id="ul-sortable" class="ui-sortable output"></ul></div>
				<div style="clear:both;"></div>
				<p>
				  <button id="newInstanceLink">Regenerate</button>
				  <button id="feedbackLink">Submit</button>
				  ${runHTML}				  
				</p>
				<span id='resultPP' class='hidden'></span>`;
		}
	});	
}

function updateTextArea(id) {
	code = $("#code" + id)[0];
	
	if(editors[id]) {
		try {
			code.value = editors[id].doc.getValue();
		}
		catch(err) {
		}
	}
}

function storeOriginalCode() {
	$.each($("textarea"), function(index, el) {
		if(el.id.startsWith("code")){
		  origCode[el.id] = el.value;
		}
	});
}


function copyPython(id) {
	updateTextArea(id);
	code = $("#code" + id)[0];
	code.select();
	code.setSelectionRange(0, 99999); /* For mobile devices */
	navigator.clipboard.writeText(code.value);  
	msg = $("#result" + id)[0];
	msg.innerHTML = "copied to clipboard"
	msg.className = "result";
}

function resetPython(id) {
	code = $("#code" + id)[0];
	code.value = origCode["code" + id];
	
	if(editors[id]) {
		try {
			editors[id].doc.setValue(code.value);
		}
		catch(err) {
		}
	}	
}

async function runParsonsCode() {
	var exId = "01E";
	var exId2 = "01T";
	
	var listItems = $("#ul-sortable li");
	var strCode = "";
	
	listItems.each(function(idx, li) {
		var line = $(li);
		var indent = "";
		switch(line.css("margin-left")) {			
		  case "0px":
			break;
		  case "50px":
			indent = INDENT;
			break;
		  case "100px":
			indent = INDENT.repeat(2);
			break;
		  case "150px":
			indent = INDENT.repeat(3);
			break;
		  case "200px":
			indent = INDENT.repeat(4);
			break;	
		  case "250px":
			indent = INDENT.repeat(5);
			break;	
		  default:
			indent = INDENT.repeat(6);
			break;			
		}
		strCode += indent + line[0].innerText + "\n";

	});

	if(editors[exId]) {
		editors[exId].doc.setValue(strCode);
		evaluatePython(exId);
	} else if (editors[exId2]) {
		editors[exId2].doc.setValue(strCode);
		evaluatePython(exId2);
	}
	
}

function convertToAsync(code, id){
	result = "async def do_main_async():\n";
	let codelines = code.split("\n");
	for(var i = 0;i < codelines.length;i++){
		result += "  " + codelines[i] + "\n";
	}
	result = result.replaceAll("from time import sleep", "")
	
	result = result.replaceAll("input(", `await asyncinput('${id}',`);
	result = result.replaceAll("time.sleep(", "sleep(");
	result = result.replaceAll("sleep(", "await sleep(");
	result += "\ndo_main_async()";
	return result;
}

async function evaluatePython(id) {
	
  updateTextArea(id);	
  setOutputHidden(id, false);
  code = $("#code" + id)[0];  
  output = $("#output" + id)[0];
  msg = $("#result" + id);
  if(msg.length > 0)
      msg[0].className = "hidden";
  
  if(!ready){
	$("#run" + id)[0].disabled = true;
	output.value = "please wait...";
	await pyodideReadyPromise;
	await pyodide.runPythonAsync(LIBRARY_PATCH);
	await pyodide.runPythonAsync(OUTPUT_PATCH);
	await pyodide.runPythonAsync(INPUT_PATCH);
	ready = true;
  }
      
  try {
	currInps = null;
	currOutput	= output
	output.value = "";
	var codeToRun = code.value;
	if(typeof runAsync !== 'undefined' && runAsync) {
      codeToRun = convertToAsync(codeToRun, id);
    }	

	codeAbort = false;
	await pyodide.runPythonAsync(codeToRun);
	
	if(id.endsWith("E"))
		document.cookie = "Code" + pageID + "--" + id + "=completed; expires=Sat, 1 Jan 2050 12:00:00 UTC";
  } catch(err) {
	errMsg = err.toString();
	errMsg = errMsg.substring(errMsg.indexOf('File "<unknown>"'));
	errMsg = errMsg.substring(errMsg.indexOf('File "<exec>"'));	
    addToOutput(errMsg);
  }
  
  $("#run" + id)[0].disabled = false;
}

async function submitPython(id) {
	  
  updateTextArea(id);	
  
  setOutputHidden(id, true);	
  code = $("#code" + id)[0];  
  output = $("#output" + id)[0];	
  
  if(!ready){
	$("#submit" + id)[0].disabled = true;
	output.value = "please wait...";	  
	await pyodideReadyPromise;
	await pyodide.runPythonAsync(OUTPUT_PATCH);
	await pyodide.runPythonAsync(INPUT_PATCH);
	ready = true;
  }
      
  try {
	currOutput = output
    var passed = true;	
	testCases = $("#tests" + id)[0].value.split('@@');
	var codeToRun = code.value;
	if(typeof runAsync !== 'undefined' && runAsync) {
      codeToRun = convertToAsync(codeToRun, id);
    }
	for(var i = 0;i < testCases.length;i++){
		output.value = "";
		testParts = testCases[i].split("$$");
		testInp = testParts[0].split("##");
		currInps = testInp
		testOut = testParts[1].replaceAll("##", "\n");
		await pyodide.runPythonAsync(codeToRun);		
		if(output.value.trim() != testOut.trim())
			passed = false;		
	}
	
	msg = $("#result" + id)[0];
	
	if(passed) {
		document.cookie = "Code" + pageID + "--" + id + "=completed; expires=Sat, 1 Jan 2050 12:00:00 UTC";
		msg.innerHTML = "<ul class='success'><li>Task completed - well done!</li></ul>";
	}
	else {		
		msg.innerHTML = "Not quite ... try again ... if you are stuck then <a href='javascript:viewTestCases(\"" + id + "\");'>viewing the test cases</a> might help.";
	}
	
	msg.className = "result";
	
  } catch(err) {
	errMsg = err.toString();
	errMsg = errMsg.substring(errMsg.indexOf('File "<unknown>"'));
	errMsg = errMsg.substring(errMsg.indexOf('File "<exec>"'));
    addToOutput(errMsg);
	msg = $("#result" + id)[0];
	msg.innerHTML = "Not quite ... try again ... if you are stuck then <a href='javascript:viewTestCases(\"" + id + "\");'>viewing the test cases</a> might help.";
	msg.className = "result";
	setOutputHidden(id, false);
  }
  
  $("#submit" + id)[0].disabled = false;
}

function viewTestCases(id) {
	msg = $("#result" + id)[0];
	result = "<p>The submit button for this task will test for the following cases:<br/><ul>"
	testCases = $("#tests" + id)[0].value.split('@@');
	for(var i = 0;i < testCases.length;i++){
		testParts = testCases[i].split("$$");
		testInp = testParts[0].split("##");
		testOut = testParts[1].replaceAll("##", "\n");	
		result += "<li>An output of <u>" + testOut.trim() + "</u>";
		if(testOut.includes("\n"))
			result += " (on separate lines)";
		if(testParts[0] != "")
			result += " for input(s) of <u>" + testInp.join("</u> and <u>") + "</u>";
		result += "</li>";		
	}
	result += "</ul></p>";
	msg.innerHTML = result;
}

window.onerror = function(msg, url, lineNo, columnNo, error) {
  try {
	addToOutput("Error occurred: to view, run page in new tab & use ctrl-shift-j to view console"); 	
  } catch(err) {}
};

function createTask() {
	var ID = "01E";
	updateTextArea(ID);	
	const code = encodeURIComponent($("#code" + ID)[0].value);
	const desc = encodeURIComponent($("#taskDescription")[0].value).replaceAll("%0A","<br/>");
	var test = " ";
	var mode = "t";
	
	if(filename.startsWith("pp")) {
		mode = "p";
	} else {	
		if($("#test1I")[0].value + $("#test1O")[0].value != "" ) {
			test = $("#test1I")[0].value.replace("\n","##") + "$$" + $("#test1O")[0].value.replace("\n","##");
			if($("#test2I")[0].value + $("#test2O")[0].value != "") {
				test += "@@" + $("#test2I")[0].value.replace("\n","##") + "$$" + $("#test2O")[0].value.replace("\n","##");
				if($("#test3I")[0].value + $("#test3O")[0].value != "") {
					test += "@@" + $("#test3I")[0].value.replace("\n","##") + "$$" + $("#test3O")[0].value.replace("\n","##");
				}
			}
		}	
	}
	
	window.location = "pagetemplate.html?code=" + CIPH(code) + "&test=" + encodeURIComponent(CIPH(test)) + "&desc=" + encodeURIComponent(CIPH(desc)) + "&mode=" + mode;
}

function activateParsons() {
	
	if(codeQS) {
		// otherwise initial will be defined on page
		initial = codeQS;
	}	

	$(document).ready(function(){
		if(typeof initial != 'undefined'){
			
			// normal Parson's
			var parson = new ParsonsWidget({
				'sortableId': 'sortable',
				'trashId': 'sortableTrash',
				'max_wrong_lines': 1,
				'feedback_cb' : displayErrors
			});
			parson.init(initial);
			parson.shuffleLines();
			$("#newInstanceLink").click(function(event){
				event.preventDefault();
				parson.shuffleLines();
			});
			$("#feedbackLink").click(function(event){
				event.preventDefault();
				var fbErrors = parson.getFeedback();
				var msg = $("#resultPP")[0];
				if (fbErrors.length == 0) {					
					msg.innerHTML = "<ul class='success'><li>Challenge completed - well done!</li></ul>";
				} else {
					msg.innerHTML = `Sorry, your solution does not meet the requirements: drag to add, rearrange or indent lines and try again.<br/>`;
				}
				msg.className = "result";				
			});
			
		} else if(typeof initialTurtle != 'undefined'){
			  var parson;
			  Sk.canvas = "studentCanvas";
			  parson = new ParsonsWidget({
				  'sortableId': 'sortable',
				  'trashId': 'sortableTrash',
				  'max_wrong_lines': 1,
				  turtleModelCode: modelTurtle,
				  'grader': ParsonsWidget._graders.TurtleGrader
			  });
			  parson.init(initialTurtle);
			  parson.shuffleLines();
			  $("#newInstanceLink").click(function(event){
				  event.preventDefault();
				  parson.shuffleLines();
			  });
			  $("#feedbackLink").click(function(event){
				  event.preventDefault();
				  var fb = parson.getFeedback();
				  var msg = $("#resultPP")[0];
				  if (fb.success) {					
					msg.innerHTML = "<ul class='success'><li>Challenge completed - well done!</li></ul>";
				  } else {
					msg.innerHTML = `Sorry, your solution does not match the model image<br/>`;
				  }
				  msg.className = "result";
			  });		
		}
	});
}
	
// display Parson's errors
function displayErrors(fb) {
		if(fb.errors.length > 0) {
			// DISABLED
			// alert(fb.errors[0]);
		}
} 
