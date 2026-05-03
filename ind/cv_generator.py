import re
import json
import os
import tkinter as tk
from tkinter import ttk, filedialog, messagebox

from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

# 
# Шрифт для PDF 
# 

font_path = os.path.join(
    os.path.dirname(__file__),
    "DejaVuSans.ttf"
)
pdfmetrics.registerFont(TTFont("CustomFont", font_path))

# 
# Модель данных
# 

class User:
    def __init__(self, name="", email="", phone="", experience="", education="", skills="", photo=""):
        self.name = name
        self.email = email
        self.phone = phone
        self.experience = experience
        self.education = education
        self.skills = skills
        self.photo = photo

# 
# Валидация
# 

def validate_email(email):
    return re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email)

def validate_phone(phone):
    return re.match(r'^\+?\d{7,15}$', phone)

# 
# Генерация PDF 
# 

def generate_pdf(user):
    doc = SimpleDocTemplate("CV.pdf", pagesize=A4)

    name_style = ParagraphStyle(
        name="name",
        fontName="CustomFont",
        fontSize=20,
        textColor=colors.black,
        spaceAfter=10
    )

    section_title = ParagraphStyle(
        name="section",
        fontName="CustomFont",
        fontSize=13,
        textColor=colors.HexColor("#2E3A59"),
        spaceAfter=6
    )

    text_style = ParagraphStyle(
        name="text",
        fontName="CustomFont",
        fontSize=10,
        spaceAfter=8
    )

    left_title = ParagraphStyle(
        name="left_title",
        fontName="CustomFont",
        fontSize=11,
        textColor=colors.white,
        spaceAfter=6
    )

    left_text = ParagraphStyle(
        name="left_text",
        fontName="CustomFont",
        fontSize=9,
        textColor=colors.white,
        spaceAfter=4
    )

    # Левая колонка
    left_elements = []

    if user.photo and os.path.exists(user.photo):
        try:
            img = Image(user.photo, width=100, height=100)
            left_elements.append(img)
            left_elements.append(Spacer(1, 10))
        except:
            pass

    left_elements.append(Paragraph("Контакты", left_title))
    left_elements.append(Paragraph(user.email, left_text))
    left_elements.append(Paragraph(user.phone, left_text))
    left_elements.append(Spacer(1, 10))

    left_elements.append(Paragraph("Навыки", left_title))
    left_elements.append(Paragraph(user.skills, left_text))

    left_table = Table([[left_elements]], colWidths=[170])
    left_table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#2E3A59")),
        ("LEFTPADDING", (0, 0), (-1, -1), 12),
        ("RIGHTPADDING", (0, 0), (-1, -1), 12),
        ("TOPPADDING", (0, 0), (-1, -1), 12),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 12),
    ]))

    # Правая колонка
    right_elements = []
    right_elements.append(Paragraph(user.name, name_style))

    right_elements.append(Paragraph("Опыт работы", section_title))
    right_elements.append(Paragraph(user.experience, text_style))

    right_elements.append(Paragraph("Образование", section_title))
    right_elements.append(Paragraph(user.education, text_style))

    right_table = Table([[right_elements]], colWidths=[360])
    right_table.setStyle(TableStyle([
        ("LEFTPADDING", (0, 0), (-1, -1), 15),
    ]))

    main_table = Table([[left_table, right_table]], colWidths=[180, 360])
    main_table.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ]))

    doc.build([main_table])
    messagebox.showinfo("Готово", "PDF создан")

# 
# GUI 
# 

def create_gui():
    root = tk.Tk()
    root.title("CV Generator")
    root.geometry("620x720")
    root.minsize(560, 640)

    style = ttk.Style()
    style.theme_use("clam")

    # Базовые стили
    style.configure("TFrame", background="#F5F7FA")
    style.configure("Card.TLabelframe", background="#FFFFFF", borderwidth=1, relief="solid")
    style.configure("Card.TLabelframe.Label", font=("Segoe UI", 11, "bold"))
    style.configure("TLabel", background="#F5F7FA", font=("Segoe UI", 10))
    style.configure("TEntry", padding=6)
    style.configure("Primary.TButton", font=("Segoe UI", 10, "bold"), padding=8)
    style.map("Primary.TButton",
              background=[("active", "#2E3A59"), ("!active", "#3E4E73")],
              foreground=[("active", "white"), ("!active", "white")])

    container = ttk.Frame(root, padding=15)
    container.pack(fill="both", expand=True)

    # Скролл
    canvas = tk.Canvas(container, highlightthickness=0, bg="#F5F7FA")
    scrollbar = ttk.Scrollbar(container, orient="vertical", command=canvas.yview)
    scroll_frame = ttk.Frame(canvas)

    scroll_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )

    canvas.create_window((0, 0), window=scroll_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    # ---------- Карточка: личные данные ----------
    personal = ttk.LabelFrame(scroll_frame, text="Личные данные", style="Card.TLabelframe", padding=12)
    personal.pack(fill="x", pady=10)

    def add_field(parent, label, row, col):
        ttk.Label(parent, text=label).grid(row=row, column=col, sticky="w", padx=5, pady=5)
        entry = ttk.Entry(parent, width=30)
        entry.grid(row=row+1, column=col, padx=5, pady=5)
        return entry

    name_entry = add_field(personal, "Имя", 0, 0)
    email_entry = add_field(personal, "Email", 0, 1)
    phone_entry = add_field(personal, "Телефон", 2, 0)

    # ---------- Карточка: опыт и образование ----------
    info = ttk.LabelFrame(scroll_frame, text="Информация", style="Card.TLabelframe", padding=12)
    info.pack(fill="x", pady=10)

    ttk.Label(info, text="Опыт работы").pack(anchor="w")
    exp_text = tk.Text(info, height=4)
    exp_text.pack(fill="x", pady=5)

    ttk.Label(info, text="Образование").pack(anchor="w")
    edu_text = tk.Text(info, height=3)
    edu_text.pack(fill="x", pady=5)

    ttk.Label(info, text="Навыки").pack(anchor="w")
    skills_text = tk.Text(info, height=3)
    skills_text.pack(fill="x", pady=5)

    # ---------- Карточка: фото ----------
    photo_frame = ttk.LabelFrame(scroll_frame, text="Фото", style="Card.TLabelframe", padding=12)
    photo_frame.pack(fill="x", pady=10)

    photo_path = {"path": ""}
    preview_label = ttk.Label(photo_frame)
    preview_label.pack()

    def choose_photo():
        path = filedialog.askopenfilename(filetypes=[("Images", "*.png *.jpg *.jpeg")])
        if path:
            photo_path["path"] = path
            try:
                img = tk.PhotoImage(file=path)
                preview_label.configure(image=img)
                preview_label.image = img
            except:
                preview_label.configure(text="Предпросмотр недоступен")

    ttk.Button(photo_frame, text="Выбрать фото", command=choose_photo).pack(pady=5)

    # ---------- Кнопки ----------
    btn_frame = ttk.Frame(scroll_frame)
    btn_frame.pack(pady=15)

    def get_user():
        return User(
            name_entry.get(),
            email_entry.get(),
            phone_entry.get(),
            exp_text.get("1.0", "end").strip(),
            edu_text.get("1.0", "end").strip(),
            skills_text.get("1.0", "end").strip(),
            photo_path["path"]
        )

    def save_data():
        user = get_user()
        if not validate_email(user.email):
            messagebox.showerror("Ошибка", "Некорректный email")
            return
        if not validate_phone(user.phone):
            messagebox.showerror("Ошибка", "Некорректный телефон")
            return

        with open("user.json", "w", encoding="utf-8") as f:
            json.dump(user.__dict__, f, ensure_ascii=False, indent=4)

        messagebox.showinfo("Сохранено", "Данные сохранены")

    def load_data():
        try:
            with open("user.json", "r", encoding="utf-8") as f:
                data = json.load(f)

            name_entry.delete(0, tk.END)
            name_entry.insert(0, data.get("name", ""))

            email_entry.delete(0, tk.END)
            email_entry.insert(0, data.get("email", ""))

            phone_entry.delete(0, tk.END)
            phone_entry.insert(0, data.get("phone", ""))

            exp_text.delete("1.0", tk.END)
            exp_text.insert("1.0", data.get("experience", ""))

            edu_text.delete("1.0", tk.END)
            edu_text.insert("1.0", data.get("education", ""))

            skills_text.delete("1.0", tk.END)
            skills_text.insert("1.0", data.get("skills", ""))

            photo_path["path"] = data.get("photo", "")

        except:
            messagebox.showerror("Ошибка", "Файл не найден")

    def create_pdf_action():
        user = get_user()
        if not user.name:
            messagebox.showerror("Ошибка", "Введите имя")
            return
        generate_pdf(user)

    ttk.Button(btn_frame, text="Сохранить", style="Primary.TButton", command=save_data).grid(row=0, column=0, padx=5)
    ttk.Button(btn_frame, text="Загрузить", style="Primary.TButton", command=load_data).grid(row=0, column=1, padx=5)
    ttk.Button(btn_frame, text="Создать PDF", style="Primary.TButton", command=create_pdf_action).grid(row=0, column=2, padx=5)

    root.mainloop()

# 

if __name__ == "__main__":
    create_gui()