# Eye Tracking Project

This project implements an eye tracking system that calculates user attention based on their gaze direction while browsing products online, such as on e-commerce platforms.

## Project Structure

```
eye-tracking-project
├── src
│   ├── main.py                # Entry point of the application
│   ├── eye_tracking           # Module for eye detection and tracking
│   │   ├── __init__.py       
│   │   ├── detector.py        # Contains EyeDetector class for face and eye detection
│   │   └── tracker.py         # Contains EyeTracker class for tracking eye movements
│   ├── attention_analysis      # Module for analyzing attention based on gaze data
│   │   ├── __init__.py       
│   │   └── analyzer.py        # Contains AttentionAnalyzer class for analyzing gaze data
│   └── utils                  # Utility functions for the project
│       ├── __init__.py       
│       └── helpers.py         # Contains helper functions for model loading and frame preprocessing
├── requirements.txt           # Lists project dependencies
├── README.md                  # Project documentation
└── .gitignore                 # Specifies files to ignore in version control
```

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   cd eye-tracking-project
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Run the application:
   ```
   python src/main.py
   ```

## Usage Guidelines

- The application will initialize the eye tracking system and start analyzing attention based on the user's gaze.
- Ensure that your webcam is accessible and permissions are granted for video capture.
- The system will provide real-time feedback on where the user is looking and generate attention reports based on the gaze data.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.