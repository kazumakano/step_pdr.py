import os.path as path
from glob import iglob
from typing import Union
import script.parameter as param
from script.log import Log


def prepare_log_pkls(src_file: Union[str, None] = None) -> None:
    if src_file is None:
        for src_file in iglob(path.join(param.ROOT_DIR, "log/*.csv")):
            Log(file_name=src_file).export_to_pkl(src_file)

    else:
        Log(file_name=src_file).export_to_pkl(src_file)

if __name__ == "__main__":
    import argparse
    from script.parameter import set_params

    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--config", help="specify your config file", metavar="PATH_TO_CONFIG_FILE")
    parser.add_argument("--src_file", help="specify sourse file", metavar="PATH_TO_SRC_FILE")
    args = parser.parse_args()

    set_params(args.config)

    prepare_log_pkls(args.src_file)
