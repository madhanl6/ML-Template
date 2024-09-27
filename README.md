# ML Pipeline Template

This repository provides a Python script to set up a standard directory structure for machine learning projects. It helps you organize files and directories into a structured format that is ideal for developing, testing, and deploying ML models.

## Files

- `script.py`: A Python script to create a structured directory for an ML pipeline project.
- `Image.png`: An image showing the directory structure created by the script.

## Features

- **Automatic Directory Creation:** Creates essential directories for data, notebooks, source code, configuration, and more.
- **Placeholder Files:** Generates placeholder files with sample content to help you get started quickly.
- **Flexible Usage:** Allows specifying a base directory or using the current directory.
- **Self-Cleanup Option:** Offers the option to delete the script after creating the project structure.

## Usage

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/madhanl6/ML-Template.git
   cd ML-Template
   ```

2. **Run the Script**:
   - Make sure Python is installed. Run the script with:

   ```bash
   python script.py [<base_directory>]
   ```

   - If you provide a `<base_directory>`, the structure will be created there. For example:

   ```bash
   python script.py D:/Template
   ```

   - If you don't provide a base directory, the script will ask if you want to use the current directory.

3. **Follow the Prompts:**
   - If no base directory is provided, you'll be asked whether to use the current directory.
   - After creating the structure, you'll be asked if you want to delete the script file.

## Customization

The file `script.py` can be further modified to fit specific needs. For example, you might want to add more directories, change the placeholder content, or adjust the default structure according to your project requirements.

## Contributing

Contributions are welcome! If you have suggestions for improvements or additional features, please open an issue or submit a pull request. Feel free to modify any sections further to better suit your project needs!

  
