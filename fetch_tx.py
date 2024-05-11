import requests
import json
import os
import time

# env API key
api_key = os.getenv('ETHERSCAN_API_KEY')

def fetch_tx(api_key, start_block, end_block, chunk_size):
    # Initialize timer
    start = time.time()
    
    for chunk_start in range(start_block, end_block + 1, chunk_size):
        transactions = []
        chunk_end = min(chunk_start + chunk_size - 1, end_block)
        
        for block in range(chunk_start, chunk_end + 1):
            url = f"https://api.etherscan.io/api?module=proxy&action=eth_getBlockByNumber&tag={hex(block)}&boolean=true&apikey={api_key}"
            response = requests.get(url)
            
            if response.status_code == 200:
                block_data = response.json()
                if block_data['result']:  # Make sure the result key exists and has data
                    transactions.extend(block_data['result']['transactions'])
        
        # write out location
        directory = 'data' # make sure it exists
        filename = f'{directory}/tx_{chunk_start}_{chunk_end}.json'  # Adjust the file path
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
end_block =   19800010    # integer block number
chunk_size = 5

# Fetch transactions
fetch_tx(api_key, start_block, end_block, chunk_size)

