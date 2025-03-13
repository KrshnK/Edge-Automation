import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize Edge WebDriver
driver = webdriver.Edge()  # Ensure Microsoft Edge WebDriver is in your PATH

def random_search():
    search_terms = [
      "Quantum Computing: Transforming Computational Paradigms", "Artificial Intelligence in Healthcare: Revolutionizing Diagnosis and Treatment", "Blockchain and Cryptocurrencies: Securing the Future of Transactions", "Cybersecurity Challenges in the Quantum Computing Era", "Augmented Reality in Education: The New Classroom Experience", "Sustainable Energy Solutions with Advanced Tech", "The Role of AI in Understanding Ancient Civilizations", "The History of the Internet: From ARPANET to 6G", "Space Exploration Technologies: The Next Frontier", "Genomics and AI: Precision in Disease Prevention", "Remote Collaboration Tools: Shaping the Future of Work", "Social Media Algorithms and Their Impact on Mental Health", "Renewable Energy Optimization Using Smart Grids", "AI-Driven Evolution of Music Genres", "Futuristic Cities: IoT and Urban Planning", "Ethical AI and Automation: Navigating the Moral Landscape", "Artificial Intelligence in Social Entrepreneurship", "Debunking Nutrition Myths Through AI Analysis", "Time Travel Simulations with Quantum Theories", "Machine Learning in Climate Change Prediction", "The Psychology of Colors in UI/UX Design", "Digital Art in the Age of AI: Creativity Redefined", "Neuroscience and Sleep Tech: Tracking the Science of Rest", "AI in Creative Writing: The Evolution of Storytelling", "Virtual Reality: The Future of Immersive Experiences", "Impact of Globalization on Tech Cultures", "The Science Behind Happiness: AI-Driven Behavioral Insights", "Evolving Educational Systems with Adaptive Learning Platforms", "Digital Privacy and AI in Personal Data Security", "The Future of Transportation: Hyperloop and Beyond", "Space Tourism: Technology Meets Adventure", "The Philosophy of Ethics in AI Development", "Generative AI in Music Creation: A New Era", "The Ethics of Genetic Engineering and CRISPR Tech", "AI in Music Therapy for Cognitive Development", "Empowering Women in Tech Through AI Innovations", "Smart Cities: A Tech-Driven Urban Development Model", "The Role of Storytelling in AI-Powered Marketing", "Social Influence Algorithms: The Psychology of Digital Persuasion", "Self-Driving Cars: The Next Phase of Mobility", "The Evolution of Language Models in Communication Tech"
    ]

    # Shuffle the list to ensure no repetition
    random.shuffle(search_terms)

    # Open Bing
    driver.get("https://www.bing.com")

    for term in search_terms:  # Iterate through each unique term
        try: 
            # Open a new tab
            driver.execute_script("window.open('https://www.bing.com', '_blank');")
            driver.switch_to.window(driver.window_handles[-1])

            # Wait for the search box to be visible and clickable
            search_box = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.NAME, "q"))
            )

            # Focus on the search box and type the search term
            search_box.clear()  # Clear any previous input if necessary
            search_box.send_keys(term)
            search_box.send_keys(Keys.RETURN)

            # Wait for a random delay before the next action
            time.sleep(random.uniform(2, 5))

            # Click a random link
            links = WebDriverWait(driver, 10).until(
                EC.presence_of_all_elements_located((By.XPATH, "//a[@href]"))
            )
            if links:
                random.choice(links).click()
                time.sleep(random.uniform(2, 5))  # Adjust as needed

                # Close the current tab after clicking
                driver.close()
                driver.switch_to.window(driver.window_handles[0])  # Switch back to the main tab

        except Exception as e:
            print(f"An error occurred while searching for '{term}': {e}")
            # Continue to the next term instead of breaking
            continue

try:
    random_search()  # Perform searches without topic repetition
except KeyboardInterrupt:
    print("Script stopped manually.")
finally:
    driver.quit()  # Close the browser when the script ends
