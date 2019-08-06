import inspect
import os
import sys


def reload_modules(user_path=None):

    # Get the user path to clear out
    if not user_path:
        user_path = os.path.dirname(__file__).lower()

    # loop over the modules and add ones belonging to this path to the
    # delete list
    to_delete = []
    print('\n---')
    for key, module in sys.modules.iteritems():
        try:
            # Get the path to the module
            module_file_path = inspect.getfile(module).lower()

            # Don't remove the startup script
            if module_file_path == __file__.lower():
                continue

            # find modules in the user path and add them to delete
            if module_file_path.startswith(user_path):
                print('removing module: {}'.format(key))
                to_delete.append(key)

        except:
            pass

    # delete these modules
    for module in to_delete:
        del (sys.modules[module])

    print('---\n')


def start():
    reload_modules()

    # start the main window
    import mayaunittestui
    mayaunittestui.show()
