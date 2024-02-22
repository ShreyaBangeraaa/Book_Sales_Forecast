<?php

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Check if the email field is set and not empty
    if (isset($_POST['email']) && !empty($_POST['email'])) {
        $email = $_POST['email'];

        // Send email
        $to = $email;
        $subject = 'Welcome to Our Website';
        $message = 'Thank you for registering!';
        $headers = 'From: your@example.com' . "\r\n" .
                   'Reply-To: your@example.com' . "\r\n" .
                   'X-Mailer: PHP/' . phpversion();

        // Check if the mail function returns true (email sent successfully)
        if (mail($to, $subject, $message, $headers)) {
            echo "Registration successful! Thank you for registering.";
        } else {
            echo "Failed to send email. Please try again.";
        }
    } else {
        echo "Email address is not provided.";
    }
} else {
    echo "Invalid request method.";
}

?>
