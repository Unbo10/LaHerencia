
# * This class is supposed to serve as the interaction with all the other
# * classes. It will contain the Data object that will store the results of
# * any optimization done while the program is running.

import toml

from pso.database.data import Data
from pso.graphics.gui import GUI
from pso.optimization import Optimization
from pyproject_hooks import __version__
class Main:
    def __init__(self) -> None:
        self.__history: Data = Data()
        self.optimizations: list[Optimization] = []
        self.gui: GUI = GUI(program_version=self.get_version())
    
    def initialize_optimization(self) -> None:
        self.__optimizations.append(Optimization())

    # def menu(self) -> None:
    #     print("------MAIN MENU-------")
    #     print("1. Create optimization")
    #     print("2. Select optimization")
    #     print("3. Delete optimization")
    #     print("4. Exit")

    def run_optimization(self) -> None:
        pass

    # def user_interface(self) -> None:
    #     exit: bool = False
    #     print("---WELCOME TO THE PARTICLE SWARM OPTIMIZATION PROGRAM!---")
    #     print("You will be able to initialize and run multiple optimizations, and store the results.")
    #     print("To exit at any point from the program press the key  combination \'Ctrl + C\'.")
    #     while not exit:
    #         print("What would you like to do?")
    #         print("1. Initialize an optimization.")
    #         print("2. Run an optimization.")
    #         print("3. Print the results of an optimization.")
    #         print("4. Exit the program.")
    #         user_input = input("Enter the number of your choice: ")
    #         if user_input == "1":
    #             self.initialize_optimization()
    #         elif user_input == "2":
    #             self.run_optimization()
    #         elif user_input == "3":
    #             pass
    #         elif user_input == "4":
    #             exit = True
    #         else:
    #             print("Invalid input. Please enter a number between 1 and 4.")

    def get_version(self) -> str:
        # Define the file path
        conf_file_path = '../pyproject.toml'

        # Load the .toml file
        data = toml.load(conf_file_path)

        # Get the version
        version = data.get('tool', {}).get('poetry', {}).get('version', 'Version not found')

        return version

if __name__ == "__main__":
    try:
        main = Main()
        print(main.get_version())
        main.user_interface()
    except KeyboardInterrupt:
        print("Exiting the program.")
        exit()

