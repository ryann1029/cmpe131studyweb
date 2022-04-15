const isAlpha = str => /^([a-zA-Z0-9]|\s)*$/.test(str); // Using RegEx to detect any letters.

const calculate = () => {
  
    // Getting input from user into height variable.
    let assignment = document.querySelector("#assignment").value;
    let score = document.querySelector("#score").value;
    let total_points = document.querySelector("#pointspossible").value;
    let weight = document.querySelector("#weight").value;
    let grades = "";
    
    // Input is string so typecasting is necessary. */
    let total_score = parseFloat(score);
    
    // Checking the condition for the providing the 
    // grade to student based on percentage
    let percentage = ((total_score/total_points) * 100);
    
    

    // checking to see if the user added a correct value for weight 
    if (weight < 0 || weight > 100)
      document.querySelector("#showdata").innerHTML = `
      <div style="color: red;">The weight entered must be between 0% and 100%.</div>
      `;
    else {

    if (percentage <= 100 && percentage >= 90) {
      grades = "A";
    } else if (percentage < 90 && percentage >= 80) {
      grades = "B";
    } else if (percentage < 80 && percentage >= 70) {
      grades = "C";
    } else if (percentage < 70 && percentage >= 60) {
      grades = "D";
    } else {
      grades = "F";
    }

    // Checking if inputs is either empty, contains characters not part of the alphabet, or something otherwise.
    if (assignment == "") {
    document.querySelector("#showdata").innerHTML = `
    <div style="color: red;">Please enter all the fields.</div>
    `;
        
    } else if(!isAlpha(assignment)){
        document.querySelector("#showdata").innerHTML = `
        <div style="color: red;">No special characters are allowed for course name. Correct your inputs.</div>
        `;

    } else if (!weight) {
      document.querySelector("#showdata").innerHTML = `
      <div style="color: red;">No weight inputted.</div>
      `;

    } else if (!score) {
      document.querySelector("#showdata").innerHTML = `
      <div style="color: red;">No score inputted.</div>
      `;

    } else if (!total_points) {
      document.querySelector("#showdata").innerHTML = `
      <div style="color: red;">No total points inputted.</div>
      `;

    } else {
    // Checking the condition for the fail and pass
        if (percentage >= 70) {
            document.querySelector("#showdata").innerHTML = 
            `You have ${total_score} points out of ${total_points}, which is a percentage of ${percentage}%.<br/> 
            <b>Your grade is ${grades}, <u>a passing grade</u></b>.`;

        } else {
            document.querySelector("#showdata").innerHTML = 
            `You have ${total_score} points out of ${total_points}, which is a percentage of ${percentage}%.<br/> 
            <b>Your grade is ${grades}. <u>Unfortunately, you failed</u></b>.`
        }
    }
  }
};