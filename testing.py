import cv2
import os
import time
import logging
import subprocess
import shutil
import psutil
import sys

logging.basicConfig(filename='app.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def log_info(message):
    """
    Logs an info message to the app.log file.
    Args:
        message (str): The info message to log.
    """
    logging.info(message)

def log_error(message):
    """
    Logs an error message to the app.log file.
    Args:
        message (str): The error message to log.
    """
    logging.error(message)
def initialize_camera():
    try:
        cap = cv2.VideoCapture(0)
        cap.set(3, 640)
        cap.set(4, 480)
        return cap
    except Exception as e:
        log_error(f"Error initializing camera: {str(e)}")
        return None
def create_output_directory(empl_id):
    try:
        output_dir = os.path.join("C:\\xampp\\htdocs\\hg\\uploads", empl_id)

        if not os.path.exists(output_dir):
            os.makedirs(output_dir, exist_ok=True)

        log_info(f"Created/accessed output directory: {output_dir}")
        return output_dir
    except Exception as e:
        logging.error(f"An error occurred: {str(e)}")
        print(f"An error occurred: {str(e)}")
        return None
def capture_frames(cap, output_dir, video_duration):
    try:
        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        video_out = cv2.VideoWriter(os.path.join(output_dir, "captured_video.avi"), fourcc, 20.0, (640, 480))

        capture_count = 0

        video_start_time = time.time()  

        while (time.time() - video_start_time) < video_duration:
            ret, frame = cap.read()
            if not ret:
                continue

            cv2.imshow("Capture Video", frame)
            video_out.write(frame)
            frame_file_name = os.path.join(output_dir, f"frame_{capture_count:04d}.jpg")
            cv2.imwrite(frame_file_name, frame)
            capture_count += 1
            print(f"Captured {capture_count} frames.")
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        video_out.release()
        cv2.destroyAllWindows()

        log_info(f"Captured {capture_count} frames.")
        return capture_count
    except Exception as e:
        log_error(f"Error capturing frames: {str(e)}")
        return None


def main():
    try:
        if len(sys.argv) < 3:
            print("Usage: python testing.py <empl_id> <duration>")
            return
        empl_id = sys.argv[1]
        duration = int(sys.argv[2])

        log_info(f"User entered name: {empl_id}")
        video_duration = duration 

        cap = initialize_camera()
        if cap is None:
            log_error("Camera initialization failed. Exiting.")
            return

        output_dir = create_output_directory(empl_id)
        if output_dir is None:
            log_error("Output directory creation failed. Exiting.")
            return

        start_time = time.time()
        capture_count = capture_frames(cap, output_dir, video_duration)
        if capture_count is None:
            log_error("Frame capture failed. Exiting.")
            return 
        end_time = time.time()
        execution_time = end_time - start_time
        cpu_usage = psutil.cpu_percent()

        print(f"Execution time: {execution_time:.2f} seconds")
        print(f"CPU Usage: {cpu_usage}%")
        print(f"{capture_count} frames captured and saved in the directory '{output_dir}'.")
        image_path = os.path.join(output_dir, "captured_video.avi")
        log_info(f"Execution time: {execution_time:.2f} seconds")
        log_info(f"CPU Usage: {cpu_usage}%")
        log_info(f"{capture_count} frames captured and saved in the directory '{output_dir}'.")
        log_info(f"Image path stored in the database: {image_path}")
    except Exception as e:
        log_error(f"An error occurred: {str(e)}")
    finally:
        if cap is not None:
            cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
