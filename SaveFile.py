class SaveToFile:

    def __init__(self, file_name):
        """Creates txt file with file_name"""
        self.file_name = file_name
        self.save_file = open(file_name, "a+")

    def add_line(self, message):
        """Adds new line with content of message on a txt file."""
        with open(self.file_name,"a+") as f:
            f.write("%s\n" % message)

    def close_file(self):
        """Closes open file."""
        self.save_file.close()