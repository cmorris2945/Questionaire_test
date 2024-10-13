<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>drbot.health</title>
<style>
  body {
   
    background-color: #f4f4f4;
    margin: 0;
    padding: 0;
    display: flex;
    justify-content: center;
    align-items: center;
  }

  form {
    background-color: #fff;
    padding: 20px;
    border-radius: 8px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    max-width: 600px;
    width: 100%;
  }

  label {
    font-weight: bold;
  }

  input[type="text"],
  input[type="email"],
  select,
  textarea {
    width: calc(100% - 22px);
    padding: 10px;
    margin: 5px 0;
    border: 1px solid #ccc;
    border-radius: 4px;
    box-sizing: border-box;
    font-size: 16px;
  }

  input[type="radio"],
  input[type="checkbox"] {
    margin-right: 5px;
  }

  input[type="submit"] {
    background-color: #4CAF50;
    color: white;
    padding: 14px 20px;
    margin: 8px 0;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    font-size: 16px;
  }

  input[type="submit"]:hover {
    background-color: #45a049;
  }

  #testingOptions,
  #noOpinionReason,
  #furtherDiscussion {
    margin-left: 20px;
  }

  @media only screen and (max-width: 600px) {
    input[type="text"],
    input[type="email"],
    select,
    textarea {
      width: 100%;
    }

    #testingOptions,
    #noOpinionReason,
    #furtherDiscussion {
      margin-left: 0;
    }
  }
</style>
</head>
<body>

<form action="#" method="post">
<label for="location">Name:</label><br>
  <input type="text" id="name" name="name" placeholder="Name" required><br><br>

  <label for="location">Location:</label><br>
  <input type="text" id="location" name="location" placeholder="Location" required><br>

  <label>Gender:</label><br>
  <input type="radio" id="male" name="gender" value="male" required>
  <label for="male">Male</label>
  <input type="radio" id="female" name="gender" value="female">
  <label for="female">Female</label>
  <input type="radio" id="other" name="gender" value="other">
  <label for="other">Other</label><br><br>

  <label for="age">Age Bracket:</label><br>
  <select id="age" name="age" required>
    <option value="<25">Less than 25 years</option>
    <option value="25-35">25 - 35 years</option>
    <option value="36-45">36 - 45 years</option>
    <option value="46-60">46 - 60 years</option>
    <option value="60+">60 and above</option>
  </select><br><br>

  <label for="email">Email Address:</label><br>
  <input type="email" id="email" name="email" placeholder="Email Address" required><br><br>

  <label>Are you the patient or are you related to the patient?</label><br>
  <input type="radio" id="patient" name="relation" value="patient" required>
  <label for="patient">Patient</label>
  <input type="radio" id="related" name="relation" value="related">
  <label for="related">Related</label><br><br>

  <label>Is the cancer diagnosed or suspected?</label><br>
  <input type="radio" id="diagnosed" name="diagnosis" value="diagnosed" required>
  <label for="diagnosed">Diagnosed</label>
  <input type="radio" id="suspected" name="diagnosis" value="suspected">
  <label for="suspected">Suspected</label>
  <input type="radio" id="notsure" name="diagnosis" value="notsure">
  <label for="notsure">Not Sure</label><br><br>

  <label>Have you done any testing?</label><br>
  <input type="radio" id="testingYes" name="testing" value="yes">
  <label for="testingYes">Yes</label>
  <input type="radio" id="testingNo" name="testing" value="no">
  <label for="testingNo">No</label><br><br>

  <div id="testingOptions" style="display: none;">
    <label>Which tests have you done?</label><br>
    <input type="checkbox" id="bloodwork" name="tests[]" value="bloodwork">
    <label for="bloodwork">Blood work</label>
    <input type="checkbox" id="biopsy" name="tests[]" value="biopsy">
    <label for="biopsy">Biopsy</label>
    <input type="checkbox" id="scans" name="tests[]" value="scans">
    <label for="scans">Radiological scans</label><br><br>
  </div>

  <label>Have you gotten an expert second opinion?</label><br>
  <input type="radio" id="opinionYes" name="opinion" value="yes">
  <label for="opinionYes">Yes</label>
  <input type="radio" id="opinionNo" name="opinion" value="no">
  <label for="opinionNo">No</label><br><br>

  <div id="noOpinionReason" style="display: none;">
    <label for="noOpinionReason">If no, why not?</label><br>
    <input type="text" id="noOpinionReason" name="noOpinionReason"><br><br>
  </div>

  <label>Are you interested in getting another expert opinion?</label><br>
  <input type="radio" id="interestedYes" name="interested" value="yes">
  <label for="interestedYes">Yes</label>
  <input type="radio" id="interestedNo" name="interested" value="no">
  <label for="interestedNo">No</label><br><br>

  <div id="furtherDiscussion" style="display: none;">
    <label>Are you interested in us getting in touch with you for a detailed discussion?</label><br>
    <input type="radio" id="discussionYes" name="discussion" value="yes">
    <label for="discussionYes">Yes</label>
    <input type="radio" id="discussionNo" name="discussion" value="no">
    <label for="discussionNo">No</label><br><br>
  </div>

  <input type="submit" value="Submit">
</form>

<script>
  const testingYesRadio = document.getElementById('testingYes');
  const testingOptionsDiv = document.getElementById('testingOptions');
  testingYesRadio.addEventListener('change', function() {
    if (this.checked) {
      testingOptionsDiv.style.display = 'block';
    } else {
      testingOptionsDiv.style.display = 'none';
    }
  });

  const opinionNoRadio = document.getElementById('opinionNo');
  const noOpinionReasonDiv = document.getElementById('noOpinionReason');
  opinionNoRadio.addEventListener('change', function() {
    if (this.checked) {
      noOpinionReasonDiv.style.display = 'block';
    } else {
      noOpinionReasonDiv.style.display = 'none';
    }
  });

  const interestedYesRadio = document.getElementById('interestedYes');
  const furtherDiscussionDiv = document.getElementById('furtherDiscussion');
  interestedYesRadio.addEventListener('change', function() {
    if (this.checked) {
      furtherDiscussionDiv.style.display = 'block';
    } else {
      furtherDiscussionDiv.style.display = 'none';
    }
  });
</script>

</body>
</html>
