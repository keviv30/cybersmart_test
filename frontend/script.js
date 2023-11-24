document.addEventListener("DOMContentLoaded", function() {
    // Initialize the application
    fetchTasks();
    fetchLocations();

    // Event listener for location change in the Add/Edit form
    document.getElementById('location').addEventListener('change', function() {
        updateBackgroundAndTemperature(this.options[this.selectedIndex].text);
    });

    // Add event listeners for Add/Edit form submission
    document.getElementById('taskForm').addEventListener('submit', function(event) {
        event.preventDefault();
        submitTaskForm();
    });
});

function fetchTasks() {
    // Fetch tasks from the API and add them to the DOM
    fetch('http://localhost:8080/tasks/')
        .then(response => response.json())
        .then(data => displayTasks(data))
        .catch(error => console.error('Error:', error));
}

function fetchLocations() {
    // Fetch locations from the API and populate the select element
    fetch('http://localhost:8080/locations/')
        .then(response => response.json())
        .then(data => {
            const locationSelect = document.getElementById('location');
            data.forEach(location => {
                let option = document.createElement('option');
                option.value = location.id;
                option.textContent = location.name;
                locationSelect.appendChild(option);
            });

            if (data.length > 0) {
                updateBackgroundAndTemperature(data[0].name);
            }
        })
        .catch(error => console.error('Error:', error));
}

function displayTasks(tasks) {
    const taskList = document.getElementById('taskList');
    taskList.innerHTML = ''; // Clear existing tasks
    tasks.forEach(task => {
        let taskDiv = document.createElement('div');
        taskDiv.className = 'task-item';
        taskDiv.style.backgroundColor = task.location_details.background_color; // Function to determine color

        let title = document.createElement('h3');
        title.textContent = "Title: " + task.title; // Assuming 'title' is a field in your task object
        taskDiv.appendChild(title);

        let description = document.createElement('p');
        description.textContent = "Description: " + task.description;
        taskDiv.appendChild(description);

        let completed = document.createElement('p');
        completed.textContent = "Completed: " + task.completed;
        taskDiv.appendChild(completed);

        let location = document.createElement('p');
        location.textContent = "Location: " + task.location_details.location_name;
        taskDiv.appendChild(location);

        let temperature = document.createElement('p');
        temperature.textContent = "Temperature: " + task.location_details.temperature;
        taskDiv.appendChild(temperature);

        taskList.appendChild(taskDiv);
    });
}

function updateBackgroundAndTemperature(locationName) {
    // Fetch weather data based on locationId and update the form's background color and display temperature
    fetch('http://localhost:8080/weather/' + locationName)
        .then(response => response.json())
        .then(data => {
            document.getElementById('taskForm').style.backgroundColor = data.background_color;
            // Display temperature information (you need to adjust based on your API response)
        })
        .catch(error => console.error('Error:', error));
}

function submitTaskForm() {
    const form = document.getElementById('taskForm');
    const formData = new FormData(form);
    const taskData = {};

    formData.forEach((value, key) => {
        taskData[key] = value;
    });

    let method = 'POST'; // Default method for adding a new task
    let url = 'http://localhost:8080/tasks/'; // URL for creating a new task

    fetch(url, {
        method: method,
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(taskData)
    })
    .then(response => response.json())
    .then(data => {
        console.log('Success:', data);
        fetchTasks(); // Refresh the task list
        form.reset(); // Reset the form fields
//        form.style.display = 'none'; // Hide the form
    })
    .catch((error) => {
        console.error('Error:', error);
    });
}

