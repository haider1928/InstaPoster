# InstaPoster

InstaPoster is a Python application that takes a current news headline and a Hadith quote, places them on image templates, and saves the results in the output folder. When Instagram credentials are set up in a `.env` file, it can also upload the created images to an account.

The application fetches a news headline and a Hadith entry from online sources, then writes the text onto prepared background images. It keeps track of headlines that have already been used so it does not repeat the same story.

The code base is organized with the program entry point and configuration under `src`, image templates under `assets`, and generated images under `output`. The project uses Python 3.14 and depends on libraries listed in `requirements.txt`.

To prepare the project, install dependencies with `python -m pip install -r requirements.txt` and create a `.env` file from `.env.example`. Use `python main.py --dry-run` to generate images without posting them, and use `python main.py` once Instagram credentials are configured for optional upload.
