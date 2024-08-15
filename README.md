# Habsy

# Coupon Extraction from A4 Flyer

## Overview
A Python script to automatically crop multiple coupons from an A4 flyer and save
each coupon as a separate image file. The script should identify each coupon on the flyer
based on their distinct bordered regions and store the cropped images locally with a specific
naming convention.

## How to Run the Code

Follow these steps to set up and run the project:

### 1. Clone the Project

To get a local copy of the project, clone the repository using:

```bash
git clone <repository-url>
```

Replace `<repository-url>` with the URL of your Git repository.

### 2. Create a Python Environment

Navigate to the project directory and create a virtual environment:

```bash
python -m venv venv
```

### 3. Activate the Virtual Environment

- **On Windows:**

  ```bash
  .\venv\Scripts\activate
  ```

- **On macOS and Linux:**

  ```bash
  source venv/bin/activate
  ```

### 4. Install Required Packages

Install the necessary packages using pip:

```bash
pip install -r requirements.txt
```

### 5. Run the Script

Execute the main script:

```bash
python script1.py
```

## Additional Information

**Note:** In the `script1.py` file, you need to update the file paths according to your system. For example, modify the `image_paths` list to point to the correct locations on your machine:

```python
# Example usage:
image_paths = [
    "C:/Habsy/3_coupons.png",
    "C:/Habsy/4_coupons.png",
    "C:/Habsy/6_coupons.png"
]
```
