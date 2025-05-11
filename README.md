# Music_scrapper, Liked Songs Downloader (For Personal Use Only)

This project is a **Python + Selenium script** that automates the process of scraping song names from your **Spotify Liked Songs** and finding/download them using a YouTube-to-MP3 conversion site. It's a personal automation tool created for educational purposes and to showcase my scripting and web automation skills.

> ⚠️ **Disclaimer**  
> This project is intended for personal, educational, and non-commercial use only. Downloading copyrighted content without proper authorization may violate the Terms of Service of platforms like YouTube and Spotify.  
> **The author does not condone piracy and assumes no responsibility for misuse of this code.**

---

## 💡 Features

- Automates login to Spotify via Selenium
- Extracts all song titles from your "Liked Songs" playlist
- Searches each song on YouTube
- Uses a YouTube-to-MP3 downloader to get the audio (if allowed)
- Logs any failed downloads

---

## 🚀 Tech Stack

- **Python 3**
- **Selenium** (with ChromeDriver)

---

## 🔧 Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/spotify-liked-songs-downloader.git
   cd spotify-liked-songs-downloader

2. Create a .env file and put put your username and password like so SPOTIFY_EMAIL=*****@gmail.com, SPOTIFY_PASSWORD=*****
3. Run the file called music_Scrapper.py