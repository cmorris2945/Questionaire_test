<?php
if (isset($_POST['subscribe'])) {
    include("config.php");

    // Validate reCAPTCHA
    //$recaptchaSecret = '6Ldfxr0pAAAAAH6HTlKQ1GlVWkV957b3NBfXGQ7P';
    //$recaptchaResponse = $_POST['g-recaptcha-response'];

    // Make API request to verify reCAPTCHA response
    //$response = file_get_contents("https://www.google.com/recaptcha/api/siteverify?secret={$recaptchaSecret}&response={$recaptchaResponse}");
    //$response = json_decode($response);

    // Check reCAPTCHA verification result
    //if (!$response->success) {
        //$_SESSION['flashError'] = 'reCAPTCHA verification failed. Please try again.';
        //header("Location: index.php"); // Redirect back to the form
       // exit();
    //}

    // Get form data
    $email = $_POST['email']; 
    $currentDate = date('Y-m-d');
    $enq_id = 10000;
    $sql = "SELECT COUNT(*) as total FROM subsribe";
    // Execute the query
    $result = sqlsrv_query($conn, $sql);
  
    // Check if query execution was successful
    if ($result) {
      // Fetch the result as an associative array
      $row = sqlsrv_fetch_array($result, SQLSRV_FETCH_ASSOC);
      $count_enq = $row['total'];
      $enq_id = $enq_id + $count_enq;
    }
    // Construct SQL query (without prepared statement)
    $sql = "INSERT INTO subsribe (id, email_subscribe, created_date) VALUES ('" . $enq_id ."', '" . $email . "', '" . $currentDate . "')";

    // Execute SQL statement
    if (sqlsrv_query($conn,$sql) === TRUE) {
        // Email notification
        $messagesubscribe = "<html>
        <head>
          <title>drbot.health</title>
        </head>
        <body>
          <p>Hi,<br>
          You have received a new subscriber!
          </p>
          <table border='1'>
            <tr>
              <td>Email Address</td>
              <td>{$email}</td>
            </tr>
            <tr>
              <td>Form Type</td>
              <td>Subscribe Form</td>
            </tr>
          </table>
        </body>
        </html>";

        // Include PHPMailer autoload file
        require 'vendor/autoload.php';


        // Instantiate PHPMailer object
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
            $mail->Subject = 'DRBOT: New Subscriber';
            $mail->Body    = $messagesubscribe;

            // Send email
            $mail->send();

            // Redirect after successful submission
            header("Location: index.php");
            exit();
        } catch (Exception $e) {
            echo "Email sending failed. Error: {$mail->ErrorInfo}";
        }
    } else {
      die(print_r(sqlsrv_errors(), true));
    }
  
    // Close database connection
    sqlsrv_free_stmt($result);
    sqlsrv_close($conn);
}

?>


