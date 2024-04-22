import argparse
import shelve
import pathlib
import hashlib
import json
from collections import defaultdict

def walk(path):
    ''' This function is designed to retrieve a list of files within a specified directory path '''
    for child in path.glob('*'):
        if child.is_dir():
            yield from walk(child)
        else:
            yield str(child)

def get_file_list(path):
    ''' It utilizes walk() function to traverse the directory structure and collect the file paths into a list'''
    return [i for i in walk(pathlib.Path(path))]

def get_hash(file_path):
    ''' Generates a hash value for a file using the SHA-256 algorithm '''
    with open(file_path, "rb") as f:
        file_hash = hashlib.sha256(f.read()).hexdigest()
    return file_hash

def get_file_attributes(path):
    ''' Retrieves file attributes such as file paths and their corresponding hashes within a specified directory '''
    return {file: (pathlib.Path(file), get_hash(file)) for file in get_file_list(path)}

def bitwise_file_compare(file1, file2):
    ''' The function compares the binary content of two files to determine if they are identical '''
    with open(file1, "rb") as f1, open(file2, "rb") as f2:
        return f1.read() == f2.read()

def write_json(path_json, data):
    ''' Writes JSON data to a file '''
    with open(path_json, 'w') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

def read_json(path_json):
    ''' Reads a JSON file and returns its contents as a dictionary '''
    with open(path_json, 'r') as file:
        data = json.load(file)
    return dict(data)


class Statistics:
    def __init__(self):
        setattr(self,
                f"{self.__class__.__name__.lower()}",
                defaultdict(lambda: None))

    def write_statistics_to_json(self, path):
        write_json(path, {'count': self.statistics['count'],
                          'recognize': self.statistics['recognize'],
                          'bin_double': self.statistics['bin_double'],
                          'name_doubles': self.statistics['name_doubles'],
                          'rec_quality': self.statistics['rec_quality'],
                          'add_today': self.statistics['add_today'],
                          'no_named': self.statistics['no_named']})


def test():
   
    path_before = './test/before'
    path_after = './test/after'

    path_json = './test/stat.json'

    # Open stat.json
    stat = Statistics()
    if pathlib.Path(path_json).is_file(): stat.statistics.update(read_json(path_json))
 
    # Update images attributes
    if not pathlib.Path('./test/before.db').is_file():
        with shelve.open('./test/before') as db_before:
            db_before.update(get_file_attributes(path_before))

    # Open new images
    db_after = get_file_attributes(path_after)

    # Open images from db
    with shelve.open('./test/before') as db_before:
        
        # Counting stats:

        # Count
        stat.statistics['count'] = len(db_before) + len(db_after)

        # Recognised images
        stat.statistics['recognize'] = len(db_before)

        # Duplicates
        unique_hashes_db_before = set(i[1] for i in db_before.values())
        unique_hashes_db_after = set(i[1] for i in db_after.values())
        
        stat.statistics['bin_double'] = len(unique_hashes_db_before & unique_hashes_db_after)

        # etc.

    # Write statistcs to stat.json
    stat.write_statistics_to_json(path_json)

    
def main():
    pass


if __name__ == '__main__':

    parser = argparse.ArgumentParser(usage=__doc__)
    parser.add_argument('-t', '--test', dest='test',
                        action='store_true',
                        default=False,
                        help='Test mode')
    args = parser.parse_args()
    
    if args.test:
        test()
    else:
        main()