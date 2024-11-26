# TODO Project

Bu loyiha foydalanuvchilarga vazifalarni qo'shish, boshqarish va kuzatishga imkon beruvchi oddiy TODO boshqaruv tizimidir. Django asosida ishlab chiqilgan va HTML yordamida vizual interfeys taqdim etilgan.

## 🚀 Texnologiyalar

- **Django**: Veb-dastur ramkasi.
- **HTML**: Veb-sahifa strukturasini yaratish uchun.
- **CSS**: Sahifani bezash va dizayn qilish uchun.
- **SQLite**: Ma'lumotlarni saqlash uchun o'rnatilgan bazaviy tizim.

## 📥 O'rnatish va Ishga Tushirish

Quyidagi bosqichlarni bajaring:

1. **Repozitoriyani klonlang:**

   ```bash
   git clone https://github.com/rinkuo/todo-project.git
   cd todo-project
Virtual muhitni yarating va faollashtiring:

Linux/MacOS:
```bash
python3 -m venv venv
source venv/bin/activate
```
Windows:
```bash
python -m venv venv
venv\Scripts\activate
```
Kerakli kutubxonani o'rnating:
```bash
pip install django
```
Django serverini ishga tushuring:
```bash
python manage.py runserver
Brauzerda http://127.0.0.1:8000/ manzilini oching.
```

📝 Asosiy Xususiyatlar
Vazifalarni qo'shish, boshqarish va o'chirish.
Vazifaning nomi, tavsifi, muhimlik darajasi va muddati ko'rsatiladi.
HTML interfeys yordamida qulay ko'rinish.

📄 Struktura
config/: Django asosiy sozlamalari.
todo/: TODO ilovasi, unda vazifalar ro'yxati va funksionallik mavjud.
manage.py: Django boshqaruv fayli.

📂 HTML Dizayni
HTML sahifasi foydalanuvchilarga qulay interfeys taqdim etadi. Vazifalar ro'yxatini ko'rish va yangi vazifalarni qo'shish funksiyalari mavjud.

🔄 GitHub Branch Tartibi
main branch: Asosiy kod.
dev_1 branch: Yangi TODO ilovasini yaratish uchun ishlatiladi.
dev_2 branch: Django loyihasi va asosiy sozlamalar.

👥 Loyihada Ishlash
Branch yaratib o'zgartirishlar kiriting:
```bash
git checkout -b yangi-branch
```
O'zgartirishlarni commit qiling:
```bash
git add .
git commit -m "O'zgartirish nomi"
```
Pull request yuboring va asosiy branchga birlashtiring.

📌 Mualliflar

Loyiha <a href="https://github.com/Mirshohid1">Mirshohid1</a> va <a href="https://github.com/Samandar005">Samandar005</a> tomonidan ishlab chiqligan.

📜 Litsenziya
MIT Litsenziyasi asosida tarqatiladi.
Ushbu matnni `README.md` fayliga joylashtiring. Faylni GitHub repozitoriyasiga qo'shishni unutmang: 

```bash
git add README.md
git commit -m "README.md fayli qo'shildi"
git push origin main
```
