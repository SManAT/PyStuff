def open_dir_dialog(self):
    """open aa dialog to choose a directory"""
    dir_name = QFileDialog.getExistingDirectory(self, "Select a Directory")
    if dir_name:
        path = Path(dir_name)
        self.dir_name_edit.setText(str(path))
