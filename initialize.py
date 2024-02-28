import subprocess
import os


try:
    import nltk
    nltk_data_dir = os.path.join(os.path.dirname(__file__), 'backend', 'nltk_data')
    if not os.path.exists(nltk_data_dir):
        os.makedirs(nltk_data_dir)
    nltk.download('all', download_dir=nltk_data_dir)
    print("NLTK data downloaded successfully!")
except Exception as e:
    print(f"Error downloading NLTK data: {str(e)}")

