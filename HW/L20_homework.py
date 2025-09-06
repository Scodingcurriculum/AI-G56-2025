"""
Lesson 20 - Homework: AI Doctor Predictor (Tkinter — Part 1, Homework)
Goal:
- Add a "Load Sample" button that auto-fills the Entry with example: "fever cough"
- Keep Train and Predict working (reads symptoms.csv, trains Naive Bayes, predicts)
- Add a tiny Help label with usage instructions
- Add a Status bar that shows friendly updates (e.g., trained row count, prediction done)

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

def predict_naive_bayes(model, symptom_line):
    disease_counts = model["disease_counts"]
    word_counts    = model["word_counts"]
    N              = model["N"]
    vocab          = model["vocab"]

    words = symptom_line.lower().split()
    best_disease, best_logprob = None, -math.inf
    # store raw probs for potential extensions later
    for disease in disease_counts:
        # Prior
        logp = math.log(disease_counts[disease] / N) if N > 0 else -math.inf
        total_words = sum(word_counts[disease].values())
        for w in words:
            logp += math.log((word_counts[disease][w] + 1) / (total_words + len(vocab) if len(vocab) > 0 else 1))
        if logp > best_logprob:
            best_logprob = logp
            best_disease = disease
    return best_disease

# -----------------------------
# Tkinter App
# -----------------------------
class AIDoctorApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("AI Doctor — Lesson 20 Homework (Tkinter Part 1)")
        self.geometry("680x360")

        self.model = None
        self.symptoms_list = []
        self.disease_list = []

        # Title
        tk.Label(self, text="AI Doctor (Naive Bayes from symptoms.csv)",
                 font=("Arial", 14, "bold")).pack(pady=(10, 5))

        # Help / instructions
        tk.Label(self,
                 text="Type symptoms separated by spaces, e.g.,  fever cough sore throat",
                 font=("Arial", 10)).pack()

        # Input row
        row = tk.Frame(self)
        row.pack(pady=8)
        tk.Label(row, text="Symptoms:", font=("Arial", 11)).pack(side=tk.LEFT, padx=6)
        self.entry = tk.Entry(row, width=50, font=("Consolas", 11))
        self.entry.pack(side=tk.LEFT, padx=6)

        # Buttons row
        btns = tk.Frame(self)
        btns.pack(pady=6)
        tk.Button(btns, text="Train (load CSV)", command=self.on_train, width=16).pack(side=tk.LEFT, padx=6)
        tk.Button(btns, text="Predict", command=self.on_predict, width=12).pack(side=tk.LEFT, padx=6)
        tk.Button(btns, text="Load Sample", command=self.on_load_sample, width=14).pack(side=tk.LEFT, padx=6)

        # Output area
        out = tk.Frame(self)
        out.pack(pady=10)
        tk.Label(out, text="Prediction:", font=("Arial", 11)).grid(row=0, column=0, sticky="e", padx=6)
        self.pred_label = tk.Label(out, text="(none yet)", font=("Arial", 11, "bold"))
        self.pred_label.grid(row=0, column=1, sticky="w")

        # Status bar
        self.status = tk.Label(self, text="Status: Ready", anchor="w", relief="sunken")
        self.status.pack(side=tk.BOTTOM, fill=tk.X, pady=(8,0))

    # --- Button handlers ---
    def on_load_sample(self):
        self.entry.delete(0, tk.END)
        self.entry.insert(0, "fever cough")
        self.status.configure(text="Status: Loaded sample input (fever cough)")

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
        disease = predict_naive_bayes(self.model, text)
        self.pred_label.configure(text=disease if disease else "(no prediction)")
        self.status.configure(text="Status: Prediction completed.")

if __name__ == "__main__":
    app = AIDoctorApp()
    app.mainloop()
