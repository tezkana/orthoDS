from PIL import Image
import os

source_file = "Unidad Dental.webp"
output_prefix = "frame_"

if not os.path.exists(source_file):
    print(f"Error: {source_file} not found.")
    exit(1)

try:
    with Image.open(source_file) as im:
        print(f"Opened {source_file}")
        print(f"Total frames: {im.n_frames}")
        
        for i in range(im.n_frames):
            im.seek(i)
            # frame_001.webp to frame_148.webp (1-based index to match JS)
            frame_num = i + 1 
            output_filename = f"{output_prefix}{frame_num:03d}.webp"
            im.save(output_filename, "WEBP")
            if i % 10 == 0:
                print(f"Saved {output_filename}")
        
        print(f"Extraction complete. Extracted {im.n_frames} frames.")

except Exception as e:
    print(f"An error occurred: {e}")
