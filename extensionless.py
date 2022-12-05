import os
import click
import json


@click.command()
# list of possible options
@click.option('--directory', prompt='Enter a path for investigation',
              help='A whole path')
@click.option('--statistics', prompt='Enter 1 if you need statistics of directory content, 0 if you do not',
              help='Enter 1 or 0')


def investigate(directory, statistics):
    """Program that investigates the directory for files without any extension."""
    # Gets information from JSON file
    abspath = os.path.abspath(os.path.dirname(__file__))
    data = json.loads(open(os.path.join(abspath, "data.json"), "r", encoding="utf-8").read())

    # Params used in statistics:
    stat = {}
    count_changes = 0
    count_directories = 0
    count_not_found_type = 0

    # Examine each object in directory
    "needs exception if given path is not a directory"
    for file in os.listdir(directory):

        # Checks for any visible extension
        flag_file_needs_investigation = True
        visible_extension = os.path.splitext(file)
        if len(visible_extension) > 1:
            visible_extension_without_dot = visible_extension[-1].lstrip('.')
            for element in data:
                extension_vis = element["extension"]
                if extension_vis == visible_extension_without_dot:
                    stat[extension_vis] = stat.get(extension_vis, 0) + 1
                    flag_file_needs_investigation = False

        # If there is no visible extension investigation is needed
        if flag_file_needs_investigation:
            f = os.path.join(directory, file)

            # Checks if it is file or directory
            if os.path.isfile(f):

                # Get file signature
                var = open(f, "rb").read(32)
                hex_bytes = " ".join(['{:02X}'.format(byte) for byte in var])

                possible_extensions = []
                # Examines signature
                for element in data:
                    for signature in element["signature"]:
                        offset = element["offset"] * 2 + element["offset"]
                        if signature == hex_bytes[offset:len(signature) + offset].upper():
                            possible_extensions.append(element["extension"])

                # Check if there is more than one possible extension
                if possible_extensions:
                    extension = possible_extensions[0]
                    if len(possible_extensions) > 1:
                        print("Here is more than one possible extension for file: " + visible_extension[0])
                        for i in possible_extensions:
                            print("Number " + str(i + 1) + ": " + possible_extensions[i])
                            num = int(input("Enter the most possible extension number:"))
                            if num > len(possible_extensions) or num <= 0:
                                print("Extension would be chosen automatically")
                                extension = possible_extensions[0]
                            else:
                                extension = possible_extensions[num - 1]

                    # Make changes to file name
                    os.rename(f, str(f) + '.' + extension)

                    # Statistics if user needed
                    if statistics:
                        stat[extension] = stat.get(extension, 0) + 1
                        count_changes += 1
                else:
                    count_not_found_type += 1
            # In case it is not a file
            else:
                count_directories += 1

    # Output
    if statistics:
        for key, value in stat.items():
            print(key, ' : ', value)
        print("Directories: " + str(count_directories))
        print("Not found type: " + str(count_not_found_type))
        print("Changed: " + str(count_changes))


if __name__ == '__main__':
    investigate()
