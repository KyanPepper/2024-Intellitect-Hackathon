<body>
    <div class="container">
        <h1>Contact Us</h1>
        <form action="submit_form.php" method="post">
            <div class="form-group">
                <label for="name">Name:</label>
                <input type="text" id="name" name="name" required>
            </div>
            <div class="form-group">
                <label for="email">Email:</label>
                <input type="email" id="email" name="email" required>
            </div>
            <div class="form-group">
                <label for="phone">Phone:</label>
                <input type="tel" id="phone" name="phone">
            </div>
            <div class="form-group">
                <label for="website">Link:</label>
                <input type="tel" id="url" name="website">
            </div>
            <div class="form-group">
                <label for="message">Message:</label>
                <textarea id="message" name="message" rows="5" required></textarea>
            </div>
            <div class="form-group">
                <button type="submit">Submit</button>
            </div>
        </form>
    </div>
</body>

    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #333;
            color: #fff;
            margin: 0;
            padding: 0;
        }
        .container {
            width: 50%;
            margin: auto;
            background: #444;
            padding: 20px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.3);
            margin-top: 50px;
            border-radius: 10px;
        }
        h1 {
            text-align: center;
            color: #33ffff;
        }
        .form-group {
            margin-bottom: 15px;
        }
        .form-group label {
            display: block;
            color: #33ffff;
        }
        .form-group input,
        .form-group textarea {
            width: 100%;
            padding: 10px;
            box-sizing: border-box;
            margin-top: 5px;
            border: 2px solid #33ffff;
            background-color: #555;
            color: #fff;
            border-radius: 5px;
        }
        .form-group button {
            display: block;
            width: 100%;
            padding: 10px;
            background-color: #33ffff;
            color: #333;
            border: none;
            cursor: pointer;
            margin-top: 10px;
            border-radius: 5px;
            font-weight: bold;
        }
        .form-group button:hover {
            background-color: #1acfcf;
        }
    </style>