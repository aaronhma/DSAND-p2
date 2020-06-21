import os as file
import print_better as show
show.__init__()


def find_files(suffix, path, dev_mode=False):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    total_files = []  # Returned list with path

    try:
        for files in file.listdir(path):  # Iterate on the path inputed
            slash_in_file = path.find("/")  # Check if / in file path
            if slash_in_file != -1:  # Slash is in path
                file_path = path + suffix  # Don't add /
            else:  # Slash is not in path
                file_path = path + "/" + suffix  # Add /
            check_real_path = file.path.isfile(
                file_path)  # Check that the file exists
            if check_real_path:  # The file exists. Yay!
                # Check that file matches the suffix.
                check_file_suffix = file_path.endswith(suffix)
                if check_file_suffix:  # The file matches the suffix! Finally!
                    total_files.append(file_path)
                else:  # File doesn't match suffix.
                    show.WARNING("[WARN] Found the file at {}, but it doesn't end with the suffix {}!".format(
                        file_path, suffix))  # File doesn't end with the suffix :(
                    # Continue the search
                    show.INFO("[INFO] Continuing search!")

                    # APPLY RECURSION :D
                    total_files.extend(find_files(suffix, file_path))
                    # APPLY RECURSION :D

            else:  # The file doesn't exist. :(
                show.FATAL("The file at {} doesn't exist!".format(file_path))

    except FileNotFoundError:
        if dev_mode:
            raise FileNotFoundError("[FATAL] THE FILE WAS NOT FOUND!")
        else:
            show.FATAL("The file was not found!")

    return total_files  # Return the list total_files


# STUDENT TESTS
if __name__ == "__main__":
    show.INFO("Running student tests.")
    # Test 1
    find_files("LRU_Cache.py", ".")
    # Test 1
    show.INFO("Test 1 should have no errors.")

    # Test 2
    find_files("Huffman_CODING.py", "./d/")
    # Test 2

    show.INFO("Test 2 should have an error.")

    # Test 3
    find_files(".gitignores", ".")
    # Test 3
    show.INFO("Test 3 should have no errors.")

    show.SUCCESS("Passed student tests.")
# STUDENT TESTS
