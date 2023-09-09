class TaskManager:
    def __init__(self) -> None:
        """Initialize the task manager."""
        self._task_list = {}
        self._task_number = 0
    
    def add(self, task_text, task_status=False):
        """
        Add a new task to the task list.

        Parameters:
        - task_text (str): The text of the task.
        - task_status (bool, optional): The status of the task (default is False).
        """
        task_name = f"Task {self._task_number}"
        self._task_list[task_name] = [task_text, task_status]
        self._task_number += 1
    
    def delete(self, task_name):
        """
        Delete a task from the task list.

        Parameters:
        - task_name (str): The name of the task to delete.
        """
        if task_name in self._task_list:
            self._task_list.pop(task_name)
        else:
            print("Task not found")
    
    def complete(self, task_name):
        """
        Mark a task as completed.

        Parameters:
        - task_name (str): The name of the task to mark as completed.
        """
        if task_name in self._task_list:
            self._task_list[task_name][1] = True
        else:
            print("Task not found")
        
    def display(self):
        """Display the list of tasks."""
        print()
        for key, value in self._task_list.items():
            task_name = key
            task_text = value[0]
            task_status = ("Not completed", "Completed")[value[1]]
            print(task_name)
            print(task_text)
            print(task_status)
            print()


class UserInterface:
    def __init__(self) -> None:
        """Initialize the user interface."""
        self.command_list = {
            "add": "Add a new task to the task list.",
            "delete": "Delete a task from the task list.",
            "complete": "Mark a task as completed.",
            "display": "Display the list of tasks.",
            "quit": "Quit the program."
        }
        
    def show_start_message(self):
        """Display the program start message."""
        print("\n", "The program is running".center(60), "\n")
    
    def show_end_message(self):
        """Display the program end message."""
        print("\n", "The program is shut down".center(60), "\n")
    
    def get_help(self):
        """Display available commands and their descriptions."""
        print("\nAvailable commands:\n")
        for command, description in self.command_list.items():
            print(f"\t{command}: {description}", end='\n\n')


class ProgramManager:
    def __init__(self, task, interface):
        """
        Initialize the program manager.

        Parameters:
        - task (TaskManager): An instance of the TaskManager class.
        - interface (UserInterface): An instance of the UserInterface class.
        """
        self.task = task()
        self.interface = interface()
        self.running = True

    def start(self):
        """Start and manage the program loop."""
        self.interface.show_start_message()

        while self.running:
            user_input = input("Enter a command: ").strip()

            if user_input == "quit":
                self.running = False
            elif user_input == "display":
                self.task.display()
            elif user_input == "add":
                self.task.add(input("Write your task: ").strip())
            elif user_input == "delete":
                self.task.delete(input("Write task name to delete: "))
            elif user_input == "complete":
                self.task.complete(input("Write task name to mark complete: "))
            elif user_input == "help":
                self.interface.get_help()
            else:
                print("Invalid command. Type 'help' to see available commands.")
        
        self.interface.show_end_message()


a = ProgramManager(TaskManager, UserInterface)
a.start()
