# Parallelepiped Analysis Application

## Overview

This application processes data about parallelepipeds, calculates their geometric properties, and generates statistical reports in JSON and HTML formats.

## Quick Deployment

### Manual Setup Steps

1. Clone the repository

   ```bash
   git clone https://github.com/krekrekerok/Parallelepiped_task
   cd Parallelepiped_task
   ```

2. Run the application
   ```bash
   python main.py
   ```

## Project Structure

```
project/
├── main.py                 # Main script
├── parallelepipeds.json    # Input data with parallelepiped dimensions
├── utils/
│   ├── __init__.py         # Utils package initialization
│   ├── characteristics.py  # Mathematical functions & characteristics output
│   ├── statistics.py       # Mathematical functions & statistics output
│   └── html.py             # HTML report generation
└── outputs/                # Output files directory
    ├── characteristics.json
    ├── statistics.json
    └── data_summary.html
```

## What the Application Does

- Reads parallelepiped dimensions from a JSON file
- Calculates properties like diagonal, volume, surface area, angles, and sphere parameters
- Computes averages across all parallelepipeds
- Generates an HTML report with visualizations
- Outputs data to JSON files for further analysis

## Requirements

- Python 3.6+
- No external dependencies (uses only standard library)

## Output Files

- `characteristics.json`: Detailed data for each parallelepiped
- `statistics.json`: Statistical summary across all figures
- `data_summary.html`: Interactive HTML report with statistics and ASCII animation

## Customization

- Edit `parallelepipeds.json` to analyze different figures
- Modify calculations in `utils/characteristics.py`
- Change report design in `utils/html.py`

## Troubleshooting

- Ensure the `outputs` directory exists before running
- Verify that your Python version is 3.6 or newer
- Check `parallelepipeds.json` for valid JSON syntax if errors occur
