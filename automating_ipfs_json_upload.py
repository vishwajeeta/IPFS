import json
import os
import subprocess

# Load the JSON file
json_file = "samplejson.json"  # Change to your actual file name
with open(json_file, "r", encoding="utf-8") as f:
    data = json.load(f)

# Create a folder for storing JSON files
output_folder = "split_json_files"
os.makedirs(output_folder, exist_ok=True)

# Store CIDs
cids = {}

for index, entry in enumerate(data):
    try:
        # Extract 'Sample ID' for the filename
        sample_id = entry.get("Sample ID", f"Sample_{index}")  # Fallback if missing
        
        # Create filename based on Sample ID
        file_name = f"{sample_id}.json"
        file_path = os.path.join(output_folder, file_name)
        
        # Save entry as a separate JSON file
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(entry, f, indent=2)
        
        # Upload file to local IPFS and get CID
        result = subprocess.run(["ipfs", "add", "-Q", file_path], capture_output=True, text=True)
        cid = result.stdout.strip()
        
        # Pin the file to prevent garbage collection
        subprocess.run(["ipfs", "pin", "add", cid])
        # Add to IPFS Desktop "Files" tab (MFS)
        subprocess.run(["ipfs", "files", "cp", f"/ipfs/{cid}", f"/{file_name}"])
        
        # Store CID
        cids[file_name] = cid
        
        print(f"Uploaded {file_name} -> CID: {cid}")

    except Exception as e:
        print(f"Error processing entry {index}: {e}")

# Save all CIDs to a JSON file
with open("uploaded_cids.json", "w", encoding="utf-8") as cid_file:
    json.dump(cids, cid_file, indent=2)

print("\n All files uploaded and CIDs saved in uploaded_cids.json")
