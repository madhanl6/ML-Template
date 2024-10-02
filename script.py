import os
import sys
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

DIRECTORIES = [
    "data/raw",
    "data/processed",
    "notebooks",
    "src/utils",
    "tests/integration_tests",
    "config",
    "logs",
    "scripts",
    "frontend/static",
    "frontend/templates",
    "backend/api",
    "backend/services",
    "backend/models",
    "backend/tests",
]

FILES = {
    "src/__init__.py": "",
    "src/data_preprocessing.py": "# Data cleaning and preprocessing code here",
    "src/feature_engineering.py": "# Feature engineering code here",
    "src/model.py": "# Model definition and training code here",
    "src/utils/__init__.py": "",
    "src/utils/logging.py": "# Logging configuration code here",
    "src/utils/config.py": "# Configuration handling code here",
    "src/utils/helpers.py": "# Additional helper functions code here",
    "tests/__init__.py": "",
    "tests/test_data_preprocessing.py": "# Tests for data preprocessing",
    "tests/test_feature_engineering.py": "# Tests for feature engineering",
    "tests/test_model.py": "# Tests for model",
    "tests/test_utils.py": "# Tests for utility functions",
    "tests/integration_tests/test_api.py": "# Integration tests for FastAPI endpoints",
    "tests/integration_tests/test_frontend.py": "# Integration tests for Streamlit components",
    "config/config.yaml": "# Configuration parameters",
    "config/logging.yaml": "# Logging configuration",
    "scripts/train_model.py": "# Script to train the model",
    "scripts/data_pipeline.py": "# Script for data pipeline management",
    "requirements.txt": "# Python dependencies for the entire project",
    "environment.yml": "# Conda environment file",
    "Dockerfile": "# Dockerfile for common usage",
    "docker-compose.yml": "# Docker Compose file",
    ".dockerignore": "# Files and directories to exclude from Docker context",
    ".env": "# Environment variables",
    "README.md": "# Project overview and instructions",
    ".gitignore": "# Git ignore file",
    "frontend/app.py": "# Main Streamlit application",
    "frontend/Dockerfile": "# Dockerfile for Streamlit",
    "frontend/requirements.txt": "# Python dependencies for Streamlit",
    "backend/main.py": "# Main FastAPI application",
    "backend/api/__init__.py": "",
    "backend/api/endpoints.py": "# API endpoints",
    "backend/services/example_service.py": "# Example service",
    "backend/models/__init__.py": "",
    "backend/models/example_model.py": "# Example Pydantic model",
    "backend/Dockerfile": "# Dockerfile for FastAPI",
    "backend/requirements.txt": "# Python dependencies for FastAPI",
    "backend/tests/__init__.py": "",
    "backend/tests/test_endpoints.py": "# Tests for FastAPI endpoints",
    "backend/tests/test_utils.py": "# Tests for utility functions in backend",
}


def create_project_structure(base_dir):
    """Create a directory structure for the ML pipeline."""
    
    # Create directories
    for directory in DIRECTORIES:
        os.makedirs(os.path.join(base_dir, directory), exist_ok=True)
    
    # Create files with placeholder content
    for file_path, content in FILES.items():
        full_path = os.path.join(base_dir, file_path)
        try:
            with open(full_path, "w") as file:
                file.write(content)
        except IOError as e:
            logging.error(f"Failed to create file {full_path}: {e}")

    logging.info(f"Project structure created successfully at {base_dir}")


def get_base_directory():
    """Get the base directory for project structure from user input."""
    if len(sys.argv) == 2:
        return sys.argv[1]
    
    while True:
        user_input = input(
            "Do you want to generate the project structure in the current directory? (y/n): "
        ).strip().lower()
        
        if user_input == "y":
            return os.getcwd()
        elif user_input == "n":
            base_dir = input("Please enter the desired directory path: ").strip()
            if os.path.isdir(base_dir):
                return base_dir
            else:
                logging.error(f"The directory '{base_dir}' does not exist. Please provide a valid directory.")
        else:
            logging.warning("Invalid input. Please enter 'y' or 'n'.")


def main():
    base_dir = get_base_directory()
    create_project_structure(base_dir)

    # Ask the user to delete this Python file
    logging.info("Project structure has been created. You can now delete this Python file.")
    delete_input = input("Do you want to delete this Python file? (y/n): ").strip().lower()
    if delete_input == "y":
        try:
            os.remove(__file__)
            logging.info("This Python file has been deleted.")
        except Exception as e:
            logging.error(f"Failed to delete the file: {e}")
    else:
        logging.info("This Python file was not deleted. You may want to remove it manually later.")

if __name__ == "__main__":
    main()
