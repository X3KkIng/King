import os

def find_databases(directory):
    """
    Find all database files in the given directory.

    :param directory: The directory to search for database files in.
    :return: A list of full paths to the database files.
    """

    # Find all files in the directory that have the ".db" file extension.
    database_files = [os.path.join(directory, file) for file in os.listdir(directory) if file.endswith(".db")]

    return database_files

# Test the script.
directory = "/path/to/database/directory"
print(find_databases(directory))