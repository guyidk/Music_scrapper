# **Spotify Liked Songs Downloader** — *Music Scraper*

This project is a **Python-based automation script** that logs into your **Spotify account**, scrapes your **Liked Songs**, and searches for each track on **YouTube** to download the **audio** using `yt-dlp`.

Built for **educational** and **personal use**, it demonstrates skills in **web automation, scraping**, and **scripting** using Selenium and `undetected-chromedriver`.

> **Disclaimer**  
> This script is for **educational, personal, and non-commercial use only**.  
> Downloading copyrighted content without permission may  
> violate the **Terms of Service** of YouTube and Spotify.  
> **The author does not condone piracy and assumes no responsibility for misuse.**

---

## **Features**

- Automated Spotify login with Selenium
- Scrapes all *Liked Songs* from your account
- Searches for each track on YouTube using `yt-dlp`
- Downloads the best available audio format (MP3/M4A)
- Interactive CLI selection of songs to download
- Logs any download errors for review
- Automatically scrolls through Spotify to load your full liked songs list

---

## 🛠 **Tech Stack**

- **Python 3**
- **Selenium** (via `undetected-chromedriver`)
- **yt-dlp** (for YouTube audio downloads)
- **python-dotenv** (for environment variable management)

---

## **Setup Instructions**

### 1. **Clone the repository**

```bash
git clone https://github.com/your-username/spotify-liked-songs-downloader.git
cd spotify-liked-songs-downloader