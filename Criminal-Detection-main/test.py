import unittest
import pyautogui
import subprocess
import time

class TestCriminalIdentificationSystem(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Start the Tkinter application
        cls.proc = subprocess.Popen(['python', 'home.py'])
        time.sleep(5)  # Wait for the app to fully load

    @classmethod
    def tearDownClass(cls):
        cls.proc.terminate()  # Ensure the app is closed after tests

    def test_register_criminal(self):
        # Navigate to the "Register Criminal" page
        res= pyautogui.locateCenterOnScreen("Register.png")
        print(res)
       # regisbut=pyautogui.center(res)
        pyautogui.moveTo(res)
        #pyautogui.click()
        pyautogui.click(x=1436, y=971)  
        # Adjust the x and y coordinates to the "Register Criminal" button
        time.sleep(15)

        # Input data into fields
    
        field_coords = {
            'Name': (200, 300),
            'Father\'s Name': (200, 340),
            'Mother\'s Name': (200, 380),
            'Gender': (200, 420),
            'DOB(yyyy-mm-dd)': (200, 460),
            'Blood Group': (200, 500),
            'Identification Mark': (200, 540),
            'Nationality': (200, 580),
            'Religion': (200, 620),
            'Crimes Done': (200, 660)
        }
        
        # Data to be entered in each field
    data = {
           'Name': 'Kartikey saini',
            'Father\'s Name': ' Sanjay Saini',
            'Mother\'s Name': 'Sarita Saini',
            'Gender': 'Male',
            'DOB(yyyy-mm-dd)': '1990-01-01',
            'Blood Group': 'O+',
            'Identification Mark': 'Scar on left cheek',
            'Nationality': 'Indian',
            'Religion': 'None',
            'Crimes Done': 'Theft'
        }

        # Enter data in each field
    for field, (x, y) in field_coords.items():
            pyautogui.click(x, y)  # Click to focus the field
            pyautogui.typewrite(data[field], interval=0.1)  # Type the input
            time.sleep(0.5)  # Wait a bit for UI to process

        # Click the "Register" button, assuming coordinates are (200, 700)
    pyautogui.click(200, 700)

        # Add assertions here if there are any expected outcomes to validate
        # For example, check for a dialog box, message, or database entry

if __name__ == '__main__':
    unittest.main()