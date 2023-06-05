import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QLabel, QVBoxLayout, QHBoxLayout, QWidget, QPushButton, QTextEdit, QTabWidget, QScrollArea, QDialog, QMessageBox
from PyQt5.QtGui import QFont, QPalette, QColor, QTextOption, QIcon
from PyQt5.QtCore import Qt
import subprocess
import threading
import socket

class UPMWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("UPM")
        self.setGeometry(25, 50, 800, 600)
        self.setWindowIcon(QIcon("Logo.png"))
        self.setup_ui()

    def setup_ui(self):
        self.appbar_label = QLabel(">>> Unified Package Manager <<<", self)
        self.appbar_label.setGeometry(20, 20, 200, 30)
        self.appbar_label.setFont(QFont("BlockHead", 19, QFont.Bold))
        self.appbar_label.setAlignment(Qt.AlignCenter)

        self.left_menu = QTabWidget(self)
        self.left_menu.setGeometry(20, 20, 750, 550)

        self.install_page = QWidget()
        self.update_page = QWidget()
        self.installed_packages_page = QWidget()
        self.help_page = QWidget()

        self.left_menu.addTab(self.install_page, "New Installation")
        self.left_menu.addTab(self.update_page, "Update Manager")
        self.left_menu.addTab(self.installed_packages_page, "Installed Packages")
        self.left_menu.addTab(self.help_page, "Help")

        self.setup_install_page()
        self.setup_update_page()
        self.setup_installed_packages_page()
        self.setup_help_page()
        
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.appbar_label)
        main_layout.addWidget(self.left_menu)

        central_widget = QWidget()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

    def setup_install_page(self):
        layout = QVBoxLayout()
        welcome_layout = QVBoxLayout()
        pname_layout = QVBoxLayout()
        
        
        layout.setSpacing(2)
        
        user_name = subprocess.check_output("whoami").decode()
        self.emoji_label = QLabel("☺️")
        self.emoji_label.setFont(QFont("BlockHead",28))
        self.emoji_label.setFixedHeight(50)
        self.emoji_label.setStyleSheet("color: Red")
        self.emoji_label.setAlignment(Qt.AlignCenter)
        
        
        self.welcome = QLabel(f"Hello,{user_name}")
        self.welcome.setFont(QFont("BlockHead", 19, QFont.Bold))
        self.welcome.setStyleSheet("color: Indigo")
        self.welcome.setFixedHeight(30)
        self.welcome.setAlignment(Qt.AlignCenter)
        
        self.desc = QLabel("UPM : Seamlessly manage packages across Linux distributions such as \nDebian, Fedora and Arch Linux with the Unified Package Manager, \nsimplifying software installation, updates, and maintenance for a \nstreamlined user experience.")
        self.desc.setFont(QFont("BlockHead", 12))
        self.desc.setFixedHeight(75)
        self.desc.setAlignment(Qt.AlignCenter)
        
        welcome_layout.addWidget(self.welcome)
        welcome_layout.addWidget(self.emoji_label)
        welcome_layout.addWidget(self.desc)
        layout.addLayout(welcome_layout)
        
        #layout.addStretch(2)
        
        self.package_name_input = QLineEdit(self.install_page)
        self.package_name_input.setFixedHeight(30)
        self.package_name_input.setAlignment(Qt.AlignCenter)
        self.package_name_input.setPlaceholderText("Enter Package Name ...")
        
        style_sheet = """
            QLineEdit {
                color: black;
                border: 1.5px solid gray; 
                border-radius: 5px;
            }
            QLineEdit::focus {
                border: 2px solid black;
            }
            QLineEdit::placeholder {
                color: gray;
                text-align: center;
            }
        """
        
        self.package_name_input.setStyleSheet(style_sheet)
        
        pname_layout.addWidget(self.package_name_input)
        layout.addLayout(pname_layout)

        buttons_layout = QHBoxLayout()  # Create a QHBoxLayout for the buttons
        buttons_layout.setSpacing(10)  # Set the spacing between buttons
    
        install_button = QPushButton("Install", self.install_page)
        install_button.setStyleSheet("background-color: green; color: white;")
        install_button.setFont(QFont("BlockHead", 14, QFont.Bold))
        install_button.clicked.connect(self.install_package)
        buttons_layout.addWidget(install_button)

        update_button = QPushButton("Update", self.install_page)
        update_button.setStyleSheet("background-color: orange; color: white;")
        update_button.setFont(QFont("BlockHead", 14, QFont.Bold))
        update_button.clicked.connect(self.update_package2)
        buttons_layout.addWidget(update_button)

        remove_button = QPushButton("Remove", self.install_page)
        remove_button.setStyleSheet("background-color: red; color: white;")
        remove_button.setFont(QFont("BlockHead", 14, QFont.Bold))
        remove_button.clicked.connect(self.remove_package)
        buttons_layout.addWidget(remove_button)

        layout.addLayout(buttons_layout)

        self.install_page.setLayout(layout)
        

    def setup_update_page(self):
        layout = QVBoxLayout()
        
        package_label = QLabel("Available Updates :", self.update_page)
        package_label.setAlignment(Qt.AlignLeft)
        package_label.setFont(QFont("BlockHead", 14))
        
        layout.addWidget(package_label)
        
        scroll_area = QScrollArea(self.update_page)  # Create a QScrollArea widget
        container = QWidget()
        scroll_layout = QVBoxLayout(container)  # Set the layout on the container widget
        scroll_layout.setSpacing(13)
        
        # Replace the following lines with actual logic to retrieve upgradable packages
        #upgradable_packages = []
        
        upgradable_packages = self.get_installed_packages()
        
        for package in upgradable_packages:
            package_label = QLabel(f"{package['name']}", container)  # Use the container widget as the parent
            scroll_layout.addWidget(package_label)
            
            update_button = QPushButton("Update", self.update_page)
            update_button.setFont(QFont("BlockHead", 11))
            update_button.clicked.connect(lambda _, pkg=package['name'], btn=update_button: self.update_package(pkg, btn))
            
            scroll_layout.addWidget(update_button)
        
        scroll_area.setWidget(container)  # Set the container widget as the central widget of the scroll area
        scroll_area.setWidgetResizable(True)  # Make the scroll area's content resizable
        #layout = QVBoxLayout(self.update_page)  # Set a layout on the installed_packages_page
        layout.addWidget(scroll_area)  # Add the scroll area to the layout

        #self.installed_packages_page.setLayout(layout)

        #for package in upgradable_packages:
        #    package_label = QLabel(f"{package['name']} ({package['version']})", self.update_page)
        #    layout.addWidget(package_label)

        #    update_button = QPushButton("Update", self.update_page)
        #    update_button.clicked.connect(lambda _, pkg=package['name']: self.update_package(pkg))
        #    layout.addWidget(update_button)
            

        self.update_page.setLayout(layout)

    def setup_installed_packages_page(self):
        scroll_area = QScrollArea(self.installed_packages_page)  # Create a QScrollArea widget
        container = QWidget()  # Create a container widget
        layout = QVBoxLayout(container)  # Set the layout on the container widget

        installed_packages = self.get_installed_packages()

        for package in installed_packages:
            package_label = QLabel(f"{package['name']} ({package['version']})", container)  # Use the container widget as the parent
            layout.addWidget(package_label)

        scroll_area.setWidget(container)  # Set the container widget as the central widget of the scroll area
        scroll_area.setWidgetResizable(True)  # Make the scroll area's content resizable
        layout = QVBoxLayout(self.installed_packages_page)  # Set a layout on the installed_packages_page
        layout.addWidget(scroll_area)  # Add the scroll area to the layout

        self.installed_packages_page.setLayout(layout)  # Set the layout on the installed_packages_page
        
        #container = QWidget(self.installed_packages_page)
        #layout = QVBoxLayout(container)

        #installed_packages = self.get_installed_packages()

        #for package in installed_packages:
        #    print(package)
        #    package_label = QLabel(f"{package['name']} ({package['version']})", self.installed_packages_page)
        #    layout.addWidget(package_label)
            
        #self.installed_packages_page.setWidget(container)
        #self.installed_packages_page.setLayout(layout)


    def setup_help_page(self):
        layout = QVBoxLayout()

        help_text = subprocess.check_output(["upm", "-help"]).decode()
        help_label = QLabel(help_text, self.help_page)
        layout.addWidget(help_label)

        self.help_page.setLayout(layout)

    def get_installed_packages(self):
        output = subprocess.check_output(["upm", "-listall"]).decode()
        lines = output.split("\n")
        packages = []
        for line in lines:
            parts = line.split("\t")
            if len(parts) == 2:
                package = {"name": parts[0], "version": parts[1]}
                packages.append(package)
        return packages

    def check_internet_connection(self):
        try:
        # Attempt to establish a connection with a reliable internet host
            socket.create_connection(("8.8.8.8", 53), timeout=2)
            return True  # Connection successful, internet is available
        except socket.error:
            return False

    def create_output_window(self, output):
        print("Entered function\n")
        app = QApplication.instance()  # Get the existing QApplication instance
        if app is None:  # If no instance exists, create a new one
            app = QApplication([])

        window = QDialog()
        window.setWindowTitle("Output")
        layout = QVBoxLayout(window)
        text_edit = QTextEdit()
        text_edit.setReadOnly(True)
        text_edit.setPlainText(output)
        layout.addWidget(text_edit)
        window.exec_()  # Run the event loop for the output window

        if app is not None and app.isRunning():
            app.exit()

    def display_output(self, output):
        self.output_text_edit.append(output)

    def no_package(self):
        QMessageBox.warning(self, "Error", "Please enter a package name", QMessageBox.Ok)
        return

    def install_package(self):
        package_name = self.package_name_input.text()
        if package_name == "":
            self.no_package()
        else:
            self.package_name_input.setText("")
            self.package_name_input.setAlignment(Qt.AlignCenter)
            command = ["upm", "-install", package_name]
            self.execute_command(command, package_name)
        
    def remove_package(self):
        package_name = self.package_name_input.text()
        if package_name == "":
            self.no_package()
        else:
            self.package_name_input.setText("")
            self.package_name_input.setAlignment(Qt.AlignCenter)
            command = ["upm", "-remove", package_name]
            self.execute_remove_command(command, package_name)

    def update_package2(self):
        package_name = self.package_name_input.text()
        if package_name == "":
            self.no_package()
        else:
            self.package_name_input.setText("")
            self.package_name_input.setAlignment(Qt.AlignCenter)
            command = ["upm", "-update", package_name]
            self.execute_update_command2(command, package_name)

    def update_package(self, package_name, update_button):
        command = ["upm", "-update", package_name]
        self.execute_update_command(command, package_name)
        
        if self.check_internet_connection():
            update_button.setText("Updated")
            update_button.setStyleSheet("background-color: green; color: white;")
            update_button.setFont(QFont("BlockHead", 12, QFont.Bold))
            update_button.setEnabled(False)
            

    def execute_command(self, command, package_name):
        try:
            output = subprocess.check_output(package_name).decode()
            QMessageBox.warning(self, "Error", f"The Package {package_name} is already installed", QMessageBox.Ok)
                
        except FileNotFoundError:
            if self.check_internet_connection():
                print("Internet is available.")
                try:
                    output = subprocess.check_output(command).decode()
                    #self.create_output_window(output)
                    QMessageBox.information(self, "Success", "Package installed successfully.", QMessageBox.Ok)                    
                except subprocess.CalledProcessError as e:
                    error_message = e.output.decode()
                    QMessageBox.warning(self, "Error", "Package installation failed", QMessageBox.Ok)
                    #self.show_warning(error_message)
                    return
            else:
                print("No internet connection.")
                QMessageBox.warning(self, "Error", "No Internet Connection", QMessageBox.Ok)
                return
            
    def execute_update_command(self, command, package_name):
        if self.check_internet_connection():
            print("Internet is available.")
            try:
                output = subprocess.check_output(command).decode()
                #self.create_output_window(output)
                #QMessageBox.information(self, "Success", "Package installed successfully.", QMessageBox.Ok)                    
            except subprocess.CalledProcessError as e:
                error_message = e.output.decode()
                QMessageBox.warning(self, "Error", "Package updation failed", QMessageBox.Ok)
                #self.show_warning(error_message)
                return
        else:
            print("No internet connection.")
            QMessageBox.warning(self, "Error", "No Internet Connection", QMessageBox.Ok)
            return
    
    def execute_update_command2(self, command, package_name):
        try:
            output = subprocess.check_output(package_name).decode()
            if "No such file or directory" in output:
                QMessageBox.warning(self, "Error", "No Package Found with the name {package_name}", QMessageBox.Ok)
            
            else:
                if self.check_internet_connection():
                    print("Internet is available.")
                    try:
                        output = subprocess.check_output(command).decode()
                        QMessageBox.information(self, "Success", "Package Updated successfully.", QMessageBox.Ok)
                    except subprocess.CalledProcessError as e:
                        error_message = e.output.decode()
                        self.show_warning(error_message)
                        return
                else:
                    print("No internet connection.")
                    QMessageBox.warning(self, "Error", "No Internet Connection", QMessageBox.Ok)
                    return
        
        except FileNotFoundError:
            QMessageBox.warning(self, "Error", f"No Package Found with the name {package_name}", QMessageBox.Ok)
            return
            
            
    
    def execute_remove_command(self, command, package_name):
        try:
            output = subprocess.check_output(package_name).decode()
            if "No such file or directory" in output:
                QMessageBox.warning(self, "Error", "No Package Found with the name {package_name}", QMessageBox.Ok)
            
            else:
                try:
                    process = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
                    output, error = process.communicate(input='y\n')  # Provide 'y\n' as input to answer the prompt
            
                    if error:
                        self.show_warning(error)
                    else:
                        #self.create_output_window(output)
                        QMessageBox.information(self, "Success", "Package removed successfully.", QMessageBox.Ok)
                except subprocess.CalledProcessError as e:
                    error_message = e.output.decode()
                    self.show_warning(error_message)
                    return
        except FileNotFoundError:
            QMessageBox.warning(self, "Error", f"No Package Found with the name {package_name}", QMessageBox.Ok)
            return
            
                
    def show_warning(self, message):
        QMessageBox.warning(self, "Error", message, QMessageBox.Ok)
        # Show a warning dialog box with the provided message
        pass
        


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = UPMWindow()
    window.show()
    sys.exit(app.exec_())
