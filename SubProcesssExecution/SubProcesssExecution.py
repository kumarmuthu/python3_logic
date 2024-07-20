__version__ = "2024.07.20.01"
__author__ = "Muthukumar Subramanian"

"""
Subprocess all methods
"""

import subprocess
import sys
import platform
import multiprocessing

"""
Basic Execution:
    subprocess.run(): Execute a command and return a CompletedProcess instance.
    subprocess.call(): Execute a command and return its return code.
    subprocess.check_call(): Execute a command and raise an exception if it fails.
    subprocess.check_output(): Execute a command and return its output, raising an exception if it fails.
Shell Execution:
    subprocess.getoutput(): Execute a command in the shell and return its output as a string.
    subprocess.getstatusoutput(): Execute a command in the shell and return its status and output as a tuple.
Advanced Execution:
    subprocess.Popen(): More flexible class for process creation and management.
    Methods:
        communicate(): Send data to stdin and read from stdout and stderr.
        wait(): Wait for the process to complete.
        terminate(): Terminate the process.
        kill(): Kill the process.
"""


class SubProcessExecution:
    """
    Subprocess Execution
    """

    def __init__(self):
        self.os_type = 'unknown'
        if platform.system() == 'Linux':
            self.os_type = 'Linux'
        elif platform.system() == 'Darwin':  # macOS
            self.os_type = 'mac'
        elif platform.system() == 'Windows':
            self.os_type = 'Windows'

    def run_command(self):
        result = None
        if self.os_type == 'Windows':
            result = subprocess.run(["cmd.exe", "/c", "dir"], capture_output=True, text=True)
        elif self.os_type == 'mac' or self.os_type == 'Linux':
            result = subprocess.run(['bash', '-c', 'ls -lrt'], capture_output=True, text=True)
        print(f"run() output:\n{result.stdout}\nrun() error:\n{result.stderr}")

    def call_command(self):
        return_code = None
        if self.os_type == 'Windows':
            return_code = subprocess.call(["cmd.exe", "/c", "dir"])
        elif self.os_type == 'mac' or self.os_type == 'Linux':
            return_code = subprocess.call(['bash', '-c', 'ls -lrt'])
        print(f"call() return code: {return_code}")

    def check_call_command(self):
        try:
            if self.os_type == 'Windows':
                subprocess.check_call(["cmd.exe", "/c", "dir"])
            elif self.os_type == 'mac' or self.os_type == 'Linux':
                subprocess.check_call(['bash', '-c', 'ls -lrt'])
            print("check_call() succeeded")
        except subprocess.CalledProcessError as e:
            print(f"check_call() failed with return code {e.returncode}")

    def check_output_command(self):
        output = None
        try:
            if self.os_type == 'Windows':
                output = subprocess.check_output(["cmd.exe", "/c", "dir"], text=True)
            elif self.os_type == 'mac' or self.os_type == 'Linux':
                output = subprocess.check_output(['bash', '-c', 'ls -lrt'], text=True)
            print(f"check_output() output:\n{output}")
        except subprocess.CalledProcessError as e:
            print(f"check_output() failed with return code {e.returncode}")

    def getoutput_command(self):
        output = None
        if self.os_type == 'Windows':
            output = subprocess.getoutput("dir")
        elif self.os_type == 'mac' or self.os_type == 'Linux':
            output = subprocess.getoutput("ls -lrt")
        print(f"getoutput() output:\n{output}")

    def getstatusoutput_command(self):
        status = None
        output = None
        if self.os_type == 'Windows':
            status, output = subprocess.getstatusoutput("dir")
        elif self.os_type == 'mac' or self.os_type == 'Linux':
            status, output = subprocess.getstatusoutput("ls -lrt")
        print(f"getstatusoutput() status: {status}\ngetstatusoutput() output:\n{output}")

    def store_output_on_variable(self):
        if self.os_type == 'Windows':
            sub_process_obj_win = subprocess.Popen(["cmd.exe", "/c", "dir"], stdout=subprocess.PIPE,
                                                   stderr=subprocess.PIPE, text=True)
            output_data, output_err_data = sub_process_obj_win.communicate()
            sub_process_obj_win.terminate()
            print(f"Windows output_data:\n {output_data}\noutput_err_data:\n {output_err_data}")

        elif self.os_type == 'mac' or self.os_type == 'Linux':
            sub_process_obj_mac = subprocess.Popen(['bash', '-c', 'ls -lrt'], stdout=subprocess.PIPE,
                                                   stderr=subprocess.PIPE, text=True)
            output_data, output_err_data = sub_process_obj_mac.communicate()
            sub_process_obj_mac.terminate()
            print(f"{self.os_type} output_data:\n {output_data}\noutput_err_data:\n {output_err_data}")

    def print_output_on_console(self):
        if self.os_type == 'Windows':
            sub_process_popen_obj_win = subprocess.Popen(["cmd.exe", "/c", "dir"], stdout=sys.stdout,
                                                         stderr=sys.stderr, text=True)
            sub_process_popen_obj_win.communicate()
            sub_process_popen_obj_win.terminate()
            print('Windows data Displayed on console')

        elif self.os_type == 'mac' or self.os_type == 'Linux':
            sub_process_obj_mac = subprocess.Popen(['bash', '-c', 'ls -lrt'], stdout=sys.stdout,
                                                   stderr=sys.stderr, text=True)
            sub_process_obj_mac.communicate()
            sub_process_obj_mac.terminate()
            print(f'{self.os_type} data Displayed on console')


def main_script():
    cls_obj = SubProcessExecution()
    print("{:#^60}".format("store_output_on_variable Start"))
    cls_obj.store_output_on_variable()
    print("{:#^60}".format("store_output_on_variable End"))

    print("{:#^60}".format("print_output_on_console Start"))
    cls_obj.print_output_on_console()
    print("{:#^60}".format("print_output_on_console End"))

    print("{:#^60}".format("run_command Start"))
    cls_obj.run_command()
    print("{:#^60}".format("run_command End"))

    print("{:#^60}".format("call_command Start"))
    cls_obj.call_command()
    print("{:#^60}".format("call_command End"))

    print("{:#^60}".format("check_call_command Start"))
    cls_obj.check_call_command()
    print("{:#^60}".format("check_call_command End"))

    print("{:#^60}".format("check_output_command Start"))
    cls_obj.check_output_command()
    print("{:#^60}".format("check_output_command End"))

    print("{:#^60}".format("getoutput_command Start"))
    cls_obj.getoutput_command()
    print("{:#^60}".format("getoutput_command End"))

    print("{:#^60}".format("getstatusoutput_command Start"))
    cls_obj.getstatusoutput_command()
    print("{:#^60}".format("getstatusoutput_command End"))


if __name__ == '__main__':
    print("{:#^30}".format("Script Start"))
    multiprocess_obj = multiprocessing.Process(target=main_script)
    multiprocess_obj.start()
    multiprocess_obj.join(timeout=15)
    if multiprocess_obj.is_alive():
        multiprocess_obj.terminate()

    print("{:#^30}".format("Script End"))
