import os
import shutil
import sys
import argparse
import time

def synchronize_folders(source_folder, replica_folder, log_file, interval):
    # Create replica folder if it doesn't exist
    if not os.path.exists(replica_folder):
        os.makedirs(replica_folder)

    try:
        while True:
            # Get list of files in source folder
            source_files = os.listdir(source_folder)

            # Get list of files in replica folder
            replica_files = os.listdir(replica_folder)

            # Synchronize files from source to replica
            for file_name in source_files:
                source_path = os.path.join(source_folder, file_name)
                replica_path = os.path.join(replica_folder, file_name)

                # Check if file exists in replica
                if file_name in replica_files:
                    # Compare timestamps
                    source_time = os.path.getmtime(source_path)
                    replica_time = os.path.getmtime(replica_path)

                    # If source file is newer, copy it to replica
                    if source_time > replica_time:
                        if os.path.isdir(source_path):
                            shutil.rmtree(replica_path)
                            shutil.copytree(source_path, replica_path)
                        else:
                            shutil.copy2(source_path, replica_path)
                        log_message = f"File '{file_name}' copied from source to replica"
                        print(log_message)
                        log_file.write(log_message + '\n')
                    

                # If file does not exist in replica, copy it from source
                else:
                    if os.path.isdir(source_path):
                        shutil.copytree(source_path, replica_path)
                    else:
                        shutil.copy2(source_path, replica_path)
                    log_message = f"File '{file_name}' copied from source to replica"
                    print(log_message)
                    log_file.write(log_message + '\n')

            # Synchronize files from replica to source
            for file_name in replica_files:
                source_path = os.path.join(source_folder, file_name)
                replica_path = os.path.join(replica_folder, file_name)

                # Check if file exists in source
                if file_name in source_files:
                    # Compare timestamps
                    source_time = os.path.getmtime(source_path)
                    replica_time = os.path.getmtime(replica_path)
                    # If replica file is newer, copy it to source
                    if source_time < replica_time:
                        if os.path.isdir(replica_path):
                            shutil.rmtree(source_path)
                            shutil.copytree(replica_path, source_path)
                        else:
                            shutil.copy2(replica_path, source_path)
                        log_message = f"File '{file_name}' copied from replica to source"
                        print(log_message)
                        log_file.write(log_message + '\n')

            # Wait for synchronization interval
            time.sleep(interval)
    except KeyboardInterrupt:
        print("\nSynchronization stopped.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Synchronize two folders.")
    parser.add_argument("source_folder", help="Path to the source folder")
    parser.add_argument("replica_folder", help="Path to the replica folder")
    parser.add_argument("log_file", help="Path to the log file")
    parser.add_argument("interval", type=int, help="Synchronization interval in seconds")
    args = parser.parse_args()

    with open(args.log_file, 'a') as log_file:
        synchronize_folders(args.source_folder, args.replica_folder, log_file, args.interval)
