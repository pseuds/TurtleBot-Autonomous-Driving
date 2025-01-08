import cv2
import argparse

def parseargs():
    parser = argparse.ArgumentParser(description='Record video from TurtleBot camera.')
    parser.add_argument('-o', '--output', type=str, default="output.mp4", help='Name of output video file. (default: output.mp4)')
    args = parser.parse_args()
    return args


if __name__ == "__main__":
    args = parseargs()

    # Define the video capture object
    cap = cv2.VideoCapture(0)  # Use 0 for the default camera. Change the number if you have multiple cameras.

    # Check if the camera opened successfully
    if not cap.isOpened():
        print("Error: Could not open the camera.")
        exit()

    # Get the default video frame width and height
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    # Get output file name
    output_name = args.output + '.mp4' if not args.output[-4:] in ['.mp4'] else args.output

    # Define the codec and create VideoWriter object
    # 'XVID' is a popular codec. Use 'MJPG', 'X264', or other codecs as needed.
    out = cv2.VideoWriter(output_name, cv2.VideoWriter_fourcc(*'mp4v'), 20.0, (frame_width, frame_height))

    print("Recording... Press 'q' to stop.")

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Could not read frame.")
            break

        # Write the frame to the output file
        out.write(frame)

        # Display the frame (optional)
        cv2.imshow('Recording', frame)

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            print("Recording stopped.")
            break

    # Release the video objects and close the display window
    cap.release()
    out.release()
    cv2.destroyAllWindows()
