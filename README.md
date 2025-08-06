# 📡 Tower Jump Analyzer

This project analyzes cell tower location data to detect **tower jumps** — sudden and likely inaccurate state changes due to triangulation noise — and estimates the **confidence level** for each location period.

---

## 🚀 Features

- Detects unrealistic state flips (e.g. NY ↔ CT)
- Estimates confidence based on time stability
- Outputs a clean `.csv` with full intervals and analysis
- Runs easily with Docker and `make`
- Optional React frontend (coming soon)

---

## 🧱 Project Structure

```
tower-jump-analyzer/
├── backend/                 # Python backend for data processing
│   ├── analyzer.py          # Tower jump logic
│   ├── cleaner.py           # Data cleaning and normalization
│   ├── config.py            # Config paths/constants
│   ├── data/                # Input CSV files
│   ├── loader.py            # Input CSV loader
│   ├── main.py              # Entry point
│   ├── report.py            # Output CSV generator
│   ├── tests/               # Pytest test suite
│   └── Dockerfile           # Backend container
├── frontend/                # Optional React frontend (MUI)
├── output/                  # CSV analysis results
├── docker-compose.yml       # Compose setup
├── Makefile                 # Run shortcuts
└── README.md
```

---

## ⚙️ How to Run (Backend)

### ✅ Using Docker (recommended)

```bash
make run
```

The final report will be saved at:

```
output/tower_jump_analysis.csv
```

### 🧹 Clean generated output

```bash
make clean
```

### 🔁 Rebuild backend from scratch

```bash
make rebuild
```

### 🐚 Open a shell in the container

```bash
make shell
```

---

## 🧪 Run Unit Tests

```bash
make test
```

Pytest runs inside the container using the test suite in `backend/tests/`.

---

## 🧰 Optional: Run Without Docker

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r backend/requirements.txt
python backend/main.py
```

Optional `.env` support:

```
INPUT_FILE=backend/data/input.csv
OUTPUT_FILE=output/tower_jump_analysis.csv
```

---

## 🖥️ Full Stack Mode (Backend + Frontend)

```bash
make run-frontend
```

This will:
- Run the backend and generate the CSV
- Launch the React app in dev mode (Vite)

The UI reads the CSV from `frontend/public/output/`.

---

## 💻 Tech Stack

- Python · Pandas
- React · TypeScript · MUI
- Docker · Make · PapaParse

---

## 🧠 Confidence Calculation

| Duration         | Confidence |
|------------------|------------|
| > 30 minutes     | 100%       |
| 15–30 minutes    | 80%        |
| < 15 minutes     | 50%        |

---

## 📦 Output Format

| Column           | Description                                 |
|------------------|---------------------------------------------|
| LocalDateTime    | Timestamp of the record                     |
| State            | Detected state (e.g., NY, CT)               |
| TowerJump        | Yes / No if it's likely a tower jump        |
| Confidence       | Percentage (50–100%)                        |
| Valid            | Whether the input row was valid             |

---

## 🧪 📊 Frontend UI (Optional)

- Interactive view of consolidated intervals
- Highlights tower jumps visually
- Responsive, scrollable table
- Pagination for large datasets
- Confidence level with color coding

---

## 🧠 Logic Overview

Tower Jumps are detected when:
- The device flips states too frequently
- The gap between two location states is very short (≤ 15 minutes)
- The switch is likely caused by triangulation noise rather than movement

Confidence is assigned per interval based on how long the user remained in a state.

Invalid records are preserved in the output with confidence = 0.

---

## 👨🏽‍💻 Author

[Bruno Vinícius](https://linkedin.com/in/bvmcarodso)  
Senior Full-Stack Engineer · Python · React · Distributed Systems