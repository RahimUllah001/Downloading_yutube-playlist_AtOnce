from pytube import Playlist

playlist_url = input("Enter your playlist URL: ")

try:
    playlist = Playlist(playlist_url)
    print(f'Downloading: {playlist.title}')

    for video in playlist.videos:
        try:
            print(f'Downloading {video.title}')
            highest_resolution_stream = video.streams.get_highest_resolution()
            if highest_resolution_stream:
                highest_resolution_stream.download()
            else:
                print(f"No high resolution stream available for {video.title}")
        except Exception as e:
            print(f"An error occurred while downloading {video.title}: {e}")

    print("Download completed.")
except Exception as e:
    print(f"An error occurred: {e}")
