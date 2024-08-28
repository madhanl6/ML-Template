import os
import sys

def create_project_structure(base_dir):
    """Create a directory structure for the ML pipeline."""
    
    # Define the directory structure
    directories = [
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
        "backend/tests"
    ]
    
    files = {
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
        "backend/tests/test_utils.py": "# Tests for utility functions in backend"
    }
    
    # Create directories
    for directory in directories:
        os.makedirs(os.path.join(base_dir, directory), exist_ok=True)
    
    # Create files with placeholder content
    for file_path, content in files.items():
        full_path = os.path.join(base_dir, file_path)
        with open(full_path, 'w') as file:
            file.write(content)
    
    print(f"Project structure created successfully at {base_dir}")

def main():
    if len(sys.argv) < 2:
        print("python script.py <base_directory>")
        sys.exit(1)
    
    base_dir = sys.argv[1]
    create_project_structure(base_dir)

if __name__ == '__main__':
    main()
