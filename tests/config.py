server_ip = "192.168.0.1"

API = {
    "base": "http://" + server_ip + ":8000/api",
}

database = {
    "host": "localhost",
    "dbname": "fitcrack",
    "user": "root",
    "password": "root",
    "port": 3306
}

tests = {
    "home": "/home/boincadm/tests/"
}

project = {
    "home": "/home/boincadm/projects/test_fitcrack/",
    "app_name": "fitcrack"
}

template = {
    "home": project["home"] + "templates/",
    "bench_in": project["home"] + "templates/bench_in",
    "app_out": project["home"] + "templates/app_out"
}

in_files = {
    "home": tests["home"] + "in/",
    "runner": {
        "config_bench": tests["home"] + "in/runner/config_bench",
        "config_dict": tests["home"] + "in/runner/config_dict",
        "config_comb": tests["home"] + "in/runner/config_comb",
        "config_mask": tests["home"] + "in/runner/config_mask",
        "hc_error": tests["home"] + "in/runner/hc_error",
        "hc_bench_out": tests["home"] + "in/runner/hc_bench_out",
        "hc_bench_out_warning": tests["home"] + "in/runner/hc_bench_out_warning",
        "hc_mask_out_found": tests["home"] + "in/runner/hc_mask_out_found",
        "hc_mask_out_not_found": tests["home"] + "in/runner/hc_mask_out_not_found",
        "hc_dict_out_found": tests["home"] + "in/runner/hc_dict_out_found",
        "hc_dict_out_not_found": tests["home"] + "in/runner/hc_dict_out_not_found",
        "hc_comb_out_found": tests["home"] + "in/runner/hc_comb_out_found",
        "hc_comb_out_not_found": tests["home"] + "in/runner/hc_comb_out_not_found",
    },
    "assimilator": {
        "bench_ok": tests["home"] + "in/assimilator/bench_ok",
        "bench_error": tests["home"] + "in/assimilator/bench_error",
        "normal_found": tests["home"] + "in/assimilator/normal_found",
        "normal_not_found": tests["home"] + "in/assimilator/normal_not_found",
        "normal_hc_error": tests["home"] + "in/assimilator/normal_hc_error",
    },
    "API": {
        "attack_modes": tests["home"] + "in/API/attack_modes",
        "hash_types": tests["home"] + "in/API/hash_types"
    },
    "example_dict": {
        "name": "example.dict",
        "path": "/home/boincadm/dictionaries/example.dict",
        "keyspace": 129989,
    },
}

runner = {
    "path": "./",
    "bin": "runner217.bin",
    "hashcat": "hashcat64.bin",
    "command_log": "runner_command.txt",
    "stderr": "stderr.txt",
    "local.conf": "local.conf",
    "test_hash": "4ac1b63dca561d274c6055ebf3ed97db",
}

charsets = {
    "path": "/home/boincadm/charsets/",
}

rules = {
    "path": "/home/boincadm/rules/",
}

dictionaries = {
    "path": "/home/boincadm/dictionaries/",
    "test_dict": {
        "path": "/home/boincadm/dictionaries/test_dict.txt",
        "name": "test_dict",
        "keyspace": 4,
    }
}

logs_path = project["home"] + "log_fitcrack-dev/"
