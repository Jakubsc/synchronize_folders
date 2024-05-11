import os
import shutil
import sys
import argparse

def synchronize_folders(source_folder, replica_folder, log_file):
    # Create replica folder if it doesn't exist
    if not os.path.exists(replica_folder):
        os.makedirs(replica_folder)

    try:
        # Get list of files in source folder
        source_files = os.listdir(source_folder)

        # Get list of files in replica folder
        replica_files = os.listdir(replica_folder)

        # Synchronize files from source to replica
        for file_name in source_files:
            source_path = os.path.join(source_folder, file_name)
            replica_path = os.path.join(replica_folder, file_name)

            # If file exists in source but not in replica, copy it
            if file_name not in replica_files:
                if os.path.isdir(source_path):
                    shutil.copytree(source_path, replica_path)
                    log_message = f"Folder '{file_name}' copied from source to replica"
                else:
                    shutil.copy2(source_path, replica_path)
                    log_message = f"File '{file_name}' copied from source to replica"
                print(log_message)
                log_file.write(log_message + '\n')

        # Delete files in replica that don't exist in source
        for file_name in replica_files:
            replica_path = os.path.join(replica_folder, file_name)
            if file_name not in source_files:
                if os.path.isdir(replica_path):
                    shutil.rmtree(replica_path)
                    log_message = f"Folder '{file_name}' deleted from replica"
                else:
                    os.remove(replica_path)
                    log_message = f"File '{file_name}' deleted from replica"
                print(log_message)
                log_file.write(log_message + '\n')
    except KeyboardInterrupt:
        print("\nSynchronization stopped.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Synchronize two folders.")
    parser.add_argument("source_folder", help="Path to the source folder")
    parser.add_argument("replica_folder", help="Path to the replica folder")
    parser.add_argument("log_file", help="Path to the log file")
    args = parser.parse_args()

    with open(args.log_file, 'a') as log_file:
        synchronize_folders(args.source_folder, args.replica_folder, log_file)
