<?php
if (isset($_POST['contact_form'])) {
    include("config.php");

  // Validate reCAPTCHA
  $recaptchaSecret = '6Ldfxr0pAAAAAH6HTlKQ1GlVWkV957b3NBfXGQ7P';
  $recaptchaResponse = $_POST['g-recaptcha-response'];

  // Make API request to verify reCAPTCHA response
  $response = file_get_contents("https://www.google.com/recaptcha/api/siteverify?secret={$recaptchaSecret}&response={$recaptchaResponse}");
  $response = json_decode($response);

  // Check reCAPTCHA verification result
  if (!$response->success) {
    // reCAPTCHA verification failed
    $_SESSION['flashError'] = 'reCAPTCHA verification failed. Please try again.';
    //header("Location: index.php"); // Redirect back to the form
    //exit();
  }
  //end captcha code start

  // Form data
  $email = $_POST['email'];
  $message = $_POST['message'];
  $currentDate = date('Y-m-d');

  // SQL to insert data into database
  $sql = "INSERT INTO contact_form (email, message, created_date) VALUES ('" . $email . "', '" . $message . "', '" . $currentDate . "')";

  // Execute SQL statement
  if ($conn->query($sql) === TRUE) {
    // Email notification
    $messageform = "<html>
<head>
  <title>drbot.health</title>
</head>
<body>
  <p>Hi,<br>
  You have received a new message!
  </p>
  <table border='1'>
    <tr>
      <td>Email Address</td>
      <td>$email</td>
    </tr>
    <tr>
      <td>Message</td>
      <td>$message</td>
    </tr>
    <tr>
    <td>Form Type</td>
    <td>Message Form</td>
  </tr>
  </table>
</body>
</html>";

    // Include PHPMailer autoload file
    require 'vendor/autoload.php';

    // Instantiate PHPMailer object
    $mail = new PHPMailer\PHPMailer\PHPMailer(true);

	  
	  
    try {
      // Server settings
      $mail->isSMTP(); // Set mailer to use SMTP
      $mail->Host       = 'smtp.gmail.com'; // SMTP server
      $mail->SMTPAuth   = true; // Enable SMTP authentication
      $mail->Username   = 'info@drbot.health'; // SMTP username
      $mail->Password   = 'vzic wmbq jrtv zlvl'; // SMTP password
      $mail->SMTPSecure = 'tls'; // Enable TLS encryption; `ssl` also accepted
      $mail->Port       = 587; // TCP port to connect to
      // Sender and recipient settings
      $mail->setFrom('info@drbot.health', 'drbot.health');
      $mail->addAddress('kanu@drbot.health'); // Add a recipient
      $mail->addCC('kanua1@icloud.com');
      $mail->addBCC('info@drbot.health');

      // Email content
      $mail->isHTML(true); // Set email format to HTML
      $mail->Subject = 'DRBOT: New Contact Inquiry';
      $mail->Body    = $messageform;

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
