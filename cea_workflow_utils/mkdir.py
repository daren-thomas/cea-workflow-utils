"""
Create a directory if it doesn't exist yet
"""
from __future__ import division
from __future__ import print_function

import cea.config
import cea.inputlocator
import os

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
    Create a directory (if it doesn't exist yet)

    :param cea.config.Configuration config: The configuration for this script, restricted to the scripts parameters.
    :return: None
    """
    directory = config.workflow_utils.directory
    directory = os.path.abspath(directory)
    directory = os.path.normpath(directory)
    if not os.path.exists(directory):
        os.makedirs(directory)
    print(f"mkdir: Created directory {directory}")


if __name__ == '__main__':
    main(cea.config.Configuration())
