from selenium import webdriver
from edb import getcontent
import time
import os
import zipfile
download_dir=os.path.expanduser("~/Downloads")


# SA-downloads script from exploit-db if possible


def download(id,browser):
    if getcontent(id)!="0":
        if browser=="CHROME":
            url = getcontent(id)

            # Configure Chrome WebDriver
            chrome_options = webdriver.ChromeOptions()

            # Initialize Chrome WebDriver
            driver = webdriver.Chrome(options=chrome_options)

            # Navigate to the URL
            driver.get(url)

            # Wait for 5 seconds
            time.sleep(5)

            # Close the Chrome WebDriver window
            driver.quit()
        elif browser=="FIREFOX":
            url = getcontent(id)
            # Initialize Firefox WebDriver
            driver = webdriver.Firefox()

            # Navigate to the URL
            driver.get(url)
            time.sleep(5)
            driver.quit()
        elif browser=="EDGE":
            url = getcontent(id)

            # Configure Microsoft Edge WebDriver
            edge_options = webdriver.EdgeOptions()

            # Initialize Microsoft Edge WebDriver
            driver = webdriver.Edge(options=edge_options)

            # Navigate to the URL
            driver.get(url)

            # Wait for 5 seconds
            time.sleep(5)

            # Close the Microsoft Edge WebDriver window
            driver.quit()

    else:
        print("No exploit-db links")



#SA-open_ref opens reference links

def open_ref(id,browser):

    if getcontent(id)!="0":
        if browser=="CHROME":
            url = getcontent(id)

            # Configure Chrome WebDriver
            chrome_options = webdriver.ChromeOptions()

            # Initialize Chrome WebDriver
            driver = webdriver.Chrome(options=chrome_options)

            # Navigate to the URL
            driver.get(url)

            # Wait for 5 seconds
            time.sleep(5)

            # Close the Chrome WebDriver window
            driver.quit()

        #to open lnks in Firefox
        
        elif browser=="FIREFOX":
            url = getcontent(id)
            # Initialize Firefox WebDriver
            driver = webdriver.Firefox()

                # Navigate to the URL
            driver.get(url)
            time.sleep(5)
            driver.quit()

        #to open links in Edge
        elif browser=="EDGE":
            url = getcontent(id)

            # Configure Microsoft Edge WebDriver
            edge_options = webdriver.EdgeOptions()

            # Initialize Microsoft Edge WebDriver
            driver = webdriver.Edge(options=edge_options)

            # Navigate to the URL
            driver.get(url)

            # Wait for 5 seconds
            time.sleep(5)

            # Close the Microsoft Edge WebDriver window
            driver.quit()
        all_files = os.listdir(download_dir)

        # Sort the files by modification time to get the top 2
        all_files.sort(key=lambda x: os.path.getmtime(os.path.join(download_dir, x)), reverse=True)
        top_two_files = all_files[:2]

        if len(top_two_files) < 2:
            print("There are not enough files to create a zip archive.")
            return

        # Create a zip file with a generic name
        zip_filename = os.path.join(download_dir, 'top_two_files.zip')

        with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for file in top_two_files:
                file_path = os.path.join(download_dir, file)
                zipf.write(file_path, os.path.basename(file_path))
    else:
        print("No exploit-db links")
    if browser == "FIREFOX":
        url1 = f"https://nvd.nist.gov/vuln/detail/{id}"
        url2 = f"https://cve.mitre.org/cgi-bin/cvename.cgi?name={id}"
        url4 = f"https://vulners.com/search?query={id}"
        url3 = f"https://vulmon.com/vulnerabilitydetails?qid={id}"

        # Initialize Firefox WebDriver
        driver = webdriver.Firefox()
        driver.get(url1)  # Open the first URL in the main tab

        # Open the subsequent URLs in new tabs
        driver.execute_script("window.open('about:blank', '_blank');")  # Open a new tab
        driver.switch_to.window(driver.window_handles[1])  # Switch to the new tab
        driver.get(url2)

        driver.execute_script("window.open('about:blank', '_blank');")  # Open another new tab
        driver.switch_to.window(driver.window_handles[2])  # Switch to the new tab
        driver.get(url3)

        driver.execute_script("window.open('about:blank', '_blank');")  # Open yet another new tab
        driver.switch_to.window(driver.window_handles[3])  # Switch to the new tab
        driver.get(url4)

        # Close the original tab (optional)
        driver.switch_to.window(driver.window_handles[0])

    elif browser == "EDGE":

        url1 = f"https://nvd.nist.gov/vuln/detail/{id}"
        url2 = f"https://cve.mitre.org/cgi-bin/cvename.cgi?name={id}"
        url3 = f"https://vulners.com/search?query={id}"
        url4 = f"https://vulmon.com/vulnerabilitydetails?qid={id}"
        user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"

        # Configure Microsoft Edge WebDriver with the custom user-agent
        edge_options = webdriver.EdgeOptions()
        edge_options.add_argument(f"user-agent={user_agent}")

        # Initialize Microsoft Edge WebDriver with the custom user-agent
        driver = webdriver.Edge(options=edge_options)
        driver.get(url1)  # Open the first URL in the main tab

        # Open the subsequent URLs in new tabs
        driver.execute_script("window.open('about:blank', '_blank');")  # Open a new tab
        driver.switch_to.window(driver.window_handles[1])  # Switch to the new tab
        driver.get(url2)

        driver.execute_script("window.open('about:blank', '_blank');")  # Open another new tab
        driver.switch_to.window(driver.window_handles[2])  # Switch to the new tab
        driver.get(url3)

        driver.execute_script("window.open('about:blank', '_blank');")  # Open yet another new tab
        driver.switch_to.window(driver.window_handles[3])  # Switch to the new tab
        driver.get(url4)
        time.sleep(3600)

    elif browser=="CHROME":
        url1 = f"https://nvd.nist.gov/vuln/detail/{id}"
        url2 = f"https://cve.mitre.org/cgi-bin/cvename.cgi?name={id}"
        url3 = f"https://vulners.com/search?query={id}"
        url4 = f"https://vulmon.com/vulnerabilitydetails?qid={id}"
        user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"

        # Configure Chrome WebDriver with the custom user-agent
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument(f"user-agent={user_agent}")

        # Initialize Chrome WebDriver with the custom user-agent
        driver = webdriver.Chrome(options=chrome_options)
        driver.get(url1)  # Open the first URL in the main tab

        # Open the subsequent URLs in new tabs
        driver.execute_script("window.open('about:blank', '_blank');")  # Open a new tab
        driver.switch_to.window(driver.window_handles[1])  # Switch to the new tab
        driver.get(url2)

        driver.execute_script("window.open('about:blank', '_blank');")  # Open another new tab
        driver.switch_to.window(driver.window_handles[2])  # Switch to the new tab
        driver.get(url3)

        driver.execute_script("window.open('about:blank', '_blank');")  # Open yet another new tab
        driver.switch_to.window(driver.window_handles[3])  # Switch to the new tab
        driver.get(url4)
        time.sleep(3600)
    # Close the original tab (optional)



