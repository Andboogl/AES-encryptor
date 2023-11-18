"""Module for showing QMessageBox"""


from PyQt6.QtWidgets import QMessageBox


def show_message(window, message):
    """Show QMessageBox"""
    message_box = QMessageBox(window)
    message_box.setText(message)
    message_box.exec()
