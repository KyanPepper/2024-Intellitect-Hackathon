<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Intro Banner with Overlay Title</title>
    <link href="/dist/output.css" rel="stylesheet">
</head>
<body style="background-color: #F8F8F8;">
    <header class="relative w-full h-64">
        <img src="https://static.spokanecity.org/photos/2013/03/03/spokane/16x10/Full/spokane.jpg" alt="Banner Image" class="w-full h-full object-cover">
        <div class="absolute inset-0 flex items-center justify-center bg-black bg-opacity-50">
            <h1 class="fade-in text-4xl font-bold text-white">Welcome to SpokaneOutreach</h1>
        </div>
    </header>
    <div class="flex items-center justify-center text-center p-4 mt-8">
        <p class="text-lg text-gray-700 max-w-xl">
            The community of Spokane cares deeply about providing resources for those who need a little extra support.
            Whether you are looking for financial aid, food, shelter, healthcare, or some other type of assistance,
            you've come to the right spot.
        </p>
    </div>
    <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-6 gap-4 p-4">
        <!-- First Square -->
        <div class="bg-purple-800 text-white p-4 flex flex-col items-center justify-center h-32">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6 mb-2" viewBox="0 0 20 20" fill="currentColor">
                <!-- SVG content -->
            </svg>
            <p class="text-lg font-semibold text-center">Food Resources</p>
        </div>
        <!-- Second Square -->
        <div class="bg-indigo-900 text-white p-4 flex flex-col items-center justify-center h-32">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6 mb-2" viewBox="0 0 20 20" fill="currentColor">
                <!-- SVG content -->
            </svg>
            <p class="text-lg font-semibold text-center">Shelter</p>
        </div>
        <!-- Third Square -->
        <div class="bg-teal-600 text-white p-4 flex flex-col items-center justify-center h-32">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6 mb-2" viewBox="0 0 20 20" fill="currentColor">
                <!-- SVG content -->
            </svg>
            <p class="text-lg font-semibold text-center">Financial Aid</p>
        </div>
        <!-- Fourth Square -->
        <div class="bg-green-700 text-white p-4 flex flex-col items-center justify-center h-32">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6 mb-2" viewBox="0 0 20 20" fill="currentColor">
                <!-- SVG content -->
            </svg>
            <p class="text-lg font-semibold text-center">Healthcare</p>
        </div>
        <!-- Fifth Square -->
        <div class="bg-yellow-700 text-white p-4 flex flex-col items-center justify-center h-32">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6 mb-2" viewBox="0 0 20 20" fill="currentColor">
                <!-- SVG content -->
            </svg>
            <p class="text-lg font-semibold text-center">Rehabilitation Centers</p>
        </div>
        <!-- Sixth Square -->
        <div class="bg-red-800 text-white p-4 flex flex-col items-center justify-center h-32">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6 mb-2" viewBox="0 0 20 20" fill="currentColor">
                <!-- SVG content -->
            </svg>
            <p class="text-lg font-semibold text-center">Other</p>
        </div>  
    </div>
    <div class="max-w-lg mx-auto mt-10 text-center">
        <a href="map" class="block w-full bg-blue-500 text-white py-4 px-6 rounded-lg font-semibold hover:bg-blue-600 transition duration-300">Map of Resources</a>
    </div> 
</body>
</html>
