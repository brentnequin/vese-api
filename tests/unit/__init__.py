import sys

import pytest

def run():

    sys.exit(pytest.main([
        "--cov=app"
    ]))

if __name__ == "__main__":
    run()