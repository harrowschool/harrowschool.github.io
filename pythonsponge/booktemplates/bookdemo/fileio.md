# Advanced Test Cases for File IO

Additional files can be added to the python runtime (at the root directory) using the following example json as shown in this challenge setup:

```json
"additionalFiles": [
	{
	  "filename": "numbers.txt",
	  "visible": false
	}
]
```

A further customisation for an advanced test case is to match out patterns against a file that should have been created by the user's code.

This is achieved by setting the `typ` of an advanced test case to be `f+` (for file must contain) or `f-` (for file must not contain) along with a `filename` attribute for the name of the file.

E.g. Complete the code to write the first n positive odd numbers to the specified file. The test-case shows how to use advanced testing to test the contents of the file after execution.

```json
"tests": [
	{
		"in": ["5"],
		"out": [
			{"typ": "f+", "pattern": "1\\n3\\n5\\n7\\n9", "filename":"numbers.txt"},
			{"typ": "f-", "pattern": "1\\n3\\n5\\n7\\n9\\n11", "filename":"numbers.txt"}
		]
	}
]
```