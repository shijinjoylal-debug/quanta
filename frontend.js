const API_BASE_URL = 'https://quanta-backend-raeq.onrender.com';
fetch(`${API_BASE_URL}/generate`, {
    method: "POST",
    headers: { "content-type": "application/json" },
    body: JSON.stringify({ content: websiteText })
})
    .then(res => res.json())
    .then(data => {
        document.getElementById("output").innerHTML = data;
    })


