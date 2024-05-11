import requests
import json
import os
import time
from urllib.parse import urlencode, urlunparse

# env API key
api_key = os.getenv('ETHERSCAN_API_KEY')

# directory for output
directory = 'data'

# Check if the directory exists and create it if necessary
if not os.path.exists(directory):
    os.makedirs(directory)

def fetch_tx(start_block, end_block, chunk_size):
    # Initialize timer
    start = time.time()
    
    for chunk_start in range(start_block, end_block + 1, chunk_size):
        transactions = []
        chunk_end = min(chunk_start + chunk_size - 1, end_block)
        
        for block in range(chunk_start, chunk_end + 1):
            query_params = {
                'module': 'proxy',
                'action': 'eth_getBlockByNumber',
                'tag': hex(block),
                'boolean': 'true',
                'apikey': api_key
            }
            url_parts = ('https', 'api.etherscan.io', '/api', '', urlencode(query_params), '')
            url = urlunparse(url_parts)
            try:
                response = requests.get(url)
                response.raise_for_status()
                block_data = response.json()
                if 'result' in block_data and isinstance(block_data['result'], dict):
                    transactions.extend(block_data['result'].get('transactions', []))
            except requests.RequestException as e:
                print(f"Request error: {e}")
            except json.JSONDecodeError:
                print("Failed to decode JSON from response.")
            
        filename = f'{directory}/blk_{chunk_start}_{chunk_end}.json'  # Adjust the file path
        # Write the transactions to a file with pretty printing
        with open(filename, 'w') as file:
            json.dump(transactions, file, indent=4)
        
        print(f"Data has been written to {filename}")
        
    # Some stats after all chunks are processed
    end = time.time()
    total_time = end - start
    average_time = total_time / (end_block - start_block + 1)
    
    print(f"Total time taken: {total_time:.2f} seconds")
    print(f"Average time per block: {average_time:.2f} seconds")


# params
start_block = 19800000  # integer block number
end_block =   19800004    # integer block number
chunk_size = 5

# Fetch transactions
fetch_tx(start_block, end_block, chunk_size)