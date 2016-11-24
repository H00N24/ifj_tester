#!/usr/bin/python3

'''
Testovaci skript pre ifj projekt
'''

import os,sys,re
from subprocess import Popen, PIPE

print('---IFJ test script---\n')

if len(sys.argv) != 2:
    print("ERROR: 2 arguments expected", file = sys.stderr)
    sys.exit(0)

signals = {}
with open(".signals") as input_file:
    for line in input_file:
        tmp = line[:-1].split('\t')
        tmp[1] = - int(tmp[1])
        signals[tmp[1]] = tmp[0] + ": " + tmp[2]

test_list = []
with open("test_list.txt") as input_file:
    for line in input_file:
        if line.startswith('#') or line == '\n':
            continue
        test_list.append(line[:-1].split('\t'))

test_dir = os.path.abspath('./test/') + '/'
log_dir  = os.path.abspath('./logs/') + '/'
test_files = os.listdir(test_dir)

if os.path.exists(sys.argv[1]) and os.path.isfile(sys.argv[1]):
    bin_path = os.path.abspath(sys.argv[1])
else:
    print("ERROR: argv[1] is not a file or does not exists", file = sys.stderr)
    sys.exit(0)

score = {}
score["ok"] = 0
score["fail"] = 0

for test in test_list:
    print("Test: \"" + test[0] + "\"")

    test_path = test_dir + test[1]
    code_path = test_path + ".code"
    out_path = test_path +  ".out"

    log_path = log_dir + test[1]
    err_save = log_path + ".stderr"
    out_save = log_path + ".stdout"

    real_rc = int(test[2])
    real_out = ""
    try:
        with open(out_path) as input_file:
            real_out = input_file.read()
    except:
        pass

    cmd = bin_path + " " + code_path
    process = Popen(cmd.split(' '), stdout = PIPE, stderr = PIPE, stdin  = PIPE,)
    out, err = process.communicate()

    proc_out = out.decode('utf-8')
    proc_err = err.decode('utf-8')
    proc_rc  = int(process.returncode)

    with open(err_save, 'w') as err_file, open(out_save,'w') as out_file:
        err_file.write(proc_err)
        out_file.write(proc_out)

    result = real_rc == proc_rc and real_out == proc_out

    print('  Return code:',real_rc == proc_rc)
    print('    Your return code:', proc_rc)
    print('    Real return code:', real_rc)
    print('  Stdout:', real_out == proc_out )
    print('    stdout saved: ./logs/' +  test[1] + ".stdout")
    print('    stderr saved: ./logs/' +  test[1] + ".stderr")
    if proc_rc in signals:
        print('  Signal:',signals[proc_rc])
    if result:
        print('  Test OK\n')
        score["ok"] += 1
    else:
        print('  Test FAILED\n')
        score["fail"] += 1


print("DONE, ok:", score["ok"], "failed:", score["fail"] )
