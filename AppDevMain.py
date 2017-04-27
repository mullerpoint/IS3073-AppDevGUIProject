#!/usr/bin/env python

##########################################################
#
# Imports
#
##########################################################

import sys                                      # Used for UI Threads
from PyQt5 import QtCore, QtGui, QtWidgets      # Used for Graphical UI
from AppDevGUI import Ui_MainWindow             # Main Window Class
from help import Ui_helpDialog                  # About Dialog Window Class
from version import Ui_versionDialog            # Version Dialog Window Class
import numpy as np                              # Used For Statistics Functions
import pandas as pd                             # Used for importing and holding data

##########################################################
#
# UI Controller Class
#
##########################################################


class AppDevProgram(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        # initialize the main window using the Ui_MainWindow Class (our class that has all the design stuff) and
        # the QMainWindow Class (Qt class with all the relevant functions to build the window)
        super(self.__class__, self).__init__()

        # Setup the UI
        self.setupUi(self)

        # Create an empty Pandas dataframe to store data in later
        self.pd_data = pd.DataFrame()

        # Create a bool variable that can tell us if a data file has been opened
        self.got_data = False

        """
        Connect Menu Items to Functions
        """
        # connect Help menu item to help window
        self.actionAbout.triggered.connect(self.menu_launchhelp)
        # connect version menu item to version window
        self.actionVersion.triggered.connect(self.menu_launchver)
        # connect open menu item to open file window
        self.actionOpen.triggered.connect(self.menu_launchopen)
        # connect open menu item to open file window
        self.actionQuit.triggered.connect(self.quit)

        """ 
        Connect Main Window Buttons to Functions
        """
        # connect the Mean Button to the calculate median function
        self.medButton.clicked.connect(self.calc_med)
        # connect the average Button to the calculate average function
        self.avgButton.clicked.connect(self.calc_avg)
        # connect the STD Button to the calculate STD function
        self.stdDevButton.clicked.connect(self.calc_std)
        # connect the min max Button to the identify min/max function
        self.maxMinButton.clicked.connect(self.calc_maxmin)
        # connect the calc all Button to the calculate all function
        self.calcAllButton.clicked.connect(self.calc_all)
        # connect the quit Button to the quit function
        self.quitButton.clicked.connect(self.quit)

    ##########################################################
    # Menu Function Definitions
    ##########################################################

    @staticmethod
    def menu_launchhelp():
        # Launch the help dialog window

        # Create a Dialog Instance
        help_dialog = QtWidgets.QDialog()
        # Define the design to use
        help_dialog.ui = Ui_helpDialog()
        # setup the UI in the dialog
        help_dialog.ui.setupUi(help_dialog)
        # start the Dialog instance
        help_dialog.exec_()
        # show the dialog
        help_dialog.show()

        return

    @staticmethod
    def menu_launchver():
        # launch the Version dialog window

        # Create a Dialog Instance
        ver_dialog = QtWidgets.QDialog()
        # Define the design to use
        ver_dialog.ui = Ui_versionDialog()
        # setup the UI in the dialog
        ver_dialog.ui.setupUi(ver_dialog)
        # start the Dialog instance
        ver_dialog.exec_()
        # show the dialog
        ver_dialog.show()

        return

    def menu_launchopen(self):
        # open the file open dialog window

        # create a file dialog with title Open File
        selected_file = QtWidgets.QFileDialog.getOpenFileName(self, "Open File")

        if selected_file[0] == '':
            # return success no file
            return 2
        else:
            # Send the file to be opened; file is a tuple we only need the first string
            new_data = self.open_file(selected_file[0])
            # append the new data to the class data frame
            self.pdData = new_data

            # Set the got data function to true
            self.got_data = True

            # return success file
            return 1

    def quit(self):
        sys.exit(app.exec())

    ##########################################################
    # Window Button Function Definitions
    ##########################################################
    def calc_med(self, clear=True):
        # calculate the median of a list of numbers
        # if no file has been opened don't try to perform calculations
        if self.got_data:  # == True

            # Perform calculation using pandas dataframe median function
            # we select the column from the dataframe and call the median function
            med = self.pdData['number'].median()

            # Create a Solution String
            out_string = "The median number of name occurrences is: " + str(med)

            # Output the solution
            self.output(out_string, clear)
        else:
            # print an error message so the user knows what happened
            self.output("No file opened", clear)

        # Return success
        return 1

    def calc_avg(self, clear=True):
        # calculate the mean/average of a list of numbers
        # if no file has been opened don't try to perform calculations
        if self.got_data:  # == True

            # Perform calculation using pandas dataframe mean function
            # we select the column from the dataframe and call the mean function
            avg = self.pdData['number'].mean()

            # Create Solution String
            out_string = "The average number of occurrences for each name is: " + str(avg)

            # output the result of the calculation
            self.output(out_string, clear)
        else:
            # print an error message so the user knows what happened
            self.output("No file opened", clear)

        # Return Success
        return 1

    def calc_std(self, clear=True):
        # calculate the standard deviation of a list of numbers

        # if no file has been opened don't try to perform calculations
        if self.got_data:  # == True

            # Perform calculation using numpy standard deviation function
            # we select the column from the dataframe and pass it to numpy to calculate
            stddev = np.std(self.pdData['number'])

            # Create Solution String
            out_string = "The standard deviation of name occurrences is: " + str(stddev)

            # Output results of calculation
            self.output(out_string, clear)
        else:
            # print an error message so the user knows what happened
            self.output("No file opened", clear)

        # Return Success
        return 1

    def calc_maxmin(self, clear=True):
        # identify the minimum and maximum of a list of numbers

        # if no file has been opened don't try to perform calculations
        if self.got_data:  # == True

            # create groups of name occurrence numbers based by splitting up genders
            gender_list = self.pdData['number'].groupby(self.pdData['gender'])

            # Calculate the indexes of the max values
            max_index = gender_list.idxmax()

            # Calculate the indexes of the min values
            min_index = gender_list.idxmin()

            # Create a blank string to fill
            out_string = ''

            # Add Max string to the output string
            out_string = out_string + "The Most Common Names are: \n"
            # iterate through the index values in max_index saving each one as idxvals to work with
            for idxvals in max_index:
                # get the data at index idxvals from pdData store it in max_item
                max_item = self.pdData.ix[idxvals]

                # Craft a string
                new_string = "Name:        " + str(max_item.ix[0]) + '\n' +\
                             "Gender:      " + str(max_item.ix[1]) + '\n' +\
                             "Occurrences: " + str(max_item.ix[2]) + '\n\n'

                # Add the string to the output string
                out_string = out_string + new_string

            # Add Min string to the output string
            out_string = out_string + "The Least Common Names are: \n"
            # iterate through the index values in min_index saving each one as idxvals to work with
            for idxvals in min_index:
                # get the data at index idxvals from pdData store it in max_item
                min_item = self.pdData.ix[idxvals]

                # Craft a string
                new_string = "Name:        " + str(min_item.ix[0]) + '\n' + \
                             "Gender:      " + str(min_item.ix[1]) + '\n' + \
                             "Occurrences: " + str(min_item.ix[2]) + '\n\n'

                # Add the string to the output string
                out_string = out_string + new_string

            # output results of calculations
            self.output(out_string, clear)

        else:
            # print an error message so teh user knows what happened
            self.output("No file opened", clear)

        # Return Success
        return 1

    def calc_all(self):
        # perform all of the above calculations

        self.calc_med(False)
        self.calc_avg(False)
        self.calc_std(False)
        self.calc_maxmin(False)

        # return success
        return 1

    ##########################################################
    # Helper functions
    ##########################################################

    def output(self, str_output, clear=False):
        # print strOutput to the text box on the GUI
        # if a clear is requested before output clear the text edit box
        if clear:
            self.textEdit.clear()
        # append the text from strOutput to the text edit box
        self.textEdit.append(str_output)

    # noinspection PyMethodMayBeStatic
    def open_file(self, file):
        # Open a file and save the data to a pandas dataframe

        # Read csv file in to variable data
        data = pd.read_csv(file, names=['name', 'gender', 'number'])

        return data


##########################################################
#
# Main Function
#
##########################################################

# Start a new QApplication instance
app = QtWidgets.QApplication(sys.argv)

# Set the application design/form/template to use
form = AppDevProgram()

# Show the form
form.show()

# Start the application/GUI loop
sys.exit(app.exec_())


