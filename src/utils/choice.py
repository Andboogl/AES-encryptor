"""Module for user selection of a file or folde"""


from PyQt6.QtWidgets import QFileDialog


def show_choice_file_window(window):
    """Show file selection window"""
    dialog = QFileDialog.getOpenFileName(window, 'Вибір файлу')
    file = dialog[0]
    return file


def show_choice_folder_window(window):
    """Show folder selection window"""
    folder = QFileDialog.getExistingDirectory(window, 'Вибір папки')
    return folder
