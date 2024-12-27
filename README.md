# digital-analog-clock

# Digital-Analog Clock

A unique web-based clock that combines digital and analog concepts. Instead of traditional clock hands, it uses numbers that rotate around the center, creating an innovative way to display time.

Live demo: [Digital-Analog Clock](https://digital-analog-clock.onrender.com/)

## Features

- **Hour Display**: 3 rotating numbers showing the current hour
- **Minute Display**: 5 rotating numbers showing the current minutes
- **Second Display**: 6 rotating numbers showing the current seconds
- **Modern Design**:
  - Light blue color scheme (#aacde2)
  - Canvas size: 600x600 pixels
  - Bold numbers (24px Arial font)
  - Clean border around the clock
- **Responsive Design**: Centered layout that works on both desktop and mobile devices

## Technologies Used

- Python (Flask)
- HTML5 Canvas
- Inline CSS for basic styling

## Project Structure
```
project/
├── app.py
├── requirements.txt
├── Procfile
└── templates/
    └── index.html
```

## Local Development

1. Clone the repository
```bash
git clone [your-repository-url]
cd [repository-name]
```

2. Install dependencies
```bash
pip install -r requirements.txt
```

3. Run the application
```bash
python app.py
```

4. Open `http://localhost:5000` in your browser

## Deployment

This project is deployed on Render.com using their free tier. Note that the application may take a few moments to wake up if it hasn't been accessed recently due to the free tier limitations.

## Author

Created by [Sandreke](https://linktr.ee/sandreke99)

## License

This project is open source and available under the [MIT License](LICENSE).
