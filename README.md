# Flask Web App Project

Ye ek fully functional Python web project hai jisme humne **Flask** framework ka use kiya hai. Ise aap apne browser (Chrome/Firefox/Edge) pe dekh sakte hain. Isme ek HTML UI bhi hai.

## Project Files
- `app.py`: Ye main backend server ki file hai.
- `requirements.txt`: Is file mein saari Python libraries/packages ki list hoti hai jo is project ko chalne ke liye chahiye.
- `templates/index.html`: Ye hamara frontend visual page hai (UI).

---

## Isko Run Kaise Karein?

Apne Ubuntu/Linux terminal mein in steps ko dhyan se follow karein:

### Step 1: Project Folder Me Jayein
Terminal open karein aur ye command likhein:
```bash
cd /home/manishjangra97/Public/flask_sample_app
```

### Step 2: Virtual Environment Banayein (Recommended)
Project ko safely run karne ke liye ek virtual environment banana acha hota hai taki system ki baaki settings kharab na ho:
```bash
python3 -m venv venv
```
Iske baad environment ko activate karein:
```bash
source venv/bin/activate
```
*(Tip: Aapko terminal mein `(venv)` likha hua dikhega.)*

### Step 3: Libraries Install Karein
Ab `requirements.txt` se Flask install karne ke liye ye command chalayein:
```bash
pip install -r requirements.txt
```

### Step 4: Web App Ko Run Karein
Sab kuch install hone ke baad, app ko start karein:
```bash
python3 app.py
```

### Step 5: Browser Me Dekhein!
Ab apna web browser (jaise Chrome) kholein aur is link par jayein:
👉 [http://127.0.0.1:5000](http://127.0.0.1:5000)

*(Agar app band karna ho, toh terminal mein wapis jakar **Ctrl+C** dabayein)*
