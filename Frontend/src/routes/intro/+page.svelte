<!DOCTYPE html>
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
            <h1 class="text-4xl font-bold text-white">Welcome to [Name Here]</h1>
        </div>
    </header>
    <div class="flex items-center justify-center text-center p-4 mt-8">
        <p class="text-lg text-gray-700 max-w-xl">The community of Spokane cares deeply about providing resources for those who need a little extra support.
        Whether you are looking for financial aid, food, shelter, healthcare, or other,
        you've come to the right spot.</p>
    </div>
    <div class="flex-container mx-auto mt-8 grid grid-cols-6 gap-4">
        <!-- First Square -->
        <div style="background-color: #742d75; color: white" class="p-4 flex flex-col items-center justify-center h-32">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-12 w-12 mb-2" viewBox="0 0 20 20" fill="currentColor">
            </svg>
            <p class="text-lg font-semibold text-center">Food Resources</p>
        </div>
        <!-- Second Square -->
        <div style="background-color: #373463; color: white" class="p-4 flex flex-col items-center justify-center h-32">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-12 w-12 mb-2" viewBox="0 0 20 20" fill="currentColor">
            </svg>
            <p class="text-lg font-semibold text-center">Shelter</p>
        </div>
        <!-- Third Square -->
        <div style="background-color: #1e8181; color: white" class="p-4 flex flex-col items-center justify-center h-32">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-12 w-12 mb-2" viewBox="0 0 20 20" fill="currentColor">
            </svg>
            <p class="text-lg font-semibold text-center">Financial Aid</p>
        </div>
        <!-- Fourth Square -->
        <div style="background-color: #62975e; color: white" class="p-4 flex flex-col items-center justify-center h-32">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-12 w-12 mb-2" viewBox="0 0 20 20" fill="currentColor">
            </svg>
            <p class="text-lg font-semibold text-center">Healthcare</p>
        </div>
        <!-- Fifth Square -->
        <div style="background-color: #9c7a39; color: white" class="p-4 flex flex-col items-center justify-center h-32">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-12 w-12 mb-2" viewBox="0 0 20 20" fill="currentColor">
            </svg>
            <p class="text-lg font-semibold text-center">Rehabilitation Centers</p>
        </div>
        <!-- Sixth Square -->
        <div style="background-color: #682e44; color: white" class="p-4 flex flex-col items-center justify-center h-32">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-12 w-12 mb-2" viewBox="0 0 20 20" fill="currentColor">
            </svg>
            <p class="text-lg font-semibold text-center">Rehabilitation Centers</p>
        </div>
    </div>
    <div class="max-w-lg mx-auto mt-10 text-center">
        <a href="map" class="block w-full bg-blue-500 text-white py-4 px-6 rounded-lg font-semibold hover:bg-blue-600 transition duration-300">Map of Resources</a>
    </div>    
</body>
</html>
