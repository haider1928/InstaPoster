# InstaPoster

InstaPoster is a Python application that turns a live news headline and a Hadith quote into polished image content. It creates one image for the news item and one image for the Hadith, saves both images to the output folder, and can optionally publish them to Instagram when credentials are provided.

## What it does

The application performs these steps:

1. Read configuration values from a `.env` file.
2. Fetch current headlines from a news service.
3. Fetch a Hadith quote from an online source.
4. Add the headline and the Hadith text onto separate image templates.
5. Save the generated images to the `output` folder.
6. If Instagram credentials are configured, log in and upload the generated images.
7. Record the headline text in a local history file so it does not get reused later.

## How it works

When `main.py` runs, it starts by loading settings and preparing the logger. It fetches news items, then selects the first headline that has not already been posted and is within the allowed length. It also fetches a Hadith from the Hadith service.

The image editor takes the selected text and writes it onto each template image. The news image receives the headline and its description. The Hadith image receives the Hadith text and a reference URL when available.

If the tool is run with `--dry-run`, it stops after generating the images. When dry run is not enabled, it connects to Instagram using the supplied username and password, uploads each generated image, and then logs out.

## Configuration

The project reads values from `.env`. The file should include at least the Instagram username and password, and any optional keys required by the news source. Use `.env.example` as a template.

The pipeline also uses a local headline history file to avoid posting the same story twice. That file is stored in the repository data folder and updated automatically after a successful news upload.

## Setup and usage

Install dependencies with:

```bash
python -m pip install -r requirements.txt
```

Set up your environment file from `.env.example`. Then run the generator in dry run mode to verify image creation:

```bash
python main.py --dry-run
```

When you are ready to publish, run:

```bash
python main.py
```

## Project structure

The repository is organized to keep the main pipeline, configuration, services, and utilities separate.

- `src/` contains the application code.
- `src/config.py` defines paths and settings.
- `src/main.py` is the program entry point.
- `src/services/` includes news, Hadith, and Instagram integration.
- `src/utils/` contains image editing and logging helpers.
- `assets/` holds the image templates used for generation.
- `output/` receives the generated images.

This structure makes it easier to update the image generation logic, swap data sources, or adjust the Instagram upload process without changing the whole application.
