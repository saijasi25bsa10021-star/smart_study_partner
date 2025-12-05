# 📚 Smart Study Partner

 It is a powerful study partner built with the he Streamlit for Science & Math revision and learning. This app helps you study efficiently by summarizing content, generating MCQs, and evaluating your answers.

## Features

-Topic-based Search: it help students by giving the information and work for searched work only
- Automatic Summarization: it automaticly summarize the topic for the students
- MCQ Generation: it will automaticly generates  the mcq for students to practice
- Answer Evaluation: it will give the score so that student can see their condition
- Dataset Support : Works with CSV files (train, validation, test sets)

## Tech Stack

- Frontend: Streamlit
- Backend: Python
- Data: Pandas, NumPy
- ML/NLP: BERT-based extractive summarizer, Transformers
- Environment: python-dotenv for configuration

## Installation

1. **Clone the repository**:
```bash
git clone https://github.com/saijasi25bsa10021-star/smart_study_partner.git
cd smart_study_partner
```

2. **Create a virtual environment** (optional but recommended):
```bash
python -m venv venv
venv\Scripts\activate
```

3. **Install dependencies**:
```bash
pip install -r requirements.txt
pip install bert-extractive-summarizer transformers torch
```

## Project Structure

```
smart_study_partner/
├── app.py                      # Main Streamlit application
├── summarizer_utils.py         # Text summarization utilities
├── my_summarizer.py            # Custom summarizer implementation
├── utils.py                    # MCQ generation & evaluation utilities
├── requirements.txt            # Python dependencies
├── dataset/                    # Study datasets
│   ├── train.csv
│   ├── validation.csv
│   └── test.csv
├── README.md                   # This file
├── STATEMENT.md                # Project mission & vision
├── presentation_outline.md     # Presentation structure
└── scripts/
    └── generate_ppt.py         # PPT generator script
```

## Usage

### Run the Application

```bash
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`

### How to Use

1. **Load Dataset**: The app automatically loads CSV files from the `dataset/` folder
2. **Enter Topic**: Type the topic you want to study (e.g., "photosynthesis", "quadratic equations")
3. **View Summary**: Get an AI-generated summary of relevant content
4. **Answer MCQs**: Answer auto-generated multiple-choice questions
5. **Get Feedback**: Receive instant evaluation of your answers

## Key Modules

### `app.py`
Main Streamlit application interface with:
- Dataset auto-loading
- Topic filtering
- Content display
- MCQ interface

### `summarizer_utils.py`
Handles text summarization using BERT-based extractive summarization

### `utils.py`
Contains functions for:
- MCQ generation from text
- Answer evaluation & scoring
- Dataset loading and preprocessing

### `my_summarizer.py`
Custom summarizer implementation for advanced use cases

```

### Dataset Format

CSV files should contain:
- `topic` or `subject` column
- `content` or `text` column
- `questions` or `passage` column

Example:
| topic | content | questions |
|-------|---------|-----------|
| Biology | Photosynthesis is... | What is photosynthesis? |

## Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## Troubleshooting

### Issue: Module not found errors
**Solution**: Ensure all dependencies are installed:
```bash
pip install -r requirements.txt
pip install bert-extractive-summarizer transformers torch
```

### Issue: CSV file not found
**Solution**: Ensure CSV files are in the `dataset/` folder

### Issue: Streamlit not running
**Solution**: Check your Python environment and try:
```bash
streamlit run app.py --logger.level=debug
```

## Performance Tips

- Pre-process large datasets to reduce loading time
- Use the validation set for faster testing
- Cache summarization results for repeated queries

## Future Enhancements

- Support for more file formats (XLSX, PDF, DOCX)
-  Multi-language support
-  User progress tracking & save sessions
-  Advanced analytics & learning insights
-  User authentication
-  Cloud deployment support

## License

This project is open-source. See `LICENSE` for details.

## Contact & Support

For issues, questions, or suggestions:
- Open an issue on GitHub
- Check the `STATEMENT.md` for project vision

## Author

**Repository**: [smart_study_partner](https://github.com/saijasi25bsa10021-star/smart_study_partner)

**Owner**: saijasi25bsa10021-star

---

**Last Updated**: December 5, 2025


