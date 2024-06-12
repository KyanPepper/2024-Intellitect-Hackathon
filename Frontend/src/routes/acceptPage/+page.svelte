<script>
    import axios from "axios";

    const backendprefix = "http://127.0.0.1:5000/";

    // @ts-ignore
    let data = [];
    // Example of an axios request
    axios.get(backendprefix + "getresources")
        .then((response) => {
            data = response.data;
        })
        .catch((error) => {
            console.error(error);
        });

        const pendingApplications = [
            {
                organization: "Organization A",
                description: "Description A",
                address: "Address A",
                phoneNumber: "123-456-7890",
                email: "orga@example.com",
                website: "www.orga.com",
                category_id: 1,
                category: { id: 1, name: "Category A" } 
            },
            {
                organization: "Organization B",
                description: "Description B",
                address: "Address B",
                phoneNumber: "987-654-3210",
                email: "orgb@example.com",
                website: "www.orgb.com",
                category_id: 2,
                category: { id: 2, name: "Category B" } 
            },
            // Add more pending applications as needed
        ];

    // @ts-ignore
    function addApplicant() {
        axios.post(backendprefix + "approveapplication")
            .then((response) => {
                
            })
            .catch((error) => {
                console.error(error);
            });
        }
</script>

<div class="cta">
    <h2 class="ctaTitle">Organization Monitor</h2>
    <p class="ctaSub">Use to add Organizations to map and system.</p>
</div>

<div class="content">
    <div class="container">
        <div class="org-list">
            <h2>Current Organizations</h2>
            <div class="seperator">
                <hr>
            </div>
            {#each data as org}
                <div class="org">
                    <span>{org.name}</span>
                    <button class="check-mark-button red">X</button>
                </div>
            {/each}
        </div>
        <div class="divider">
            <hr>
        </div>
        <div class="pending-list">
            <h2>Pending Organizations</h2>
            <div class="seperator">
                <hr>
            </div>
                {#each pendingApplications as pendingOrg}
                    <div class="pending-org">
                        <span>{pendingOrg.organization}</span>
                        <button class="check-mark-button green">&#10004;</button>
                        <button class="check-mark-button red">X</button>
                    </div>
                {/each}
            </div>
        </div>
</div>

<div class="additional-info">
    <p>"To me it would not seem that a Steward who faithfully surrenders his charge is not diminished in love or in honour."</p>
</div>

<style>
    /* Basic CSS for demonstration purposes */
    body {
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
            margin: auto;
            padding: 20px;
            margin-top: 20px;
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
        .org:hover,
        .pending-org:hover {
            transform: scale(1.1); /* Enlarge on hover */
            transition: transform 0.3s ease; /* Add smooth transition */
        }
        .org-list .org,
        .pending-list .pending-org {
            margin-top: 5px;
            margin-bottom: 10px;
            font-size: 1.2em;
            transition: transform 0.3s ease; /* Add transition for smooth scaling */
        }

        .org:hover,
        .pending-org:hover {
            transform: scale(1.1); /* Enlarge on hover */
        }
        .org-list, .pending-list {
            flex-basis: 45%;
            margin: 10px;
            padding: 20px;
            border: 2px solid #ccc; /* Increased border size */
            border-radius: 10px; /* Rounded corners */
            text-align: center;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1); /* Added box shadow */
        }
        .org-list h2, .pending-list h2 {
            font-size: 1.5em;
            font-weight: normal;
            margin-bottom: 2px;
        }
        .org-list .org, .pending-list .pending-org {
            margin-top: 5px;
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
            border-top: 1px solid #333;
            width: 100%;
        }
        .seperator {
            width: 100%;
        }
        .seperator hr {
            border-top: .5px solid #333;
            width: 100%;
        }
        .check-mark-button {
            display: inline-block;
            width: 23px;
            height: 23px;
            border: none;
            border-radius: 50%;
            text-align: center;
            font-size: 14px;
            line-height: 23px;
            cursor: pointer;
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
            flex-grow: 1; /* Let additional-info grow to fill remaining space */
            width: 100%; /* Make sure it spans the entire width */
            text-align: center;
            color: #fff;
            margin-top: auto; /* Push it to the bottom */
            margin-bottom: auto; /* Reset margin bottom to ensure it fills the remaining space */
            padding: 20px; /* Add padding for better appearance */
            background-color: #333;
        }
        .additional-info p {
            margin-bottom: 10px;
            color:light-gray;
            font-style: italic;
        }
</style>

