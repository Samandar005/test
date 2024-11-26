from django.shortcuts import HttpResponse

def task_list(request):
    http_response = """
    <!DOCTYPE html>
<html lang="uz">
<head>
    <meta charset="UTF-8">
    <title>Vazifalar Ro'yxati</title>
</head>
<body>
    <h1>Vazifalar Ro'yxati</h1>
    <h2>Yangi vazifa qo'shish</h2>
    <form>
        <label for="vazifa-nomi">Vazifa nomi:</label>
        <input type="text" id="vazifa-nomi" name="vazifa-nomi"><br><br>
        <label for="tavsif">Tavsif:</label><br>
        <textarea id="tavsif" name="tavsif"></textarea><br><br>
        <label for="muhimlik">Muhimlik darajasi:</label>
        <select id="muhimlik" name="muhimlik">
            <option value="past">Past</option>
            <option value="orta">O'rta</option>
            <option value="yuqori">Yuqori</option>
        </select><br><br>
        <label for="muddat">Muddat:</label>
        <input type="date" id="muddat" name="muddat"><br><br>
        <button type="submit">Vazifani qo'shish</button>
    </form>
    <h2>Mavjud vazifalar</h2>
    <table>
        <tr>
            <th>Vazifa</th>
            <th>Tavsif</th>
            <th>Muhimlik</th>
            <th>Muddat</th>
            <th>Holat</th>
        </tr>
        <tr>
            <td>Hisobot tayyorlash</td>
            <td>Oylik moliyaviy hisobotni tayyorlash va topshirish</td>
            <td>Yuqori</td>
            <td>2023-05-31</td>
            <td>Bajarilmoqda</td>
        </tr>
        <tr>
            <td>Mijoz bilan uchrashuv</td>
            <td>Yangi loyiha bo'yicha mijoz bilan muzokaralar o'tkazish</td>
            <td>O'rta</td>
            <td>2023-05-25</td>
            <td>Rejalashtirilgan</td>
        </tr>
        <tr>
            <td>Prezentatsiya tayyorlash</td>
            <td>Yangi mahsulot uchun taqdimot slaydlarini tayyorlash</td>
            <td>Past</td>
            <td>2023-06-05</td>
            <td>Boshlanmagan</td>
        </tr>
        <tr>
            <td>Xodimlar uchun trening</td>
            <td>Yangi dasturiy ta'minot bo'yicha xodimlarga qo'llanma berish</td>
            <td>O'rta</td>
            <td>2023-06-10</td>
            <td>Rejalashtirilgan</td>
        </tr>
        <tr>
            <td>Loyiha hujjatlarini yangilash</td>
            <td>Joriy loyihaning texnik hujjatlarini yangilash va arxivlash</td>
            <td>Past</td>
            <td>2023-06-15</td>
            <td>Boshlanmagan</td>
        </tr>
    </table>
</body>
</html>

"""
    return HttpResponse(http_response)