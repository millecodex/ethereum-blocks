# Ethereum Block Downloader
This project is designed to download Ethereum block data using the Etherscan API. It chunks the data for efficient processing and stores it locally. This allows for analysis and usage of historical block data for Ethereum.

## Getting Started
To get this project running on your local machine for development and testing purposes, follow these instructions.

### Prerequisites
- Python 3.x
- Requests library (`pip install requests`)
- An API key from [Etherscan.io](https://etherscan.io/apis)

## Setup
To use the Etherscan API effectively, you will need an API key. Here's how you can store your API key securely using an environment variable:

### Setting up the API Key as an Environment Variable
1. **Obtain an API Key**:
   - Visit [Etherscan.io](https://etherscan.io/apis) and sign up for an API key if you haven't already.

2. **Set the Environment Variable**:
   - For **macOS/Linux**:
     - Open your terminal.
     - Run the following command to add the API key to your bash profile (replace `YourApiKeyHere` with your actual API key):
       ```bash
       echo 'export ETHERSCAN_API_KEY="YourApiKeyHere"' >> ~/.bash_profile
       ```
     - Reload the profile with:
       ```bash
       source ~/.bash_profile
       ```
   - For **Windows**:
     - Search for "Environment Variables" in your Windows search bar and select "Edit the system environment variables".
     - In the System Properties window, click on the "Environment Variables" button.
     - In the Environment Variables window, click "New" under the "System variables" section.
     - Set the variable name as `ETHERSCAN_API_KEY` and the value as your actual API key.
     - Click OK and close all windows.

3. **Accessing the API Key in Your Application**:
   - In your Python script, you can access the API key like this:
     ```python
     import os
     api_key = os.getenv('ETHERSCAN_API_KEY')
     if not api_key:
         raise ValueError("API Key is not set in environment variables")
     ```

This method ensures that your API key remains secure and is not hard-coded into your source code, which is especially important if you plan to share your code publicly on platforms like GitHub.

### To clone this Repo
Clone the repository and navigate into the project directory:

```bash
git clone https://github.com/millecodex/ethereum-blocks.git
cd ethereum-blocks
```

### Installation
Create a virtual environment and install the required packages:

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
pip install -r requirements.txt
```

### Configuration
Set up your Etherscan API key in your environment:

```bash
export ETHERSCAN_API_KEY='YourApiKeyHere'
```

### Usage
Run the script to start downloading blocks:

```bash
python fetch_tx.py
```

## How It Works
The script fetches Ethereum blocks in chunks and saves each chunk to a separate JSON file in the `data/` directory. This process optimizes data handling and minimizes memory usage. A 50 block chunk will be about 14 mb. 

### Performance
- **Blocks per Day**: Approximately 6,500 to 6,900 blocks are processed daily. If 50 blocks are 14 mb, a day's worth of blocks will be about 1.9 GB. (to be tested)
- **Download Time**: It takes about 1.5 seconds per block, which may vary based on network speed and API responsiveness. 
- **Rate Limitations**: This is longer than the rate limited frequency of 5 calls/second. This is because full block data is heavy. Linking transactions or calling per hash is much faster than may run into rate limits.

### Data Structure
A sample JSON structure of an Ethereum block:

```json
{
    "blockHash": "0x95d7f597b43f97bb4dcb0f1d9a74f13d6d6236592cd01d122945d04b5a2aabad",
    "blockNumber": "0x12e1fc0",
    "from": "0xae2fc483527b8ef99eb5d9b44875f005ba1fae13",
    "gas": "0x2765f",
    "gasPrice": "0x12a773871",
    "maxFeePerGas": "0x12a773871",
    "to": "0x88df592f8eb5d7bd38bfef7deb0fbc02cf3778a0",
    "transactionIndex": "0x2",
    "value": "0x7a69",
    "type": "0x0",
    "v": "0x25",
    "r": "0x1b4f",
    "s": "0x1b4e"
}
```

## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

