# CWT Ads Agent

An automated video generation pipeline that leverages **Python** for asset orchestration and **Remotion (React)** for programmatic video rendering.

## 🚀 Features
- **Automated Orchestration**: Python script handles file management and JSON timeline generation.
- **Dynamic Rendering**: React-based video engine that adapts to provided assets.
- **High Performance**: Optimized for rapid rendering on Apple Silicon (MacBook Air).

## 🛠️ Setup & Installation

### 1. Python Environment
```bash
# Create and activate virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Remotion Setup
```bash
cd cwt-remotion
npm install
```

## 🎥 Usage
1. Place your background image (`bg.png`) and voiceover (`voice.mp3`) in the root directory.
2. Run the pipeline:
   ```bash
   python3 main.py
   ```
3. Find your rendered video in the `output/` folder.

## 🎓 Author
**Pratyay Roy**  
*Computer Science Engineering (AIML)*  
*Techno India University, Kolkata*
