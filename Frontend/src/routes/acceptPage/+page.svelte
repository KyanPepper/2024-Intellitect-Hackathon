<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Organization Applications</title>
</head>
<body>
    <div class="cta">
        <h2 class="ctaTitle">Organization Monitor</h2>
        <p class="ctaSub">Use to add Organizations to map and system</p>
    </div>

    <div class="content">
        <div class="container">
            <div class="org-list">
                <h2>Current Organizations</h2>
                <div class="org">
                    <span>Organization 1</span>
                    <button class="check-mark-button red">X</button>
                </div>
                <div class="org">
                    <span>Organization 2</span>
                    <button class="check-mark-button red">X</button>
                </div>
                <div class="org">
                    <span>Organization 3</span>

                    <button class="check-mark-button red">X</button>
                </div>
            </div>
            
            <div class="divider">
                <hr>
            </div>
            
            <div class="pending-list">
                <h2>Pending Organizations</h2>
                <div class="pending-org">
                    <span>Organization 4</span>
                    <button class="check-mark-button green">&#10004;</button>
                    <button class="check-mark-button red">X</button>
                </div>
                <div class="pending-org">
                    <span>Organization 5</span>
                    <button class="check-mark-button green">&#10004;</button>
                    <button class="check-mark-button red">X</button>
                </div>
                <div class="pending-org">
                    <span>Organization 6</span>
                    <button class="check-mark-button green">&#10004;</button>
                    <button class="check-mark-button red">X</button>
                </div>
            </div>
        </div>
    </div>

    <div class="additional-info">
        <p>Cool info and stuff</p>
    </div>

</body>

<style>
        /* Basic CSS for demonstration purposes */
        body, html {
            margin: 0;
            padding: 0;
            height: 100%;
        }
        .container {
            display: flex;
            justify-content: center;
            align-items: center;
            flex-direction: column;
            height: 100%;
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
        .ctaSub {
            font-size: 15px;
        }
        .content {
            display: flex;
            flex-direction: column;
            align-items: center;
            flex-grow: 1;
            width: 100%;
        }
        .org-list, .pending-list {
            flex-basis: 45%;
            margin: 10px;
            padding: 20px;
            border: 1px solid #ccc;
            border-radius: 5px;
            text-align: center;
        }
        .org-list h2, .pending-list h2 {
            font-size: 1.5em;
            font-weight: bold;
            text-decoration: underline;
            margin-bottom: 10px;
        }
        .org-list .org, .pending-list .pending-org {
            margin-bottom: 10px;
            font-size: 1.2em;
        }
        .divider {
            width: 100%;
            margin-top: 20px; /* Adjusted margin */
            margin-bottom: 20px; /* Adjusted margin */
        }
        .divider hr {
            border: none;
            border-top: 1px solid #ccc;
            width: 50%;
        }
        .check-mark-button {
            display: inline-block;
            width: 30px;
            height: 30px;
            border: none;
            border-radius: 50%;
            text-align: center;
            font-size: 16px;
            line-height: 30px;
            cursor: pointer;
            transition: background-color 0.3s ease;
            margin: 0 5px; /* Added margin */
        }
        .check-mark-button.green {
            background-color: green;
            color: white;
        }
        .check-mark-button.red {
            background-color: red;
            color: white;
        }
        .additional-info {
            flex-shrink: 0; /* Prevent additional-info from shrinking */
            flex-grow: 1; /* Let additional-info grow to fill remaining space */
            width: 100%; /* Make sure it spans the entire width */
            text-align: center;
            color: #fff;
            margin-top: auto; /* Push it to the bottom */
            background-color: #333;
        }
        .additional-info p {
            margin-bottom: 10px;
        }
</style>