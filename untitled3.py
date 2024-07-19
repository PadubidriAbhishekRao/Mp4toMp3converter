import os
from moviepy.editor import VideoFileClip
from pathlib import Path

def convert_mp4_to_mp3(input_folder, output_folder):
    Path(output_folder).mkdir(parents=True, exist_ok=True)
    mp4_files = [f for f in os.listdir(input_folder) if f.endswith('.mp4')]

    for mp4_file in mp4_files:
        mp4_path = os.path.join(input_folder, mp4_file)
        mp3_file = os.path.splitext(mp4_file)[0] + '.mp3'
        mp3_path = os.path.join(output_folder, mp3_file)

        print(f"Converting {mp4_file} to MP3...")
        try:
            video = VideoFileClip(mp4_path)
            video.audio.write_audiofile(mp3_path)
            video.close()
            print(f"Conversion complete: {mp3_file}")
        except Exception as e:
            print(f"Error converting {mp4_file}: {str(e)}")

    print("All conversions completed!")

if __name__ == "__main__":
    input_folder = input("Enter the input folder path: ")
    output_folder = input("Enter the output folder path: ")
    convert_mp4_to_mp3(input_folder, output_folder)
    input("Press Enter to exit...")