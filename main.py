"""
SEOS Main Entry Point.
"""

import sys
from core.kernel import Kernel


def main():
    kernel = Kernel()

    # Si el usuario pasa --headless, arrancamos solo el servidor API
    if "--headless" in sys.argv:
        kernel.run_headless()
    else:
        # Arranque normal con interfaz gráfica
        kernel.run()


if __name__ == "__main__":
    main()
