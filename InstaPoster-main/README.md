InstaPoster automatically fetches public news headlines and authentic hadiths, renders them onto images, and posts them to an Instagram account. It combines simple web scraping, image rendering, and Instagram publishing in a small Python pipeline.

Open InstaPoster and it looks for the latest news and short religious texts on the web. It chooses a short item that has not been posted before and prepares it for sharing.

![home screen](screenshots/home_screen.png)

The program writes the chosen words onto a background image so they appear like a shareable post. It saves the image and then sends the image to the connected Instagram account.

![post preview](screenshots/post_preview.png)

If the post goes up successfully the program records the headline so it does not post it again. If something goes wrong it writes a helpful message so a person can fix the problem.

![cli success](screenshots/cli_success.png)

Tech stack:
- Python (3.10+ recommended)
- Pillow for image manipulation
- requests + BeautifulSoup4 for web scraping
- instagrapi for Instagram publishing
- python-dotenv for environment variable loading

Project layout:
- src/: source code
  - src/main.py: pipeline entry point
  - src/config.py: path and environment handling
  - src/services/: scraping and external services
  - src/utils/: image and logging utilities
- assets/: image templates used as backgrounds
- data/: runtime files (headlines log)
- output/: generated images

Install and run:
1. Create and activate a virtual environment (optional but recommended).
2. Install dependencies:
   pip install -r requirements.txt
3. Copy .env.example to .env and set the required environment variables (instagram_username, instagram_password, newsapi if used).
4. Run the pipeline:
   python -m src.main

Configuration:
- Credentials and API keys must go into .env and must not be committed. The script reads instagram_username and instagram_password from environment variables.
