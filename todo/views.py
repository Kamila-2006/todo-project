from django.shortcuts import HttpResponse

def task_create(request):
    html_response = """
    <h1>Yangi vazifa yaratish</h1>
    <form>
    <label>Vazifa nomi:</label>
    <input type="text">
    <label>Tavsiv:</label>
    <textarea></textarea>
    <label>Muddati:</label>
    <input type="date"
    <label>Muhimlik darajasi:</label>
    <select>
        <option>Past</option>
        <option>O'rta</option>
        <option>Yuqori</option>
    </select>
    <button>Vazifani saqlash</button>
    </form>
    <style>
        form {
            width: 300px;
        }

        label, input, textarea, select, button {
            display: block;
            width: 80%;
            margin-bottom: 15px;
        }

        button {
            width: auto;
            margin-top: 10px;
        }

        input, textarea, select {
            padding: 8px;
            font-size: 14px;
        }

        textarea {
            height: 80px;
        }
    </style>
    """
    return HttpResponse(html_response)