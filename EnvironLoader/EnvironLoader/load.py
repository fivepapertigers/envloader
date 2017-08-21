""" Module for storing environment variables """
from .cli import get_input
from .db import search_env_vars

TMP_FILE = "/tmp/envloaderenv.tmp"


def main():
    print "\n--------------------------"
    print "Load environment variables"
    print "--------------------------\n"

    selected = []

    while True:
        search_term = get_input('Enter a search term: ', _require_value)
        choices = search_env_vars(search_term)
        _process_search_results(choices, selected, search_term)

        another = get_input('Would you like to search again? [Y,n] ')
        if another and another.lower() == 'n':
            break
        print '\n'

    if not selected:
        return "\nNo environment variables selected. Exiting...\n"

    with open(TMP_FILE, 'w') as tmpfile:
        print "Executing the following commands: \n"
        for selection in selected:
            command = "export {}={}".format(selection['key'], selection['val'])
            print "    {}".format(command)
            tmpfile.write(command)

        print "\nExiting."



def _process_search_results(choices, selected, search_term):
    if not choices:
        print "Search did not find any results."
    else:
        print "\nShowing results for: {}\n".format(search_term)
        while True:
            if all([chc in selected for chc in choices]):
                print "All search results selected."
                break
            print "    [a] SELECT ALL"
            for idx, choice in enumerate(choices):
                if choice not in selected:
                    print "    [{}] {}={}  # {}".format(\
                        idx, choice['key'], choice['val'], choice['description'])
            chosen = get_input("\nChoose a result: ")

            if chosen == 'a':
                select_all = [choice for choice in choices
                              if choice not in selected]

                selected = selected + select_all
                print "Selected {} environment "\
                      "variables \n".format(len(select_all))
                break

            try:
                chosen = int(chosen)
                selected.append(choices[chosen])
            except (KeyError, ValueError):
                print "ERROR: invalid selection"

def _require_value(inp):
    if inp:
        return inp
    print "ERROR: you must enter a value for this field"

if __name__ == '__main__':
    main()
