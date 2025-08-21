import sys
import time

def progress_bar(iterable, prefix="", size=40, file=sys.stdout):
    """
    Display a progress bar for any iterable.
    
    :param iterable: iterable (e.g., range, list, etc.)
    :param prefix: text before the bar
    :param size: bar width
    :param file: output stream
    """
    total = len(iterable)

    def show(j):
        x = int(size * j / total)
        file.write("%s[%s%s] %i/%i\r" % (prefix, "#" * x, "." * (size - x), j, total))
        file.flush()

    show(0)
    for i, item in enumerate(iterable, 1):
        yield item
        show(i)
    file.write("\n")
    file.flush()
