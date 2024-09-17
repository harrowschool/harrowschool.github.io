function openEmail() {
    // Get form values
    const name = document.getElementById('yourName').value;
    const award = document.getElementById('award').value;
    const section = document.getElementById('section').value;
    const duration = document.getElementById('duration').value;
    const edofeID = document.getElementById('edofeID').value;
    const assessorName = document.getElementById('assessorName').value;
    const assessorEmail = document.getElementById('assessorEmail').value;

    // Construct the URL with query parameters
    const body = `<p>Dear ${name},

<p>Thank you for agreeing to be my assessor for the ${section} section of my ${award} Duke of Edinburgh Award. Now that I have completed the required ${duration} on this activity, I would like to ask if you could fill out an assessor report for me?<p>

Here are the required steps to complete an assessor report

1. Go to [dofe.org/assessor](https://www.dofe.org/assessor)
2. Enter your email address, then enter the verification code when you receive it.
3. Enter my details as follows:
	- Participant’s ID number: ${edofeID}
	- Level: ${award}
	- Section you are assessing: ${section}
4. Then fill out the assessor report form on the next page. 

Here is some [further guidance](https://www.dofe.org/wp-content/uploads/2019/12/Writing-Assessor-Reports-Full-Sections.pdf) on how to write assessor reports should you need it.

Thank you again for being my assessor and helping me to complete my ${award} Duke of Edinburgh Award.

Best wishes,

${name}
`

    const url = `mailto:${assessorEmail}?subject=${encodeURIComponent("Request for Assessor Report")}&body=${body}`
    
    // Open the constructed URL in a new window or tab
    window.open(url, '_blank');
}