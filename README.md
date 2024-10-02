# ML Pipeline Template

This repository contains a Python script designed to establish a standard directory structure for machine learning projects. It helps you organize files and directories in a way that is conducive to developing, testing, and deploying ML models.

## Files

- `script.py`: A Python script to create a structured directory for an ML pipeline project.
- `Image.png`: An image showing the directory structure created by the script.

## Features

- **Automatic Directory Creation:** Creates essential directories for data, notebooks, source code, configuration, and more.
- **Placeholder Files:** Generates placeholder files with sample content to help you get started quickly.
- **Flexible Usage:** Offers the option to specify a base directory or use the current directory.
- **Self-Cleanup Option:** Provides the choice to delete the script after creating the project structure.

## Usage

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/madhanl6/ML-Template.git
   cd ML-Template
   ```

2. **Run the Script**:
   - Ensure Python is installed. You can run the script using:

   ```bash
   python script.py [<base_directory>]
   ```

   - If you specify a `<base_directory>`, the structure will be created there. For example:

   ```bash
   python script.py D:/Template
   ```

   - If you do not provide a base directory, simply run:
   
   ```bash
   python script.py
   ```

   - The script will then prompt you to confirm whether to use the current directory or specify a different one.

3. **Follow the Prompts:**
   - After creating the structure, you will be prompted to decide if you want to delete the folder containing the script file.

## Customization

The script.py file can be modified to suit your specific needs. You can add more directories, change the placeholder content, or adjust the default structure according to your project requirements.

## Contributing

Contributions are welcome! If you have suggestions for improvements or additional features, please open an issue or submit a pull request. Feel free to modify any sections further to better suit your project needs!

  
