# System 7 TUI Desktop Environment

class System7TUI:
    def __init__(self):
        self.apps = []

    def add_app(self, app_name):
        self.apps.append(app_name)
        print(f"{app_name} added to System 7 TUI.")

    def launch_app(self, app_name):
        if app_name in self.apps:
            print(f"Launching {app_name}...")
        else:
            print(f"{app_name} not found!">

    def show_apps(self):
        print("Available Apps:")
        for app in self.apps:
            print(f"- {app}")

if __name__ == '__main__':
    system7 = System7TUI()
    system7.add_app('Text Editor')
    system7.add_app('File Manager')
    system7.show_apps()
    system7.launch_app('Text Editor')
