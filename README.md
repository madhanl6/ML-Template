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

## Future Releases

We have exciting plans for future updates to enhance the functionality and usability of this project:

1. **Customizable Templates:** Introduce the ability for users to define their own directory and file structures via configuration files.
2. **Interactive Command Line Interface (CLI):** Enhance the user experience by implementing an interactive CLI for better navigation and options.
3. **Version Control Integration:** Automate the initialization of Git repositories and provide basic setup for initial commits and branching.
4. **Environment Configuration:** Automatically set up virtual environments with specified packages and dependencies using `requirements.txt` or `environment.yml`.
5. **Enhanced Documentation:** Provide comprehensive guides and examples for various machine learning workflows using the generated project structure.

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

The `script.py` file can be modified to suit your specific needs. You can add more directories, change the placeholder content, or adjust the default structure according to your project requirements.

## Contributing

Contributions are welcome! If you have suggestions for improvements or additional features, please open an issue or submit a pull request. Feel free to modify any sections further to better suit your project needs!
