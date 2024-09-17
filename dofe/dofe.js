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
    const body = `Dear ${assessorName},%0A%0AThank you for agreeing to be my assessor for the ${section} section of my ${award} Duke of Edinburgh Award. Now that I have completed the required ${duration} on this activity, I would like to ask if you could fill out an assessor report for me?%0A%0AHere are the required steps to complete an assessor report%0A%0A1. Go to https://www.dofe.org/assessor%0A2. Enter your email address, then enter the verification code when you receive it.%0A3. Enter my details as follows:%0A%09• Participant’s ID number: ${edofeID}%0A%09• Level: ${award}%0A%09• Section you are assessing: ${section}%0A4. Then fill out the assessor report form on the next page.%0A%0AHere is some further guidance on how to write assessor reports should you need it:%0A%0Ahttps://www.dofe.org/wp-content/uploads/2019/12/Writing-Assessor-Reports-Full-Sections.pdf%0A%0AThank you again for being my assessor and helping me to complete my ${award} Duke of Edinburgh Award.%0A%0ABest wishes,%0A%0A${name}`

    const url = `mailto:${assessorEmail}?subject=${encodeURIComponent("Request for Assessor Report")}&body=${body}`
    
    // Open the constructed URL in a new window or tab
    window.open(url, '_blank');
}