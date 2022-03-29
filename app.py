import arguments

# Get all CLI input arguments
arguments = arguments.argument_reader()
input_path = arguments.input_path
output_path = arguments.output_path
template_arxml = arguments.template
update = arguments.update

from console import MtcVersion
@app.route('/mtc', methods = ['GET'])
def mtc_install_version():
    return MtcVersion().install_mtc_console_data(request = request)