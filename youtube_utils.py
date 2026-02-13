import re
from youtube_transcript_api import YouTubeTranscriptApi


def extract_video_id(url):
    regex = r"(?:v=|\/)([0-9A-Za-z_-]{11})"
    match = re.search(regex, url)
    return match.group(1) if match else None


def get_transcript(video_url):
    video_id = extract_video_id(video_url)

    if not video_id:
        return None

    api = YouTubeTranscriptApi()
    transcript_list = api.fetch(video_id)

    full_text = " ".join([item.text for item in transcript_list])

    return full_text
