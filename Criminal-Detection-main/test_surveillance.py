# test_surveillance.py

import pyautogui
import pytest
import subprocess
import time

@pytest.fixture(scope="session", autouse=True)
def start_application():
    # Launch the application before starting the test
    proc = subprocess.Popen(['python', 'home.py'])
    time.sleep(5)  # Wait for the application to open
    yield
    proc.terminate()  # Terminate the application after tests are done

def test_video_surveillance(start_application):
    # Adjust the confidence as needed to find the button on your screen
    video_surveillance_button = pyautogui.locateCenterOnScreen('video_surveillance_button.png')
    assert video_surveillance_button is not None, "Video Surveillance button not found."
    pyautogui.click(video_surveillance_button)

    # Wait for the camera feed to initialize
    time.sleep(5)

    # Placeholder: you'll need an actual way to confirm the camera feed is open
    # Since pyautogui cannot check this directly, look for an on-screen indicator
    camera_indicator = pyautogui.locateCenterOnScreen('camera_indicator.png')
    
    # If the camera_indicator is not found within a certain time, the test should fail
    start_time = time.time()
    while True:
        if pyautogui.locateCenterOnScreen('camera_indicator.png'):
            break
        elif time.time() - start_time > 10:  # Timeout after 10 seconds
            assert False, "Camera feed did not start within 10 seconds."
        time.sleep(0.5)  # Check every half second

    # If the loop breaks and the assertion has not failed, the camera indicator was found
    assert True, "Camera feed started successfully."

if __name__ == "__main__":
    pytest.main(['-v', __file__])
