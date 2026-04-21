# InstaPoster

InstaPoster is an automated Instagram poster application that fetches news headlines from Dawn, retrieves authentic Hadiths from `sunnah.com`, intelligently writes the content onto base images using Python Imaging Library (Pillow), and systematically publishes them online.

## Architecture

This project strictly follows Software Engineering Best Practices, separating functionality into modular components for high readability, maintainability, and scalability.

```text
InstaPoster/
├── .env                  # Environment Variables (keep secret)
├── .env.example          # Template for credentials setup
├── README.md             # The current documentation
├── requirements.txt      # Dependency configurations
├── assets/               # Folder storing graphical templates
│   ├── hadith.jpg          
│   └── your_image.jpg      
├── data/                 # Dynamic logfiles or DB persistence
│   └── headlines.txt       
├── output/               # Generative outputs prior to uploading
└── src/                  # The root package execution environment
    ├── config.py         # Application level variable storage
    ├── main.py           # Core algorithmic pipeline entrypoint
    ├── services/         # Interactions interacting over the network
    │   ├── hadith.py       
    │   ├── instagram.py    
    │   └── news.py         
    └── utils/            # Data-structures and utility functionality
        ├── image.py        
        └── logger.py       
```

## Features

- **Automated Logging System:** Integrated `logging` implementation ensuring robust tracing.
- **Fail-Safe HTTP Handlers:** Integrates generic connection error management avoiding silent crashes.
- **Pillow Data Enhancer:** Algorithm dynamically splits long strings onto graphics via width-wrapping heuristics to preserve contextual word readability.
- **Dynamic Content Discovery:** Identifies duplication states explicitly, ensuring the stream only generates fresh unique headlines.

## Installation

1. Construct the pipeline dependencies locally via:
```bash
pip install -r requirements.txt
```

2. Establish `.env` variables via the schema specified in `.env.example`.

## Execution Process

```bash
python -m src.main
```
