# 🌎 World Bank Data Scraper
![World Bank Scraper](https://img.shields.io/badge/Python-Data%20Scraper-blue)

A Python scraper that fetches comprehensive country data from the World Bank API, including details like capital cities, regions, and income levels. Built with error handling, logging, and progress tracking for reliable data collection.

## ✨ Features

- Fetches detailed country information from World Bank's API
- Handles errors gracefully with comprehensive logging
- Shows real-time progress with tqdm progress bars
- Saves data in a clean CSV format
- Tracks and reports countries with missing data
- Type-hinted for better code maintainability

## 🚀 Quick Start

### Prerequisites

```bash
pip install requests pandas beautifulsoup4 tqdm
```

### Required Files

1. `country_iso_codes.csv` - A file containing country ISO codes to scrape
2. The script will generate `WorldBank_data.csv` with the scraped data

### Usage

1. **Prepare the Input File:** Ensure `country_iso_codes.csv` exists with country ISO codes in the first column.
2. **Run the Script:**
   ```sh
   python worldbank_scraper.py
   ```
3. **View the Output:** The extracted data will be saved in `WorldBank_data.csv`.

## 📊 Output Data Format

The scraper collects the following information for each country:
- Country ISO Code
- Country Name
- Capital City
- Region
- Income Level

## 📊 Sample Output
| CountryIsoCode | CountryName | Capital       | Region         | IncomeLevel        |
|--------------|------------|--------------|--------------|----------------|
| USA          | United States | Washington D.C. | North America | High income |
| IND          | India        | New Delhi       | South Asia    | Lower middle income |

## 🛠️ Technical Details

- Uses BeautifulSoup4 for XML parsing
- Implements concurrent request handling
- Includes comprehensive error handling and logging
- Progress tracking with tqdm
- Type hints for better code maintainability
- Configurable logging levels

## 📝 Logging

The scraper includes detailed logging:
- Information about the scraping progress
- Warnings for countries with missing data
- Error messages for failed requests
- Success messages for data saving

## ⚠️ Error Handling

The scraper handles various scenarios:
- Missing country data
- API request failures
- File I/O errors
- Parsing errors

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

## 📜 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- World Bank for providing the public API
- All contributors and users of this project

