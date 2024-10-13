<?php
if (isset($_POST['inquiry_witin'])) {
  include("config.php");

  // Validate reCAPTCHA
  $recaptchaSecret = '6Ldfxr0pAAAAAH6HTlKQ1GlVWkV957b3NBfXGQ7P';
  $recaptchaResponse = $_POST['g-recaptcha-response'];

  // Make API request to verify reCAPTCHA response
  $response = file_get_contents("https://www.google.com/recaptcha/api/siteverify?secret={$recaptchaSecret}&response={$recaptchaResponse}");
  $response = json_decode($response);

  // Check reCAPTCHA verification result
  if (!$response->success) {
    $_SESSION['flashError'] = 'reCAPTCHA verification failed. Please try again.';
    //header("Location: index.php"); // Redirect back to the form
    exit();
  }

  // Form data
  $name = $_POST['name'];
  $location = $_POST['location'];
  $age = $_POST['age'];
  $email = $_POST['email'];
  $gender = $_POST['gender'];
  $relation = $_POST['relation'];
  $diagnosis = $_POST['diagnosisType'];
  $specify_location_of_cancer = $_POST['locationInput'];
  $insurance = $_POST['insurance'];
  $mobile_number = $_POST['mobile_number'];
  $testing = isset($_POST['testing']) ? $_POST['testing'] : 'no';
  $tests = isset($_POST['tests']) ? implode(', ', $_POST['tests']) : '';
  $opinion = $_POST['opinion'];
  $noOpinionReason = isset($_POST['noOpinionReason']) ? $_POST['noOpinionReason'] : '';
  $interested = $_POST['interested'];
  $remark = $_POST['remark'];
  $discussion = isset($_POST['discussion']) ? $_POST['discussion'] : '';
  $currentDate = date('Y-m-d');
  $enq_id = 10000;

  // SQL query to get count of records in 'inquiry_within' table
  $sql = "SELECT COUNT(*) as total FROM inquiry_within";
  // Execute the query
  $result = mysqli_query($conn, $sql);

  // Check if query execution was successful
  if ($result) {
    // Fetch the result as an associative array
    $row = mysqli_fetch_assoc($result);
    $count_enq = $row['total'];
    $enq_id = $enq_id + $count_enq;
  }

  // SQL to insert data into database
  $sql_inquiry = "INSERT INTO inquiry_within (enq_id, name, mobile_number, specify_location_of_cancer, insurance, remark,  location, age, email, gender, relation, diagnosis, testing, tests, opinion, noOpinionReason, interested, discussion, date) 
        VALUES ('$enq_id', '$name', '$mobile_number', '$specify_location_of_cancer', '$insurance', '$remark',  '$location', '$age', '$email', '$gender', '$relation', '$diagnosis', '$testing', '$tests', '$opinion', '$noOpinionReason', '$interested', '$discussion', '$currentDate')";


  if ($conn->query($sql_inquiry) === TRUE) {
    // Prepare mail content
    $messagecontent = "<html>
    <head>
      <title>Patient Details</title>
    </head>
    <body>
      <p>Hi,<br>
      You have received a new inquiry!
      </p>
      <table border='1'>
        <tr>
          <td><strong>Patient Name</strong></td>
          <td><strong>Patient Data</strong></td>
        </tr>
        <tr>
          <td>Patient ID</td>
          <td>$enq_id</td>
        </tr>
        <tr>
          <td>Name</td>
          <td>$name</td>
        </tr>
        <tr>
          <td>Location</td>
          <td>$location</td>
        </tr>
        <tr>
          <td>Age Bracket</td>
          <td>$age</td>
        </tr>
        <tr>
          <td>Email Address</td>
          <td>$email</td>
        </tr>
        <tr>
          <td>Telephone Number</td>
          <td>$mobile_number</td>
        </tr>
        <tr>
          <td>Gender</td>
          <td>$gender</td>
        </tr>
        <tr>
          <td>Are you the patient or are you related to the patient?</td>
          <td>$relation</td>
        </tr>
        <tr>
          <td>Is the cancer diagnosed or suspected?</td>
          <td>$diagnosis</td>
        </tr>
        
        <tr>
          <td>Specify location of cancer</td>
          <td>$specify_location_of_cancer</td>
        </tr>
        <tr>
          <td>Have you done any testing?</td>
          <td>$testing</td>
        </tr>
        <tr>
        <td>Have you done any testing?</td>
        <td>$tests</td>
      </tr>
      <tr>
        <td>Do you have medical insurance?</td>
        <td>$insurance</td>
      </tr>
        <tr>
          <td>Have you gotten an expert second opinion?</td>
          <td>$opinion</td>
        </tr>
        <tr>
          <td>Have you gotten an expert second opinion->Why not?</td>
          <td>$noOpinionReason</td>
        </tr>
        <tr>
          <td>Are you interested in getting another expert opinion?</td>
          <td>$interested</td>
        </tr>
        <tr>
        <td>Are you interested in us getting in touch with you for a detailed discussion?</td>
        <td>$discussion</td>
      </tr>
      <tr>
        <td>Special Remark</td>
        <td>$remark</td>
      </tr>
      </table>
    </body>
    </html>";

    // Include PHPMailer autoload file
    require 'vendor/autoload.php';

    // Instantiate PHPMailer object
    $mail = new PHPMailer\PHPMailer\PHPMailer(true);

    try {
      // SMTP settings
      $mail->isSMTP();
      $mail->Host       = 'smtp.gmail.com'; // SMTP server
      $mail->SMTPAuth   =  true; // Enable SMTP authentication
      $mail->Username   = 'info@drbot.health'; // SMTP username
      $mail->Password   = 'vzic wmbq jrtv zlvl'; // SMTP password
      $mail->SMTPSecure = 'tls'; // Enable TLS encryption; `ssl` also accepted
      $mail->Port       =  587; // TCP port to connect to

      // Sender and recipient settings
      $mail->setFrom('info@drbot.health', 'drbot.health');
      $mail->addAddress('kanu@drbot.health'); // Add a recipient
      $mail->addCC('kanua1@icloud.com');
      $mail->addBCC('info@drbot.health');

      $mail->isHTML(true);
      $mail->Subject = 'DRBOT: New Patient Inquiry #' . $enq_id;
      $mail->Body    = $messagecontent;

      // Send email
      $mail->send();
      // Redirect after successful submission
      header("Location: index.php");
      exit();
    } catch (Exception $e) {
      echo "Email sending failed. Error: {$e->getMessage()}";
    }
  } else {
    echo "Error: " . $conn->error;
  }

  // Close database connection
  $conn->close();
}

?>
