import base64
import os
import fnmatch
from pathlib import Path


class IMage2Base64Converter():
    """
    a class to batch convert Image Types unto Base64Encoded Images
    use e.g.
    <img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAUAAAAFCAYAAA==" alt="Red dot" />
    """
    def __init__(self):
        self.images = self.search_files('.', ['*.jpg', '*.jpeg', '*.png'])
        self.convert()

    def search_files(self, directory='.', pattern=''):
        """
        search for pattern in directory recursive
        :param directory: path where to search. relative or absolute
        :param pattern: a list e.g. ['*.jpg', '__.*']
        """
        data = []
        for dirpath, dirnames, files in os.walk(directory):
            for p in pattern:
                for f in fnmatch.filter(files, p):
                    data.append(os.path.join(dirpath, f))
        return data

    def getFilename(self, filename):
        """ get the filename only, without extension """
        return Path(filename).stem

    def convert(self):
        for img in self.images:
            print("Processing %s" % img)
            with open(img, "rb") as img_file:
                my_string = base64.b64encode(img_file.read())
                # write to file
                new_filename = "%s.base64" % self.getFilename(img)
                print("Saving to: %s" % new_filename)

                file = open(new_filename, 'w')
                file.write("%s" % my_string.decode("utf-8"))
                file.close()


if __name__ == "__main__":
    tool = IMage2Base64Converter()
    print("\nUse it in Html like\n<img src=\"data:image/png;base64,<base64data>\" />")
