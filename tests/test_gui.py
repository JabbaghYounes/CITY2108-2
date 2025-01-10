import os
import time
import subprocess

def test_simulate_access():
    # construct correct path to main.py
    main_py_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../main.py"))

    # start porgram using path
    app_process = subprocess.Popen(["python3", main_py_path])
    
    # add load buffer time 
    time.sleep(5)

    # making sure main window is open
    result_main_window = subprocess.run(["xdotool", "search", "--name", "Room Access Control System"], capture_output=True, text=True)
    print(f"Main window search result: {result_main_window.stdout}")
    assert result_main_window.returncode == 0, "Main application window not found!"

    # moving and clicking mouse to simulate access button 
    simulate_button_coords = (1628, 674)  # grbbed button coordinantes xdotool getmouselocation
    subprocess.run(["xdotool", "mousemove", str(simulate_button_coords[0]), str(simulate_button_coords[1])])
    subprocess.run(["xdotool", "click", "1"])

    # add load buffer time for window to appear
    time.sleep(10)

    # listing all visible windows after clicking
    result_all_windows = subprocess.run(["xdotool", "search", "--onlyvisible"], capture_output=True, text=True)
    print(f"All visible windows: {result_all_windows.stdout}")

    # title matching to make sure simulate access window is open
    result_simulate_window = subprocess.run(["xdotool", "search", "--name", "Simulate"], capture_output=True, text=True)
    print(f"Simulate Access window search result: {result_simulate_window.stdout}")
    assert result_simulate_window.returncode == 0, "Simulate Access window did not open!"

    # porgram shutdown
    app_process.terminate()

if __name__ == "__main__":
    test_simulate_access()
