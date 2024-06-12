<body>
    <div class="cta">
        <h2 class="ctaTitle">Join the Cause</h2>
        <p class="ctaSub">Fill the form out below to get involved!</p>
    </div>

<div class="container">
    <h1>Organization Info</h1>
    <form action="submit_form.php" method="post">
        <div class="form-group">
            <input type="text" id="name" name="name" placeholder="Name" required>
        </div>
        <div class="form-group">
            <input type="email" id="email" name="email" placeholder="Email" required>
        </div>
        <div class="form-group">
            <input type="tel" id="phone" name="phone" placeholder="Phone" required>
        </div>
        <div class="form-group">
            <input type="url" id="website" name="website" placeholder="Website" required>
        </div>
        <div class="form-group">
            <textarea id="message" name="message" rows="5" placeholder="Your Why" required></textarea>
        </div>
        <div class="form-group">
            <button type="submit">Submit</button>
        </div>
        <div class="screening-info">
            Your Application will go through an internal screening process and more information may be needed.
        </div>
    </form>
</div>

    <div class="additional-info">
        <p>Additional ways to help</p>
        <a href="https://intellitect.com/">Link1</a> | <a href="https://intellitect.com/">Link2</a> | <a href="https://intellitect.com/">Link3</a>
    </div>

</body>

       <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            color: #333;
            margin: 0;
            padding: 0;
        }
        .cta {
            background-color: #333;
            color: #fff;
            padding: 50px 20px;
            text-align: center;
        }
        .ctaTitle {
            font-weight: bold;
            font-size: 30px;
        }
        .ctaSub{
            font-size: 15px;
        }
        .container { 
            width: 50%;
            margin: auto;
            background: #fff;
            padding: 20px;
            box-shadow: 0 10px 20px rgba(0, 0, 0, 0.1); /* Adjusted shadow properties */
            border-radius: 5px;
            margin-top: 20px;
        }
        h1 {
            text-align: center;
            color: #333;
            font-weight: bold;
        }
        .form-group {
            margin-bottom: 15px;
        }
        .form-group input,
        .form-group textarea {
            width: 100%;
            padding: 10px;
            box-sizing: border-box;
            margin-top: 5px;
            border: 1px solid #ccc;
            background-color: #fff;
            color: #333;
            border-radius: 3px;
            resize: none;
        }
        .form-group input[type="text"],
        .form-group input[type="email"],
        .form-group input[type="tel"],
        .form-group input[type="url"],
        .form-group textarea {
            width: 100%;
            padding: 10px;
            box-sizing: border-box;
            margin-top: 5px;
            border: 1px solid #ccc;
            background-color: #fff;
            color: #333;
            border-radius: 3px;
            resize: none;
            transition: all 0.3s ease; /* Add transition */
        }

        .form-group input[type="text"]:hover,
        .form-group input[type="email"]:hover,
        .form-group input[type="tel"]:hover,
        .form-group input[type="url"]:hover,
        .form-group textarea:hover {
            transform: scale(1.025); /* Scale up on hover */
            transition: all 0.5s ease; /* Add transition */
        }
        .form-group button {
            display: block;
            width: 100%;
            padding: 10px;
            background-color: #333;
            color: #fff;
            border: none;
            cursor: pointer;
            margin-top: 10px;
            border-radius: 3px;
            font-weight: bold;
            transition: all 0.3s ease; /* Add transition */
        }

        .form-group button:hover {
            background-color: #555;
            transform: scale(1.025); /* Scale up on hover */
            transition: all 0.5s ease; /* Add transition */
        }
        .screening-info {
            font-size: smaller;
            text-align: center;
            color: #888;
            font-style: italic;
        }
        .form-group button:hover {
            background-color: #555;
        }
        .additional-info {
            text-align: center;
            color: #fff;
            margin-top: 20px;
            background-color: #333;
        }
        .additional-info p {
            margin-bottom: 10px;
        }
        .additional-info a {
            color: #fff;
            text-decoration: none;
            font-weight: normal;
            margin: 0 50px;
        }
        .additional-info a:hover {
            color: grey;
        }
    </style>