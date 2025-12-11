# PC Build Recommender 2

A lightweight and intelligent PC component recommendation system powered by **Gemini 2.5 LLM**.  
The tool generates accurate and balanced PC build configurations based on the user's budget, workload, and specific requirements.

---

## 🚀 Features

- AI-driven component selection using Gemini 2.5  
- Use-case optimized builds (Gaming, ML/AI, Editing, Productivity, etc.)  
- Budget-aware recommendations  
- Compatibility-focused outputs (socket, wattage, form factor)  
- Extensible architecture for additional LLMs or rules  
- Lightweight Python project with minimal setup  

---

## 📁 Project Structure

PC-Build-Recommender2/
│
├── app/ # Core application logic
├── assets/ # Static files or resources
├── requirements.txt # Dependencies
├── .gitattributes
└── README.md # Documentation

yaml
Copy code

---

## 🛠️ Installation

### 1. Clone the repository

git clone https://github.com/Chiranthan497/PC-Build-Recommender

2.git
cd PC-Build-Recommender2

2. Install dependencies
bash
Copy code
pip install -r requirements.txt
▶️ Usage
Run the application (update entry point if needed):

bash
Copy code
python app/main.py
Provide inputs such as:

Budget

Use case

Preferred hardware constraints

The system will query Gemini 2.5 and return a structured PC build.

📦 Example Output
vbnet
Copy code
Recommended PC Build (ML/AI – ₹120,000 Budget)

CPU: AMD Ryzen 7 5700X

GPU: NVIDIA RTX 4060 Ti

RAM: 32GB DDR4 3600MHz

Storage: 1TB NVMe SSD

Motherboard: B550 ATX

PSU: 650W 80+ Gold

Case: Mid Tower Airflow

Reasoning:
Optimized for training small to medium ML models with strong GPU acceleration
and balanced thermals under sustained loads.
🔮 Future Enhancements
Live price aggregation

Region-specific store support

Web UI (Streamlit/FastAPI)

GPT / LLaMA model support

Local build history

## 👨‍💻 Contributors
1. Chiranthan (1MS22CS048)

2. Adarsh Bennur (1MS22CS008)

3. Darshan Chouthayi (1MS22CS049)


## 📜 License
MIT License
