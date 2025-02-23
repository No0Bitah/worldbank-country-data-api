import requests
import pandas as pd
from bs4 import BeautifulSoup
from tqdm import tqdm
import warnings
from requests.exceptions import RequestException
from typing import List

import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

warnings.filterwarnings('ignore')

class WorldBankScraper:
    DATA_FILE: str = 'WorldBank_data.csv'  # File to store the extracted data
    COUNTRY_CODES_FILE: str = 'country_iso_codes.csv'  # File containing country codes
    BASE_URL: str = "http://api.worldbank.org/v2/countries/{}"  # API endpoint for fetching country data
    
    def __init__(self) -> None:
        self.data: List[List[str]] = []  # List to store successfully fetched country data
        self.no_data: List[str] = []  # List to store country codes with no available data
    
    def get_country_data(self, url: str) -> None:
        """Fetches country data from the World Bank API and appends it to the data list."""
        try:
            response: requests.Response = requests.get(url)
            response.raise_for_status()
            
            soup: BeautifulSoup = BeautifulSoup(response.content, "xml")
            country_element = soup.find('wb:country')  # Extract country element
            
            if not country_element:
                self.no_data.append(url)  # Store URLs with missing data
                return
            
            # Append extracted country details to data list
            self.data.append([
                country_element["id"],  # Country ISO code
                soup.find('wb:name').get_text(),  # Country name
                soup.find('wb:capitalCity').get_text(),  # Capital city
                soup.find('wb:region').get_text(),  # Region
                soup.find('wb:incomeLevel').get_text()  # Income level
            ])
        
        except RequestException as e:
            logging.error(f"Request error for {url}: {str(e)}")
            return None
        except Exception as e:
            logging.error(f"Unexpected error for {url}: {str(e)}")
            return None
    
    def save_data_to_csv(self) -> None:
        """Saves the collected data to a CSV file."""
        try:
            df: pd.DataFrame = pd.DataFrame(self.data, columns=['CountryIsoCode', 'CountryName', 'Capital', 'Region', 'IncomeLevel'])
            
            with tqdm(total=1, desc="Saving data to CSV") as pbar:
                    df.to_csv(self.DATA_FILE, index=False)
                    pbar.update(1)
            df.to_csv(self.DATA_FILE, index=False)
            logging.info(f"Data successfully saved to {self.DATA_FILE}")

        except Exception as e:
            logging.error(f"Error saving data to CSV: {str(e)}")   
      
    
    def run(self) -> None:
        """Executes the scraper, handling errors gracefully."""
        try:
            df: pd.DataFrame = pd.read_csv(self.COUNTRY_CODES_FILE).drop_duplicates()  # Load and remove duplicate country codes
        except FileNotFoundError:
            logging.error(f"Error: {self.COUNTRY_CODES_FILE} not found.")
            return
        except Exception as e:
            logging.error(f"Unexpected error reading {self.COUNTRY_CODES_FILE}: {str(e)}")
            return
        
        try:
            with tqdm(total=len(df), desc="Getting data from World Bank API") as pbar:
                for country_code in df.iloc[:, 0]:  # Assuming country code is in the first column
                    self.get_country_data(self.BASE_URL.format(str(country_code)))
                    pbar.update(1)  # Update progress bar
            
            self.save_data_to_csv()  # Save extracted data to CSV
        except Exception as e:
            logging.error(f"Unexpected error during execution: {str(e)}")
        
        if self.no_data:
            logging.warning("***** No Data Found for These Countries: *****")
            logging.warning("\n".join(self.no_data))  # Print countries with missing data

if __name__ == '__main__':
    scraper: WorldBankScraper = WorldBankScraper()
    scraper.run()
