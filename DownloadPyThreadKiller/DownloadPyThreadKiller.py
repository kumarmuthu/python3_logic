__version__ = "2024.07.20.01"
__author__ = "Muthukumar Subramanian"

"""
Download the PythreadKiller package and Install/Upgrade on
"""

import os
import platform
import subprocess
import time
from collections import OrderedDict
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from prettytable import PrettyTable
import re
import multiprocessing


class DownloadPyThreadKiller:
    def __init__(self):
        options = Options()
        options.add_argument("--disable-notifications")
        options.add_argument("no-sandbox")
        options.add_argument("--disable-gpu")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument('--ignore-ssl-errors=yes')
        options.add_argument('--ignore-certificate-errors')
        options.add_argument("window-size=1400,600")
        options.add_argument("headless=new")

        # Initialize Chrome WebDriver
        self.browser = webdriver.Chrome(options=options)
        self.browser.maximize_window()
        self.browser.get('https://pypi.org/project/PyThreadKiller/')
        time.sleep(2)
        self.wait = WebDriverWait(self.browser, 10)
        self.final_dict = OrderedDict({})

    def get_download_dir(self):
        """Get the default download directory based on the OS."""
        if platform.system() == "Windows":
            return os.path.join(os.environ['USERPROFILE'], "Downloads")
        else:
            return os.path.join(os.path.expanduser("~"), "Downloads")

    def find_downloaded_file(self, download_dir, extension=".whl"):
        """Find the most recently downloaded file with the given extension in the download directory."""
        files = [os.path.join(download_dir, f) for f in os.listdir(download_dir) if f.endswith(extension)]
        return max(files, key=os.path.getctime) if files else None

    def delete_similar_files(self, download_dir):
        """Delete all files in the download directory that match the pattern but are not the valid filename."""
        files_to_delete = [f for f in os.listdir(download_dir) if f.startswith('PyThreadKiller') and f.endswith('.whl')]
        if files_to_delete:
            for file in files_to_delete:
                os.remove(os.path.join(download_dir, file))
                print(f"Deleted PyThreadKiller similar file(s): {file}")

    def download_files(self):
        print("{:*^30}".format(" Script Start "))
        try:
            # Click release history
            click_release_history = self.wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="history-tab"]')))
            click_release_history.click()
            print("Process done for Release history")

            # Click latest version
            click_latest_version = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="content"]/div[2]/div/div[2]/a')))
            click_latest_version.click()
            print("Process done for latest version")

            # Click download files tab
            click_download_files = self.wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="files-tab"]')))
            click_download_files.click()
            print("Process done for Download files")

            # Get the download directory
            download_dir_before = self.get_download_dir()
            self.delete_similar_files(download_dir_before)

            # Click download .whl file
            click_download_whl_file = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="files"]/div[2]/div[2]/a[1]')))
            click_download_whl_file.click()
            print("Process done for Select and download wheel(.whl) file")
            time.sleep(5)
            # Get the download directory
            download_dir_after = self.get_download_dir()

            # Find the most recently downloaded file
            downloaded_file = self.find_downloaded_file(download_dir_after)
            if downloaded_file:
                try:
                    print(f"Installing/upgrading: {downloaded_file}")
                    if platform.system() == "Windows":
                        # Install or upgrade the downloaded wheel file
                        sub_process_obj = subprocess.Popen(
                            ['cmd.exe', '/c', 'pip3.12 install %s --upgrade' % downloaded_file],
                            stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
                    else:
                        # Install or upgrade the downloaded wheel file
                        sub_process_obj = subprocess.Popen(['bash', '-c',
                                                            'pip3.12 install %s --upgrade' % downloaded_file],
                                                           stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
                    output_data, output_err_data = sub_process_obj.communicate()
                    print(f"Pip output_data:\n {output_data}\noutput_err_data:\n {output_err_data}")
                    sub_process_obj.terminate()
                    print(f"Installed/Upgraded: {downloaded_file}")
                except ValueError as e:
                    print(e)
                except subprocess.CalledProcessError as e:
                    print(f"Error installing/upgrading {downloaded_file}: {e}")

                # Delete the downloaded file
                os.remove(os.path.join(download_dir_after, downloaded_file))
                print(f"Deleted downloaded file: {downloaded_file}")
            else:
                print("No downloaded wheel file found.")

        except StaleElementReferenceException:
            print("Observed exception in Try block")

    def execute_test_scenarios(self):
        try:
            self.download_files()
        except StaleElementReferenceException:
            print("Observed exception in Try block")
        self.browser.quit()
        print("{:*^30}".format(" Script End "))


def main_script():
    cls_obj = DownloadPyThreadKiller()
    cls_obj.execute_test_scenarios()


if __name__ == '__main__':
    print("{:#^30}".format("Script Start"))
    multiprocess_obj = multiprocessing.Process(target=main_script)
    multiprocess_obj.start()
    multiprocess_obj.join(timeout=120)
    if multiprocess_obj.is_alive():
        multiprocess_obj.terminate()

    print("{:#^30}".format("Script End"))
