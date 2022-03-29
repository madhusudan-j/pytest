import logging
import sys,os
from optparse import OptionParser

class argument_reader:
    '''
    Get input from CLI argumnets provided by user
    '''
    def __init__(self):
        parser = OptionParser()
        parser.add_option("-i","--input_path",dest="input_path",help="Provide the input_path")
        parser.add_option("-o","--output_path",dest="output_path",help="Provide the output_path")
        parser.add_option("-t","--template",dest="template",help="Provide the template")
        parser.add_option("-u","--update",dest="update",help="Provide the update")
        (options, args) = parser.parse_args()

        # check required input arguments are given or not
        if not options.input_path or not os.path.isdir(options.input_path):
            print("Error: Input files Directory is not provided")
            logging.debug("Error: Input files Directory is not provided")
            sys.exit(1)

        if not options.output_path:
            print("Error: Output files Directory is not provided")
            logging.debug("Error: Output files Directory is not provided")
            sys.exit(1)

        if not options.template or not os.path.isfile(options.template):
            print("Error: Template file is not provided")
            logging.debug("Error: Template file not provided")
            sys.exit(1)
        
        if not options.update:
            print("Update feature is not provided")
            logging.debug("Update feature is not provided")
            sys.exit(1)

        self.input_path = options.input_path
        self.output_path = options.output_path
        self.template = options.template
        self.update = options.update

        # if the given output directory doesn't exists create the directory
        if not os.path.exists(self.output_path):
            os.makedirs(self.output_path)
            print("output directory created...... " + self.output_path)
               
