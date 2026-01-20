class FileManager():
  files = []

  def __init__(self):
    pass


  def TotalFiles(self):
    # ...
    # Here should be a query fetching the files from a folder.
    # A var is replacing it for exemple
    self.files = ["path/to/file1", "path/to/file2"]
    return len(self.files)

file_manager = FileManager()
print(file_manager.TotalFiles())
