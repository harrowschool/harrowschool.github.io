# Challenge

This page shows a challenge which has test cases which must be passed for the page to be marked as complete on the book report.

In the EDIT CHALLENGE area, you will notice that two tests have been provided for this challenge: when Joe is inputted, the output must be Hello Joe and when Alice is entered, the output must be Hello Alice.

It is easy to make a mistake in your JSON so if the challenge won't run after your change then copy/paste your JSON into any online JSON validator to see what the problem might be.

If the challenge runs but does not give the expected result then look at your test cases carefully. The `.*` wildcard allows the user to include a prompt in their input which will match to this 'zero or more characters' so long as it is followed finally by the correct greeting message.

Try making a change to this challenge and to the test cases and then save and preview to check it it has worked.

Note that the out string in the JSON settings will also accept `\n` for new lines. For ease of use though, our testing ignores any extra blank new lines at the very end of the output (e.g. for input `Joe`, if there is a prompt of `Enter name:` this challenge output stream would actually be `Enter name:Hello Joe\n` but your test case can just specify `.*Hello Joe`. 

Under the hood, we just convert the test out string into a regex, escaping all control sequencing except for `\n` and `.*`. 

Because we don't escape `\n`, if you have several print statements in your expected output then you will need to allow a `\n` for each in your test case matching e.g. `.*\n.*cat` would match any printed line of output followed by another printed line which ends with the text `cat`. Your test case won't match correctly if you just use `.*cat` although you can see our advanced test case syntax for more control.

Note that by default test cases are shown to the user when an incorrect submission is made. This is generally recommended to avoid user frustration when fixing their code! However to hide the input and expected output of any particular test-case from the user you can set an optional `reveal` attribute to `false` which is done on each test-case as shown:

```
"tests": [
  { "in": "Joe", "out": ".*Hello Joe", "reveal": false },
  { "in": "Alice", "out": ".*Hello Alice", "reveal": false }
]
```
