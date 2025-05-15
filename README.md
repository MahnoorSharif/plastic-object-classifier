
# ♻️ Plastic Object Classifier – Conveyor Belt Sorter

This project is a Critical Thinking assignment solution for Bahria University (Spring 2025). It classifies plastic objects into **Black**, **Transparent**, or **Colorful** using a Python + OpenCV + Flask web interface and sorts them into respective folders (Conveyor Belt A, B, C).

---

## 📌 Objective

Build an automated system to:
- 📷 Accept user-uploaded plastic object images
- 🧠 Analyze image using rule-based detection (brightness, color)
- 🗂️ Classify the object
- 📁 Move image to correct folder:
  - **Black → Conveyor Belt A → `/black/`**
  - **Transparent → Conveyor Belt B → `/transparent/`**
  - **Colorful → Conveyor Belt C → `/colorful/`**

---

## 🛠️ Tech Stack

- Python 3
- OpenCV
- Flask (web framework)
- HTML/CSS for UI

---

## 🗂️ Project Structure

```
plastic_classifier/
├── app.py               # Flask app
├── classify.py          # Rule-based logic (OpenCV)
├── templates/
│   └── index.html       # Upload form
├── static/
│   └── style.css        # Page styling
├── uploads/             # Temporary upload area
├── black/               # Black plastic images
├── transparent/         # Transparent plastic images
├── colorful/            # Colorful plastic images
└── README.md            # This file
```

---

## ⚙️ Setup Instructions

### ✅ 1. Clone the Repository

```bash
git clone https://github.com/yourusername/plastic-classifier.git
cd plastic-classifier
```

### ✅ 2. Install Requirements

```bash
pip install flask opencv-python
```

### ✅ 3. Run the App

```bash
python app.py
```

Open in browser: [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 🌟 Features

- Simple web interface to upload images
- Classifies image using:
  - **Brightness threshold** → Transparent
  - **Color pixel strength** → Colorful
  - **Otherwise** → Black
- Automatically moves the image into respective folders
- Displays classification result instantly on the web page

---

## 💡 Logic Used (in `classify.py`)

```python
if brightness > 180:
    → Transparent → Conveyor Belt B
elif strong color pixels > threshold:
    → Colorful → Conveyor Belt C
else:
    → Black → Conveyor Belt A
```

---

## 🧪 Example Test Images

| Image Name   | Result                    | Folder      |
|--------------|---------------------------|-------------|
| test.jpg   | Black → Conveyor Belt A   | `/black/`   |
| test4.jpg   | Transparent → Conveyor B  | `/transparent/` |
| test5.jpg| Colorful → Conveyor C     | `/colorful/`|

---



## 🔗 Live Demo / GitHub Pages (if applicable)

> _Not applicable for Flask apps unless deployed._

---

## 📑 Assignment Info

**Course:** BES-103 Critical Thinking  
**University:** Bahria University  
**Semester:** Spring 2025  
**Marks:** 5  
**Deadline:** 18-05-2025

---

## 🙋‍♀️ Authors

- Mahnoor Sharif(02-235232-001) and Hadiqa Mehmood(02-235232-007)
- [Your GitHub Profile](https://github.com/yourusername)
