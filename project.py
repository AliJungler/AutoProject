import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

FONT_LABEL = ("Segoe UI", 10)
FONT_HEADER = ("Segoe UI", 11, "bold")

COLOR_BG = "#0f172a"          
COLOR_CARD = "#1e293b"        
COLOR_TEXT_LABEL = "#cbd5e1"  
COLOR_BORDER = "#334155"      

H_GREEN = "#86efac"  
H_BLUE = "#93c5fd"
H_YELLOW = "#fde047"

app = ctk.CTk()

app.geometry("1350x750") 
app.title("TEST")
app.configure(fg_color=COLOR_BG)


main_container = ctk.CTkFrame(app, fg_color="transparent")
main_container.pack(pady=15, padx=20, fill="both", expand=True)


def fokus_mundur(event):
    event.widget.tk_focusPrev().focus_set()
    return "break"

app.bind("<Caps_Lock>", fokus_mundur)
app.bind("<Up>", fokus_mundur)
app.bind("<Shift-Tab>", fokus_mundur)


def create_card(parent, title, icon, color):
    card = ctk.CTkFrame(parent, fg_color=COLOR_CARD, corner_radius=12, border_width=1, border_color=COLOR_BORDER)
    ctk.CTkLabel(card, text=f"{icon} {title}", font=FONT_HEADER, text_color=color).pack(pady=(10, 5), padx=15, anchor="w")
    content = ctk.CTkFrame(card, fg_color="transparent")
    content.pack(fill="both", expand=True, padx=15, pady=(0, 15))
    return card, content

def create_label(parent, text):
    return ctk.CTkLabel(parent, text=text, font=FONT_LABEL, text_color=COLOR_TEXT_LABEL)

col1 = ctk.CTkFrame(main_container, fg_color="transparent")
col1.grid(row=0, column=0, padx=5, sticky="n")

card_sinop, c_sinop = create_card(col1, "SINOPTIK & INSTRUMEN", "📊", H_GREEN)

card_sinop.pack(fill="x", pady=(0, 10)) 


single_fields = [("👁️ Visibility", "Visibility"), ("☁️ WW", "WW"), ("☁️ W1", "W1"), ("☁️ W2", "W2"), ("🌥️ Tutupan", "Tutupan Langit")]
for i, (icon_text, _) in enumerate(single_fields):
    create_label(c_sinop, f"{icon_text}:").grid(row=i, column=0, sticky="e", padx=(0,5), pady=3)
    if "WW" in icon_text or "W" in icon_text or "Tutupan" in icon_text:
        ctk.CTkComboBox(c_sinop, values=["Pilih..."], width=190, height=24).grid(row=i, column=1, columnspan=3, sticky="w", pady=3)
    else:
        ctk.CTkEntry(c_sinop, width=190, height=24).grid(row=i, column=1, columnspan=3, sticky="w", pady=3)


paired_fields = [
    ("🌬️ Arah", "Kecepatan"),
    ("🧭 QFF", "QFE"),
    ("🌡️ T. Kering", "T. Basah"),
    ("📈 T. Max", "📉 T. Min"),
    ("🌧️ Hujan", "💧 Penguapan")
]

start_row = len(single_fields)
for i, (f1, f2) in enumerate(paired_fields):
    r = start_row + i
    
    create_label(c_sinop, f"{f1}:").grid(row=r, column=0, sticky="e", padx=(0,5), pady=3)
    ctk.CTkEntry(c_sinop, width=70, height=24).grid(row=r, column=1, sticky="w", padx=(0,10), pady=3)
    
    create_label(c_sinop, f"{f2}:").grid(row=r, column=2, sticky="e", padx=(0,5), pady=3)
    ctk.CTkEntry(c_sinop, width=70, height=24).grid(row=r, column=3, sticky="w", pady=3)



def build_awan_form(parent_card, fields, start_row=0):
    for i, f in enumerate(fields):
        create_label(parent_card, f"{f}:").grid(row=i+start_row, column=0, sticky="e", padx=(0,8), pady=2)
        ctk.CTkEntry(parent_card, width=110, height=24).grid(row=i+start_row, column=1, sticky="w", pady=2)


col2 = ctk.CTkFrame(main_container, fg_color="transparent")
col2.grid(row=0, column=1, padx=(10, 5), sticky="n")

card_ar1, c_ar1 = create_card(col2, "AWAN RENDAH 1", "☁️", H_BLUE)
card_ar1.pack(fill="x", pady=(0, 10))
build_awan_form(c_ar1, ["CL", "NCL", "Jenis", "Jumlah", "T. Dasar", "T. Puncak", "Arah", "Sudut", "Arah Sbnry"])

card_ar2, c_ar2 = create_card(col2, "AWAN RENDAH 2", "☁️", H_BLUE)
card_ar2.pack(fill="x")
build_awan_form(c_ar2, ["Jenis", "Jumlah", "T. Dasar", "T. Puncak", "Arah", "Sudut", "Arah Sbnry"])


col3 = ctk.CTkFrame(main_container, fg_color="transparent")
col3.grid(row=0, column=2, padx=5, sticky="n")

card_am1, c_am1 = create_card(col3, "AWAN MENENGAH 1", "⛅", H_BLUE)
card_am1.pack(fill="x", pady=(0, 10))
build_awan_form(c_am1, ["CM", "NCM", "Jenis", "Jumlah", "T. Dasar", "Arah"])

card_am2, c_am2 = create_card(col3, "AWAN MENENGAH 2", "⛅", H_BLUE)
card_am2.pack(fill="x")
build_awan_form(c_am2, ["Jenis", "Jumlah", "T. Dasar", "Arah"])


col4 = ctk.CTkFrame(main_container, fg_color="transparent")
col4.grid(row=0, column=3, padx=(5, 0), sticky="n")

card_at1, c_at1 = create_card(col4, "AWAN TINGGI 1", "🌤️", H_BLUE)
card_at1.pack(fill="x", pady=(0, 10))
build_awan_form(c_at1, ["CH", "NCH", "Jenis", "Jumlah", "T. Dasar", "Arah"])

card_at2, c_at2 = create_card(col4, "AWAN TINGGI 2", "🌤️", H_BLUE)
card_at2.pack(fill="x", pady=(0, 10))
build_awan_form(c_at2, ["Jenis", "Jumlah", "T. Dasar", "Arah"])

card_tanah, c_tanah = create_card(col4, "KEADAAN TANAH", "🌱", H_YELLOW)
card_tanah.pack(fill="x")
create_label(c_tanah, "Status:").grid(row=0, column=0, sticky="e", padx=(0,8))
ctk.CTkComboBox(c_tanah, values=["Lembab", "Kering", "Basah"], width=110, height=24).grid(row=0, column=1, sticky="w")


btn_frame = ctk.CTkFrame(app, fg_color="transparent")
btn_frame.pack(pady=20, padx=20, anchor="w")

btn_simpan = ctk.CTkButton(btn_frame, text="🚀 SIMPAN & JALANKAN KE WEB", font=("Segoe UI", 12, "bold"), 
                           width=240, height=45, fg_color="#2563eb", hover_color="#1d4ed8", corner_radius=8)
btn_simpan.pack(side="left", padx=(0, 15))

btn_backup = ctk.CTkButton(btn_frame, text="☁️ BACKUP KE CLOUD SAJA", font=("Segoe UI", 12, "bold"), 
                           width=240, height=45, fg_color="#334155", hover_color="#1e293b", corner_radius=8, 
                           border_width=1, border_color="#475569")
btn_backup.pack(side="left")

app.mainloop()