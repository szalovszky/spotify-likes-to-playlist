# Spotify Liked Songs to Playlist(s)

Automate the organization of your liked songs on Spotify by automatically splitting them into playlists within Spotify's playlist track count limit (10,000). This is ideal for easily sharing your liked songs with others.

## Getting Started

### Prerequisites

- A Spotify account
- Python 3.x
- pip (Python package installer)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/szalovszky/spotify-likes-to-playlist.git
   ```

2. Navigate to the project directory:

   ```bash
   cd spotify-likes-to-playlist
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Configure your Spotify API credentials by creating a `.env` file with the following content:

   ```env
   SPOTIFY_CLIENT_ID=your_spotify_client_id
   SPOTIFY_CLIENT_SECRET=your_spotify_client_secret
   SPOTIFY_REDIRECT_URI=your_redirect_uri
   ```

   Replace `your_spotify_client_id` and `your_spotify_client_secret` with your actual Spotify API credentials. Also, provide a valid `SPOTIFY_REDIRECT_URI`. This should be the URI where the Spotify API will redirect the user after authentication. Make sure it matches the redirect URI you specified when registering your Spotify application.

### Usage

1. Run the application:

   ```bash
   python main.py
   ```

2. Follow the on-screen instructions to authenticate the app with your Spotify account.

3. Once authenticated, the app will create playlist(s) from your liked songs.

## License

spotify-likes-to-playlist is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Support and Contributions

For bug reports, feature requests, or contributions, please open an issue or submit a pull request on the GitHub repository.
