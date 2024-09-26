# YouTube Playlist Downloader Using Pytube

This demonstrates how to download all videos from a YouTube playlist using the `pytube` library in Python. The script fetches a playlist URL, iterates over the videos in the playlist, and downloads each video in its highest resolution.

## Prerequisites

Make sure to install the required Python package before running the script:

```bash
pip install pytube
```

---

## Python Code for Downloading YouTube Playlist

```python
from pytube import Playlist  # Import Playlist class from pytube

# Get the playlist URL from the user
playlist_url = input("Enter your playlist URL: ")
```

### Explanation:
- **`pytube.Playlist`**: This class is used to handle YouTube playlists and extract video information.
- **`input()`**: This function captures the playlist URL entered by the user.

---

```python
try:
    playlist = Playlist(playlist_url)
    print(f'Downloading: {playlist.title}')  # Display the playlist title
```

### Explanation:
- **`Playlist(playlist_url)`**: This initializes a Playlist object using the provided URL.
- **`playlist.title`**: Retrieves the title of the playlist and prints it.

---

```python
    # Iterate over the videos in the playlist
    for video in playlist.videos:
        try:
            print(f'Downloading {video.title}')  # Print the video title
            
            # Get the highest resolution available for the video
            highest_resolution_stream = video.streams.get_highest_resolution()
            
            # Download the video if a high-resolution stream is available
            if highest_resolution_stream:
                highest_resolution_stream.download()
            else:
                print(f"No high resolution stream available for {video.title}")
```

### Explanation:
- **`playlist.videos`**: This retrieves all the videos in the playlist.
- **`video.streams.get_highest_resolution()`**: Fetches the stream with the highest resolution for each video.
- **`download()`**: Downloads the video to the current directory.

---

```python
        except Exception as e:
            print(f"An error occurred while downloading {video.title}: {e}")  # Handle download errors
```

### Explanation:
- **Exception handling**: Catches any errors that occur during the download process for each video and prints the error message.

---

```python
    print("Download completed.")
except Exception as e:
    print(f"An error occurred: {e}")  # Handle errors with the playlist URL or initialization
```

### Explanation:
- **Top-level error handling**: Catches errors that occur during the initialization of the playlist (e.g., if the URL is invalid) and prints the error message.

---

## Full Example Code

```python
from pytube import Playlist

# Get the playlist URL from the user
playlist_url = input("Enter your playlist URL: ")

try:
    playlist = Playlist(playlist_url)
    print(f'Downloading: {playlist.title}')

    # Iterate over the videos in the playlist
    for video in playlist.videos:
        try:
            print(f'Downloading {video.title}')
            
            # Get the highest resolution available for the video
            highest_resolution_stream = video.streams.get_highest_resolution()
            
            # Download the video if a high-resolution stream is available
            if highest_resolution_stream:
                highest_resolution_stream.download()
            else:
                print(f"No high resolution stream available for {video.title}")
        except Exception as e:
            print(f"An error occurred while downloading {video.title}: {e}")

    print("Download completed.")
except Exception as e:
    print(f"An error occurred: {e}")
```

---

## Output

When you run this script, it will prompt you to enter the playlist URL. It will then download each video in the highest available resolution.

---

## Conclusion

This script provides an easy way to download an entire YouTube playlist using Python's `pytube` library. It handles common errors such as unavailable streams and invalid URLs, ensuring that the download process runs smoothly.
