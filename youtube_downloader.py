import sys
import os
import yt_dlp

def create_directory(path):
    if not os.path.exists(path):
        os.makedirs(path)
        print(f"Created directory: {path}")
    else:
        print(f"Directory already exists: {path}")

def download_video(video_url, download_path="downloads"):
    try:
        # Ensure the download path exists
        create_directory(download_path)

        ydl_opts = {
            'outtmpl': f'{download_path}/%(title)s.%(ext)s',
            'ignoreerrors': True,  # Equivalent to -i
            'no_abort_on_error': True  # Continue with next video on errors
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print(f"Downloading video from {video_url}")
            ydl.download([video_url])
        print(f"Downloaded video to {download_path}")
    except Exception as e:
        print(f"Error downloading {video_url}: {e}")

def download_playlist(playlist_url, download_path="downloads"):
    try:
        # Ensure the download path exists
        create_directory(download_path)

        ydl_opts = {
            'outtmpl': f'{download_path}/%(playlist)s/%(playlist_index)s - %(title)s.%(ext)s',
            'ignoreerrors': True,  # Equivalent to -i
            'no_abort_on_error': True  # Continue with next video on errors
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print(f"Downloading playlist from {playlist_url}")
            ydl.download([playlist_url])
        print(f"Downloaded playlist to {download_path}")
    except Exception as e:
        print(f"Error downloading playlist {playlist_url}: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python youtube_downloader.py <url> [download_path]")
        sys.exit(1)

    url = sys.argv[1]
    download_path = sys.argv[2] if len(sys.argv) > 2 else "downloads"

    if "playlist" in url.lower():
        download_playlist(url, download_path)
    else:
        download_video(url, download_path)

    print("Download complete.")
