# Advanced Test Cases for Evaluated Statements

A further use of additional test cases are to run statements (e.g. mini unit-tests) against the user's completed code as shown in the setup for this challenge.

When `typ` is set to `s+` or `s-` then the output match pattern is compared not to the output from the code but from the result when running the provided `statement` expression which will be evaluated on the completion of running the user's code.

```json
"tests": [
	{
		"in": [],
		"out": [
			{"typ": "s+", "pattern": "21", "statement":"getNextMultipleOfSeven(15)"},
			{"typ": "s-", "pattern": "14", "statement":"getNextMultipleOfSeven(14)"},                        
			{"typ": "s+", "pattern": "42", "statement":"getNextMultipleOfSeven(41)"}
		]
	}
]
```

For example: complete the function to take an integer as parameter and return the next multiple of 7 which is strictly greater than it.
