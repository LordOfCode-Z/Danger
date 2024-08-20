import tkinter as tk
from tkinter import ttk

class ControlApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Python Control App")
        self.root.geometry("1024x600")
        self.root.config(bg="#0a0f2c")  # Koyu mavi arka plan

        # Set up the main layout
        self.setup_menu()
        self.setup_tabs()

    def setup_menu(self):
        """Create the left-side menu."""
        menu_frame = tk.Frame(self.root, bg="#1a1f3c", width=200)
        menu_frame.pack(side="left", fill="y")

        buttons = [
            ("Home", self.home),
            ("Clients", self.open_clients),
            ("Tutorial", self.open_tutorial),
            ("Builder", self.build_project),
            ("Port Settings", self.open_port_settings),
            ("Settings", self.open_settings)
        ]
        
        for text, command in buttons:
            button = tk.Button(menu_frame, text=text, bg="#3a3f6c", fg="white", 
                               font=("Arial", 12), command=command)
            button.pack(fill="x", pady=5)

    def setup_tabs(self):
        """Set up the main control panel with tabs."""
        style = ttk.Style()
        style.configure('TNotebook.Tab', background="#3a3f6c", foreground="white", 
                        padding=[10, 5], font=("Arial", 10))
        style.configure('TFrame', background="#0a0f2c")

        tab_control = ttk.Notebook(self.root, style="TNotebook")
        
        # Create tabs
        self.device_tab = ttk.Frame(tab_control, style='TFrame')
        self.client_tab = ttk.Frame(tab_control, style='TFrame')
        self.settings_tab = ttk.Frame(tab_control, style='TFrame')
        
        # Add tabs to the tab control
        tab_control.add(self.device_tab, text='Device Control')
        tab_control.add(self.client_tab, text='Client Management')
        tab_control.add(self.settings_tab, text='Settings')
        
        tab_control.pack(expand=1, fill="both")
        
        # Add content to tabs
        self.setup_device_tab()
        self.setup_client_tab()
        self.setup_settings_tab()

    def setup_device_tab(self):
        """Device Control tab content."""
        tk.Label(self.device_tab, text="Device Control", font=("Arial", 16), 
                 bg="#0a0f2c", fg="white").pack(pady=10)
        
        control_frame = tk.Frame(self.device_tab, padx=10, pady=10, bg="#0a0f2c")
        control_frame.pack()

        # Example Device Control Buttons
        tk.Button(control_frame, text="Shutdown Device", command=self.shutdown_device, 
                  bg="#3a3f6c", fg="white", font=("Arial", 12")).pack(pady=5)
        tk.Button(control_frame, text="Fetch Device Info", command=self.fetch_device_info, 
                  bg="#3a3f6c", fg="white", font=("Arial", 12")).pack(pady=5)
        
    def setup_client_tab(self):
        """Client Management tab content."""
        tk.Label(self.client_tab, text="Client Management", font=("Arial", 16), 
                 bg="#0a0f2c", fg="white").pack(pady=10)
        
        client_frame = tk.Frame(self.client_tab, padx=10, pady=10, bg="#0a0f2c")
        client_frame.pack()

        # Example Client Management Buttons
        tk.Button(client_frame, text="Add Client", command=self.add_client, 
                  bg="#3a3f6c", fg="white", font=("Arial", 12")).pack(pady=5)
        tk.Button(client_frame, text="Remove Client", command=self.remove_client, 
                  bg="#3a3f6c", fg="white", font=("Arial", 12")).pack(pady=5)
        tk.Button(client_frame, text="List Clients", command=self.list_clients, 
                  bg="#3a3f6c", fg="white", font=("Arial", 12")).pack(pady=5)

    def setup_settings_tab(self):
        """Settings tab content."""
        tk.Label(self.settings_tab, text="Settings", font=("Arial", 16), 
                 bg="#0a0f2c", fg="white").pack(pady=10)
        
        settings_frame = tk.Frame(self.settings_tab, padx=10, pady=10, bg="#0a0f2c")
        settings_frame.pack()

        # Example Settings Control
        tk.Button(settings_frame, text="Save Settings", command=self.save_settings, 
                  bg="#3a3f6c", fg="white", font=("Arial", 12")).pack(pady=5)
        tk.Button(settings_frame, text="Load Settings", command=self.load_settings, 
                  bg="#3a3f6c", fg="white", font=("Arial", 12")).pack(pady=5)
    
    # Placeholder Methods
    def home(self):
        print("Home action")

    def open_clients(self):
        print("Open Clients action")

    def open_tutorial(self):
        print("Open Tutorial action")

    def build_project(self):
        print("Build Project action")

    def open_port_settings(self):
        print("Open Port Settings action")

    def open_settings(self):
        print("Open Settings action")

    def shutdown_device(self):
        print("Shutting down device...")

    def fetch_device_info(self):
        print("Fetching device info...")

    def add_client(self):
        print("Adding a new client...")

    def remove_client(self):
        print("Removing a client...")

    def list_clients(self):
        print("Listing all clients...")

    def save_settings(self):
        print("Settings saved.")

    def load_settings(self):
        print("Settings loaded.")

# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = ControlApp(root)
    root.mainloop()