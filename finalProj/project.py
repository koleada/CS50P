import colorama
import re
import argparse


def main():
    print(
        f"""{colorama.Fore.CYAN}
     _      _            _   _                         
    | |    | |          | | (_)                        
  __| | ___| |_ ___  ___| |_ ___   _____   _ __  _   _ 
 / _` |/ _ \ __/ _ \/ __| __| \ \ / / _ \ | '_ \| | | |
| (_| |  __/ ||  __/ (__| |_| |\ V /  __/_| |_) | |_| |
 \__,_|\___|\__\___|\___|\__|_| \_/ \___(_) .__/ \__, |
                                          | |     __/ |
                                          |_|    |___/ 
        """
    )

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-u",
        "--url",
        type=str,
        help="URL pointing to the JS or JSON you want to search",
    )
    parser.add_argument(
        "-f", "--file", type=str, help="The JS or JSON file you want to search"
    )
    parser.add_argument(
        "-o", "--output", type=str, default=None, help="Name of the output file"
    )
    parser.add_argument(
        "--json", action="store_true", help="Flag used to specify a JSON file input"
    )
    parser.add_argument(
        "-js",
        "--javascript",
        action="store_true",
        help="Flag used to specify a javascript file input",
    )


if __name__ == "__main__":
    main()
