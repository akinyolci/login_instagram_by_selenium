<!DOCTYPE html>
<html>
<body>
  <h1>Login Instagram By Selenium</h1>
  <p>This Python project uses Selenium, a popular web testing library, to automate the login process on Instagram. It provides a simple script that allows users to provide their username and password, and automatically logs them into their Instagram account using the Firefox web driver. The project also includes a test case to validate the login functionality.</p>
  
  <h2>Features</h2>
    <ul>
        <li>Automates the login process on Instagram using Python and Selenium.</li>
        <li>Provides a user-friendly interface to input the username and password.</li>
        <li>Uses the Firefox web driver for web automation.</li>
        <li>Includes a test case to validate the login functionality.</li>
        <li>Easy to integrate and extend for further automation tasks on Instagram.</li>
    </ul>
  
  <h2>Installation</h2>
  <p>Follow the steps below to install the necessary dependencies:</p>
  <ol>
    <li>Clone the repository: <code>git clone https://github.com/akinyolci/login_instagram_by_selenium.git</code></li>
    <li>Navigate to the project directory: <code>cd login_instagram_by_selenium</code></li>
    <li>Install the required packages: <code>pip install -r requirements.txt</code></li>
  </ol>
  
  <h2>Usage</h2>
  <p>Instructions on how to use the project:</p>
  <ol>
    <li>Import the necessary modules in your Python script.</li>
    <li>Create an instance of the <code>HomePage</code> class, passing the <code>browser</code> object as an argument.</li>
    <li>Call the <code>go_to_login_page()</code> method on the <code>home_page</code> object to navigate to the login page.</li>
    <li>Call the <code>login()</code> method on the <code>login_page</code> object, passing the username and password as arguments, to perform the login action.</li>
    <li>Perform any additional actions or tests using the <code>browser</code> object.</li>
    <li>Finally, close the browser using the <code>browser.close()</code> method.</li>
  </ol>
  
  <h2>Contributing</h2>
  <p>Contributions to this project are welcome! If you have any suggestions or improvements, please submit a pull request or raise an issue on the GitHub repository.</p>
  
  <h2>License</h2>
  <p>This project is licensed under the <a href="LICENSE" target="_blank">MIT License</a>.</p>
  
  <h2>Contact Information</h2>
  <p>For any questions or inquiries, please contact <a href="mailto:yolci.akin@gmail.com">Akın Yolci</a>.</p>
</body>
</html>

