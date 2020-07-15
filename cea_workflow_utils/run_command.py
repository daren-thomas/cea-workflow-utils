"""
Run shell commands from cea workflows
"""
from __future__ import division
from __future__ import print_function

import cea.config
import cea.inputlocator
import subprocess

__author__ = "Daren Thomas"
__copyright__ = "Copyright 2020, Architecture and Building Systems - ETH Zurich"
__credits__ = ["Daren Thomas"]
__license__ = "MIT"
__version__ = "0.1"
__maintainer__ = "Daren Thomas"
__email__ = "cea@arch.ethz.ch"
__status__ = "Production"


def main(config):
    """
    Run the command in ``config.cmd_step.cmd`` and fail if the return code is non-zero.

    :param cea.config.Configuration config: The configuration for this script, restricted to the scripts parameters.
    :return: None
    """
    command = config.workflow_utils.command
    subprocess.run(command, shell=True, check=True)


if __name__ == '__main__':
    main(cea.config.Configuration())
