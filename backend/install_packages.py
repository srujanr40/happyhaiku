import subprocess
import os

def install_packages():
    packages = ['pandas', 'certifi', 'nltk', 'praw', 'python-dotenv', 'flask']

    for package in packages:
        try:
            print(f"Installing {package}...")
            subprocess.check_call(['pip', 'install', package])
            print(f"{package} installed successfully!")
        except subprocess.CalledProcessError:
            print(f"Error installing {package}.")

def download_nltk_data():
    try:
        import nltk
        nltk_data_dir = nltk.data.find('nltk_data')
        if not os.path.exists(nltk_data_dir):
            os.makedirs(nltk_data_dir)
        nltk.download('all', download_dir=nltk_data_dir)
        print("NLTK data downloaded successfully!")
    except Exception as e:
        print(f"Error downloading NLTK data: {str(e)}")

if __name__ == "__main__":
    install_packages()
    download_nltk_data()
