"""
Lesson 21 - Homework: AI Doctor Predictor (Tkinter — Part 2, Homework)
Goal:
- Add a confidence bar (###----- style) and color theming:
    HIGH (>=70%) -> green, MEDIUM (40-69%) -> orange, LOW (<40%) -> red
- Keep Train / Predict working from symptoms.csv (Naive Bayes)
- Keep Reset & Disclaimer
- Maintain GUI readability (labels, frames)

Standard library only.
"""

import csv
import math
from collections import defaultdict
import tkinter as tk
from tkinter import messagebox

# -----------------------------
# Naive Bayes helpers
# -----------------------------
def read_symptom_csv(path="symptoms.csv"):
    symptoms, diseases = [], []
    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        if not {"symptoms", "disease"}.issubset(set(reader.fieldnames or [])):
            raise ValueError("CSV must have headers: symptoms,disease")
        for row in reader:
            s = (row["symptoms"] or "").strip().lower()
            d = (row["disease"] or "").strip().lower()
            if s and d:
                symptoms.append(s)
                diseases.append(d)
    return symptoms, diseases

def train_naive_bayes(symptoms_list, disease_list):
    disease_counts = defaultdict(int)
    word_counts = defaultdict(lambda: defaultdict(int))
    N = len(symptoms_list)
    for s, d in zip(symptoms_list, disease_list):
        disease_counts[d] += 1
        for w in s.split():
            word_counts[d][w] += 1
    vocab = set(w for s in symptoms_list for w in s.split())
    return {"disease_counts": disease_counts, "word_counts": word_counts, "N": N, "vocab": vocab}

def predict_with_scores(model, symptom_line):
    """Return (best_disease, confidence_percent, scores_dict) using normalized NB class probs."""
    disease_counts = model["disease_counts"]
    word_counts    = model["word_counts"]
    N              = model["N"]
    vocab          = model["vocab"]

    words = symptom_line.lower().split()
    # compute exp(log-prob) scores
    probs = {}
    for disease in disease_counts:
        if N <= 0:
            probs[disease] = 0.0
            continue
        logp = math.log(disease_counts[disease] / N)
        total_words = sum(word_counts[disease].values())
        denom = (total_words + len(vocab)) if len(vocab) > 0 else 1
        for w in words:
            logp += math.log((word_counts[disease][w] + 1) / denom)
        probs[disease] = math.exp(logp)

    # normalize
    total = sum(probs.values())
    if total <= 0:
        # degenerate case
        return None, 0.0, probs

    for k in probs:
        probs[k] /= total

    best_disease = max(probs, key=probs.get)
    conf_percent = probs[best_disease] * 100.0
    return best_disease, conf_percent, probs

# -----------------------------
# Tkinter App
# -----------------------------
class AIDoctorApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("AI Doctor — Lesson 21 Homework (Tkinter Part 2)")
        self.geometry("760x480")

        self.model = None
        self.symptoms_list = []
        self.disease_list = []

        # Title
        tk.Label(self, text="AI Doctor (Naive Bayes from symptoms.csv)",
                 font=("Arial", 14, "bold")).pack(pady=(10, 5))

        # Input + Buttons frame
        top = tk.Frame(self)
        top.pack(pady=6)

        tk.Label(top, text="Symptoms:", font=("Arial", 11)).grid(row=0, column=0, sticky="e", padx=6)
        self.entry = tk.Entry(top, width=52, font=("Consolas", 11))
        self.entry.grid(row=0, column=1, padx=6)

        tk.Button(top, text="Train (load CSV)", width=16, command=self.on_train).grid(row=0, column=2, padx=6)
        tk.Button(top, text="Predict", width=12, command=self.on_predict).grid(row=0, column=3, padx=6)
        tk.Button(top, text="Reset", width=10, command=self.on_reset).grid(row=0, column=4, padx=6)

        # Output section
        out = tk.LabelFrame(self, text="Output", padx=8, pady=8)
        out.pack(pady=10, fill="x", padx=8)

        row1 = tk.Frame(out); row1.pack(anchor="w")
        tk.Label(row1, text="Prediction:", font=("Arial", 11)).pack(side=tk.LEFT)
        self.pred_label = tk.Label(row1, text="(none)", font=("Arial", 11, "bold"))
        self.pred_label.pack(side=tk.LEFT, padx=8)

        row2 = tk.Frame(out); row2.pack(anchor="w", pady=3)
        tk.Label(row2, text="Confidence:", font=("Arial", 11)).pack(side=tk.LEFT)
        self.conf_label = tk.Label(row2, text="0.00% [LOW]", font=("Arial", 11))
        self.conf_label.pack(side=tk.LEFT, padx=8)

        # Confidence bar (text-based)
        row3 = tk.Frame(out); row3.pack(anchor="w", pady=3)
        tk.Label(row3, text="Conf Bar:", font=("Arial", 11)).pack(side=tk.LEFT)
        self.bar_label = tk.Label(row3, text="----------", font=("Consolas", 12))
        self.bar_label.pack(side=tk.LEFT, padx=8)

        # Explanation
        row4 = tk.Frame(out); row4.pack(anchor="w", pady=3)
        tk.Label(row4, text="Explanation:", font=("Arial", 11)).pack(side=tk.LEFT)
        self.explain_label = tk.Label(row4, text="(matched words shown in UPPERCASE)", font=("Arial", 10))
        self.explain_label.pack(side=tk.LEFT, padx=8)

        # Disclaimer
        self.disclaimer = tk.Label(self, text="This is an AI-style demo. For health issues, consult a doctor.",
                                   font=("Arial", 10), fg="#444")
        self.disclaimer.pack(pady=(2, 0))

        # Status bar
        self.status = tk.Label(self, text="Status: Ready", anchor="w", relief="sunken")
        self.status.pack(side=tk.BOTTOM, fill=tk.X, pady=(8,0))

    # --- Button handlers ---
    def on_train(self):
        try:
            self.symptoms_list, self.disease_list = read_symptom_csv("symptoms.csv")
            if not self.symptoms_list:
                self.status.configure(text="Status: CSV loaded but no rows found.")
                return
            self.model = train_naive_bayes(self.symptoms_list, self.disease_list)
            self.status.configure(text=f"Status: Model trained on {len(self.symptoms_list)} rows.")
        except FileNotFoundError:
            messagebox.showerror("File Not Found", "symptoms.csv not found in this folder.")
            self.status.configure(text="Status: Training failed (file not found).")
        except Exception as e:
            messagebox.showerror("Error", str(e))
            self.status.configure(text="Status: Training failed.")

    def on_predict(self):
        text = self.entry.get().strip()
        if not text:
            self.status.configure(text="Status: Please enter symptoms before predicting.")
            return
        if not self.model or not self.model["N"]:
            self.status.configure(text="Status: Please train the model first (Train button).")
            return

        # Predict
        pred, conf, _ = predict_with_scores(self.model, text)
        self.pred_label.configure(text=pred if pred else "(no prediction)")

        # Confidence string + bar + color
        tag = "HIGH" if conf >= 70 else "MEDIUM" if conf >= 40 else "LOW"
        self.conf_label.configure(text=f"{conf:.2f}% [{tag}]")
        # bar
        filled = max(1, int(conf) // 10)
        bar = "#" * filled + "-" * (10 - filled)
        self.bar_label.configure(text=bar)

        # color theme
        color = "#2e8b57" if tag == "HIGH" else "#ff8c00" if tag == "MEDIUM" else "#cc0000"
        self.pred_label.configure(fg=color)
        self.conf_label.configure(fg=color)
        self.bar_label.configure(fg=color)

        # Explanation: matched words
        words = text.lower().split()
        matched = [w for w in words if any(w in s.split() for s in self.symptoms_list)]
        not_found = [w for w in words if w not in matched]
        expl = f"Matched: {' '.join([w.upper() for w in matched])} | Missed: {' '.join(not_found) if not_found else '(none)'}"
        self.explain_label.configure(text=expl)

        self.status.configure(text="Status: Prediction completed.")

    def on_reset(self):
        self.entry.delete(0, tk.END)
        self.pred_label.configure(text="(none)", fg="black")
        self.conf_label.configure(text="0.00% [LOW]", fg="black")
        self.bar_label.configure(text="----------", fg="black")
        self.explain_label.configure(text="(matched words shown in UPPERCASE)")
        self.status.configure(text="Status: Cleared input/output.")

if __name__ == "__main__":
    app = AIDoctorApp()
    app.mainloop()
